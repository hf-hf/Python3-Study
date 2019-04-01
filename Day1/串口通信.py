# coding=utf-8
import serial
#import pyserial
#import pymysql
import threading
import time
x = serial.Serial('COM2', 9600)#这是我的串口，测试连接成功，没毛病
# i=0
def fasong():#发送函数
    while True:
        time.sleep(3)
        myinput= bytes([0X01,0X03,0X00,0X00,0X00,0X01,0X84,0X0A])
        #这是我要发送的命令，原本命令是：01 03 00 00 00 01 84 0A
        x.write(myinput)
def jieshou():#接收函数
    while True:
        while x.inWaiting()>0:
            # 读取串口传过来的字节流，这里我根据文档只接收7个字节的数据
            myout = x.read_all()
            for y in myout:
                print(hex(y))
            #datas =''.join(map(lambda x:('/x' if len(hex(x))>=4 else '/x0')+hex(x)[2:],myout))#将数据转成十六进制的形式
            #new_datas = datas.split("/x")#将字符串分割，拼接下标4和5部分的数据
            #need = new_datas[4]+new_datas[5];#need是拼接出来的数据，比如：001a
            #my_need = int(hex(datas),16)#将十六进制转化为十进制
            #print(datas)
            # sql = "INSERT INTO VOC_DATA(value,create_time)VALUES('"+str(my_need)+"',"+str(int(time.time()))+")"
            # 使用 execute()  方法执行 SQL 查询
            # 执行sql语句
            # cursor.execute(sql)
            # 提交到数据库执行
            # db.commit()


if __name__== '__main__':
    # 打开数据库连接
    # db = pymysql.connect("localhost","root","123456789","voc" )
    # 使用 cursor() 方法创建一个游标对象 cursor
    # cursor = db.cursor()
    # 线程1：不断的去请求数据
    t1 = threading.Thread(target=jieshou,name="jieshou")
    # 线程2：不断地去接收数据
    # t2= threading.Thread(target=fasong, name="fasong")
    # t2.start()#开启线程1
    t1.start()#开启线程2