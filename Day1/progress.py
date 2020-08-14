# -*- coding: utf-8 -*-

def make_graph(percent):
    '''Make progress graph from API graph'''
    done_block = '█'
    empty_block = '░'
    pc_rnd = round(percent)
    return "{}{}".format(done_block*int(pc_rnd/4), empty_block*int(25-int(pc_rnd/4)))

if __name__ == '__main__':
    print make_graph(20)