# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:40:57 2019

@author: LJ
"""

import sys
import time

from subprocess import getstatusoutput as gso
if sys.version[0] == '2':
    from commands import getstatusoutput as gso
from configuration import *
import re


def monitor():
    # a program to monitor running status
    if sys.version[0] == '2':
        if nplot == 2:
            snap_time = 45
        if nplot in [1, 3]:
            snap_time = 3
        else:
            snap_time = 15
        status, output = gso('qstat')
        pattern = '(\d{7})\.service'
        jobid = re.findall(pattern, status, output)[-1]
        print('jobid is ', jobid)
        while re.findall(jobid, status, output):
            print(status, output)
            time.sleep(snap_time)
            status, output = gso('qstat')
            print('\n\n\n\n\n')
        print('job is done')


def pack(comment, pdist, numeric):
    # rename the desired file folder as 20010101-comment
    date = time.strftime('%Y%m%d', time.localtime(time.time()))
    # des_folder: destination of status, output files
    des_folder = date + '-' + comment
    # remove than creat the folder
    gso('rm -rf %s' % des_folder)
    gso('mkdir -p %s/orbit_results' % des_folder)
    # cp certain files based the value of pdist and numeric
    if pdist * numeric == 2:
        # numeric balance and distribution
        gso('cp {orbit,orbit.F,fbm_dist.dat,job.pbs} ./%s' % des_folder)
    elif pdist == 2:
        # numeric distribution
        gso('cp {orbit,orbit.F,fbm_dist.dat,job.pbs} ./%s' % des_folder)
    else:
        gso('cp {orbit,orbit.F,job.pbs} ./%s' % des_folder)
    # a program to package file 
    gso('cp {*.plt,orbit.out,configuration.py} ./%s/orbit_results' % (des_folder))
    gso('cp -r ./plot_functions ./%s' % (des_folder))


if __name__ == '__main__':
    monitor()
    pack(comment, pdist, numeric)
