# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:40:57 2019

@author: LJ
"""

from __future__ import print_function
import sys
import time

if sys.version[0] == '2':
    from commands import getstatusoutput as gso
from configuration import *
import re


def monitor():
    # a program to monitor running status
    if sys.version[0] == '2':
        snap_time = 45
        status, output = gso('qstat')
        pattern = '(\d{7})\.service'
        jobid = re.findall(pattern, output)[-1]
        print('jobid is ', jobid, '\n')
        while re.findall(jobid, output):
            print(output)
            time.sleep(snap_time)
            status, output = gso('qstat')
            print('\n\n\n\n\n')
        print('job is done')


def pack(comment):
    # rename the desired file folder in form of 20010101-comment
    date = time.strftime('%Y%m%d', time.localtime(time.time()))
    # des_folder: destination of status, output files
    des_folder = date + '-' + comment
    # remove then creat the folder
    gso('rm -rf %s' % des_folder)
    gso('mkdir -p %s/orbit_results' % des_folder)
    gso('cp {orbit,orbit.F} ./%s' % des_folder)
    gso('cp {*.plt,orbit.out,configuration.py} ./%s/orbit_results' % (des_folder))
    gso('rm -rf q63887*')

if __name__ == '__main__':
    monitor()
    pack(comment)
