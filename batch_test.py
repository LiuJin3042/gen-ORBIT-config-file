"""
Created on Fri Aug 16 08:04:15 2019

@author: LJ
"""

# ekev from 20 to 80
# amp from 1e-5 to 1e-4

from __future__ import division
from configuration import *
from make import main


def linspace(start, stop, count):
    # generate a arithmetic progression, from start to stop, total number is count
    step = (stop - start) / (count - 1)
    ap = []
    for i in range(count):
        ap.append(start + i * step)
    return ap


l_amp = [0]
l_polo = linspace(0.1,0.7,4)
l_ekev = linspace(20,100,5)

for i_ekev in l_ekev:
    for i_amp in l_amp:
        for i_polo in l_polo:
            amp = [i_amp]
            polo = i_polo
            ekev = i_ekev
            comment = 'D-amp=%e-polo=%f-ekev=%d'%(amp[0],polo,ekev)
            main(numeric, a, rmaj, rx, krip, q0, qed, qrx, mp0, 
                 modes, harm, nmod, mmod, omegv, alfv, amp, dele, a1, wdt, cnt, ptrb_file,
                 npert, polo, p1, p2, pchi, zprt, prot, ekev, bkg, ntor, nprt, nplot, pdist, perturb_subroutine,
                 submit)