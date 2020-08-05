# -*- coding: utf-8 -*-

import socket
import smtplib
from email.mime.text import MIMEText
import logging.handlers
import ConfigParser
import time
from threading import Timer
import paramiko
import sys
import array

reload(sys)
sys.setdefaultencoding('utf-8')

# 定义一个RotatingFileHandler，最多备份10个日志文件，每个日志文件最大1M
LOG_FILENAME = 'udp_port_health_check.log'
# Set up a specific logger with our desired output level
my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(filename)s - [line:%(lineno)d] - %(levelname)s - %(message)s')

handler = logging.handlers.RotatingFileHandler(LOG_FILENAME, maxBytes=1024*1024, backupCount=10)
handler.setFormatter(formatter)
my_logger.addHandler(handler)

# 检查间隔60s
timer_interval = 60

check_data = array.array('B',[0x29,0x29,0x80,0x00,0x99,0x00,0x00,0x00,0x01,0x18,0x08,
                              0x28,0x09,0x02,0x29,0x03,0x60,0x69,0x10,0x12,0x02,0x45,
                              0x34,0x00,0x00,0x00,0x01,0x7f,0x00,0x00,0x00,0xff,0xf7,
                              0x5f,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0x00,0x00,
                              0x14,0x00,0x24,0x34,0x36,0x30,0x3b,0x30,0x30,0x3b,0x32,
                              0x31,0x35,0x31,0x34,0x3b,0x33,0x37,0x36,0x33,0x32,0x00,
                              0x05,0x00,0x04,0x30,0x70,0x20,0x00,0x04,0x00,0x08,0x05,
                              0xc2,0x00,0x16,0x00,0xa3,0x42,0x53,0x4a,0x41,0x35,0x43,
                              0x38,0x20,0x42,0x53,0x4a,0x5f,0x58,0x55,0x56,0x31,0x2e,
                              0x34,0x3b,0xfe,0x00,0x06,0x00,0xa5,0x00,0x00,0x00,0x0c,
                              0x00,0x06,0x00,0x89,0xff,0xff,0xff,0xff,0x00,0x24,0x00,
                              0xa9,0x01,0xcc,0x00,0x01,0x54,0x0a,0x93,0x00,0x13,0x00,
                              0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
                              0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,
                              0x00,0x00,0x0c,0x0d])

A5C_response_data = array.array('B',[0x29,0x29,0x21,0x00,0x05,0x0c,0x80,0x00,0xa8,0x0d])
M11_response_data = array.array('B',[0x29,0x29,0x21,0x00,0x05,0x0c,0x80,0x18,0xb0,0x0d])

def checkUdpPort(myconf):
    udpServerList = myconf[10].split(",")
    for udpServer in udpServerList:
        udpIpAndPort = udpServer.split(":")
        try:
            '''
                客户端使用UDP时，首先仍然创建基于UDP的Socket，
                然后，不需要调用connect()，直接通过sendto()给服务器发数据：
            '''
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.settimeout(10)

            # 发送数据:
            s.sendto(check_data, (udpIpAndPort[0], int(udpIpAndPort[1])))
            # 接收数据:
            responseMsg = s.recv(1024)
            byteArray = array.array('B', responseMsg)
            if(A5C_response_data == byteArray or M11_response_data == byteArray):
                # print(responseMsg.encode('hex'))
                my_logger.info(udpIpAndPort[0] + ':' + udpIpAndPort[1] + ' udp port health!')
            else:
                raise Exception("responseMsg error!")
        except Exception as ex:
            # 重启端口
            my_logger.error(udpIpAndPort[0] + ':' + udpIpAndPort[1]
                            + ' udp port error!' + ex.message, exc_info=True)
            send_mail(udpIpAndPort[0] + ':' + udpIpAndPort[1]
                            + ' udp port error!' + ex.message, u'请确认端口重启！')
            serverPort = udpIpAndPort[1]
            serverConfig = getuserpwd(udpIpAndPort[0])
            proc_restart(serverConfig[0], serverConfig[1],
                         serverConfig[2], serverConfig[3],
                         serverPort, serverConfig[4])
        finally:
            s.close()

def send_mail(subject, msg):
    try:
        msg_fmt = MIMEText(msg,_subtype='html',_charset='utf-8')
        msg_fmt['From'] = myconf[7]
        mailto = myconf[9].split(',')
        msg_fmt['Subject'] = subject
        msg_fmt['To'] = ','.join(mailto)
        s = smtplib.SMTP_SSL(myconf[6], 465)
        s.login(myconf[7], myconf[8])
        s.sendmail(msg_fmt['From'], mailto, msg_fmt.as_string())
        s.close()
        my_logger.info('main-mailer send mail succeeded!')
    except Exception as ex:
        my_logger.error('main-mailer send mail failed! ' + ex.message, exc_info=True)
        send_mail_err(subject, msg)

def send_mail_err(subject, msg):
    try:
        cf = ConfigParser.ConfigParser()
        cf.read("setting.conf")
        mail_host = cf.get("mail_err", "mail_host")
        mail_user = cf.get("mail_err", "mail_user")
        mail_pwd = cf.get("mail_err", "mail_pwd")
        mail_to = cf.get("mail_err", "mail_to")

        msg_fmt=MIMEText(msg, _subtype='html', _charset='utf-8')
        msg_fmt['From'] = mail_user
        mailto = mail_to.split(',')
        msg_fmt['Subject'] = subject
        msg_fmt['To'] = ','.join(mailto)
        mt = smtplib.SMTP_SSL(mail_host, 465)
        mt.login(mail_user, mail_pwd)
        mt.sendmail(msg_fmt['From'], mailto, msg_fmt.as_string())
        mt.close()
        my_logger.info('reserve-mailer send mail succeeded!')
    except Exception as ex:
        my_logger.error('reserve-mailer send mail failed!' + ex.message, exc_info=True)

def readconf():
    cf = ConfigParser.ConfigParser()
    cf.read("setting.conf")
    db_host = cf.get("db_new", "db_host")
    db_port = cf.getint("db_new", "db_port")
    db_user = cf.get("db_new", "db_user")
    db_pwd = cf.get("db_new", "db_pwd")
    db_db = cf.get("db_new", "db_db")
    db_charset = cf.get("db_new", "db_charset")

    mail_host = cf.get("mail", "mail_host")
    mail_user = cf.get("mail", "mail_user")
    mail_pwd = cf.get("mail", "mail_pwd")
    mail_to = cf.get("mail", "mail_to")

    check_ip_port = cf.get("udp", "check_ip_port")
    return db_host, db_port, db_user, db_pwd, db_db, \
           db_charset, mail_host, mail_user, mail_pwd, mail_to, check_ip_port

# 重启端口
def proc_restart(ip, port, user, pwd, proc_port, platform):
    restart_result = ''
    try:
        # 连接服务器
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        client.connect(ip, port, user, pwd, timeout=5)

        # 查看进程是否存在
        proc_num = 0
        stdin, stdout, stderr = client.exec_command("/bin/ps aux | grep '\-host\-port %s' | grep -v grep" % (proc_port))
        outLines = stdout.readlines()
        errorLines = stderr.readlines()
        for std in outLines:
            my_logger.info('before restart ' + ip + ':' + proc_port + ' ' + std.strip('\n'))
            proc_num += 1
        for std2 in errorLines:
            my_logger.error('before restart ' + ip + ':' + proc_port + ' ' + std2.strip('\n'))
            restart_result = '失败'
        if restart_result == '失败':
            mail_title = ip + ':' + proc_port + " " + platform \
                         + ' udp端口监控报警需重启，自动重启失败，请立即确认！'
            send_mail(mail_title, mail_title)
            return restart_result
        # 如果进程存在则先杀死进程
        stopCmd = "/root/1-runlatest-trunk-" + platform + "/2-stopContainer.sh %s"
        if proc_num > 0:
            print(stopCmd % (proc_port))
            stdin, stdout, stderr = client.exec_command(stopCmd % (proc_port))
            outLines = stdout.readlines()
            errorLines = stderr.readlines()
            for std1 in outLines:
                my_logger.info('stopContainer ' + ip + ':' + proc_port + ' ' + std1.strip('\n'))
            for std2 in errorLines:
                my_logger.error('stopContainer ' + ip + ':' + proc_port + ' ' + std2.strip('\n'))
                restart_result = '失败'
            if restart_result == '失败':
                mail_title = getFailMailTitle(ip, proc_port, platform)
                send_mail(mail_title, mail_title)
                return restart_result
        # 启动进程
        startCmd = "/root/1-runlatest-trunk-" + platform + "/1-startContainers.sh %s"
        print(startCmd % (proc_port))
        stdin, stdout, stderr = client.exec_command(startCmd % (proc_port))
        outLines = stdout.readlines()
        errorLines = stderr.readlines()
        for std in outLines:
            my_logger.info('startContainers ' + ip + ':' + proc_port + ' ' + std.strip('\n'))
        for std in errorLines:
            my_logger.error('startContainers ' + ip + ':' + proc_port + ' ' + std.strip('\n'))
            restart_result = '失败'
        if restart_result == '失败':
            mail_title = getFailMailTitle(ip, proc_port, platform)
            send_mail(mail_title, mail_title)
            return restart_result
        # 检查启动结果并写到log
        time.sleep(15)
        stdin, stdout, stderr = client.exec_command("/bin/ps aux | grep '\-host\-port %s' | grep -v grep" % (proc_port))
        outLines = stdout.readlines()
        errorLines = stderr.readlines()
        for std in outLines:
            ddm_proc = std.strip('\n')
            if any(ddm_proc) == True:
                restart_result = '成功'
                my_logger.info('restartResult ' + ip + ':' + proc_port + ' restart succeeded。' + '\n' + ddm_proc)
        for std in errorLines:
            my_logger.error('restartResult ' + ip + ':' + proc_port + ' ' + std.strip('\n'))
            restart_result = '失败'
        if restart_result == '失败':
            mail_title = getFailMailTitle(ip, proc_port, platform)
            send_mail(mail_title, mail_title)
            return restart_result

        # htop信息写到log
        fileName = ip + '_' + time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
        client.exec_command("/usr/bin/top -b -n1 >> /maindisk/ops/log/htop/top_%s.txt" % (fileName))
        client.exec_command("/usr/bin/ps auxf >> /maindisk/ops/log/htop/ps_%s.txt" % (fileName))

        client.close()
        return restart_result
    except Exception as ex:
        send_mail(platform + u' udp端口健康检查程序出现异常，请确认！', u'请确认日志内容！')

def getFailMailTitle(ip, proc_port, platform):
    return ip + ':' + proc_port + " " + platform \
        + ' udp端口健康检查程序出现异常，自动重启失败，请立即确认！'

def getuserpwd(ip):
    cf = ConfigParser.ConfigParser()
    cf.read("setting.conf")
    port = cf.get(ip, "server_port")
    user = cf.get(ip, "login_user")
    pwd = cf.get(ip, "login_pw")
    platform = cf.get(ip, "platform")

    return ip, port, user, pwd, platform

if __name__ == '__main__':
    # ip = "192.168.1.100"
    # serverPort = "25013"
    # serverConfig = getuserpwd(ip)
    # proc_restart(serverConfig[0], serverConfig[1], serverConfig[2], serverConfig[3], serverPort)

    try:
        myconf = readconf()
        t = Timer(timer_interval, checkUdpPort)
        while True:
            checkUdpPort(myconf)
            time.sleep(timer_interval)
    except Exception as ex:
        send_mail(u'p1 udp端口健康检查程序出现异常，请确认！', u'请确认日志内容！')