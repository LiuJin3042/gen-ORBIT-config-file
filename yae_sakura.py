# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 17:20:47 2019

@author: LJ
"""

from __future__ import print_function
import time
import signal


def in_heart(x,y):
    # 使用心形曲线限制输出区域, 如果在心形曲线里, 就输出字符, 否则不输出
    return ((x*0.03)**2+(y*0.1)**2-1)**3-(x*0.03)**2*(y*0.1)**3 < 0


def love_u(word, print_size):
    # word是要输出的文字, print_size是2个元素的列表, 第一个元素代表横向长度, 第二个代表纵向长度
    word_len = len(word)
    x_range = [i for i in range(-print_size[0], print_size[0])]
    y_range = [i for i in range(print_size[1], -print_size[1], -1)]
    sleep_time = 0.000045  # 输出间隔时间
    # 先组成所有字, 然后逐字输出
    output_word = '\n'
    for y in y_range:
        one_line = ''
        for x in x_range:
            one_line = one_line + (word[(x-y) % word_len]if in_heart(x, y) else ' ')
        output_word = output_word + '\n' + one_line
    [(time.sleep(sleep_time), print(i, end='')) for i in output_word]


def signal_handler(signal, frame):
    return 0

def claim():
    signal.signal(signal.SIGINT, signal_handler) # 防止ctrl+c退出
    love_u('YAE SAKURA ', [45,12])
