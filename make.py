# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:55:23 2019

Read the configuration file, read the file to be changed, and write the new file

@author: LJ
"""

from __future__ import division
from configuration import *
import modify
import sys
import time
import sub
import gen_fbm


# import gen_fbm


def main(numeric, a, rmaj, rx, krip, q0, qed, qrx, mp0, 
         modes, harm, nmod, mmod, omegv, alfv, amp, dele, a1, wdt, cnt, ptrb_file,
         npert, polo, p1, p2, pchi, zprt, prot, ekev, bkg, ntor, nprt, nplot, pdist, perturb_subroutine,
         comment, submit):
    """
    read and rewrite eqs.f
    output file should be in the same dir
    """
    modify.mod_eqs(numeric, a, rmaj, rx, krip, q0, qed, qrx, mp0)

    """
    read and rewrite perturb.f
    output file should be in the same dir
    """
    modify.mod_perturb(npert, modes, harm, nmod, mmod, omegv, alfv, amp, dele, a1, wdt, cnt, ptrb_file)

    """
    read and rewrite orbit.F
    output file should be in the same dir
    """
    modify.mod_orbit(npert, polo, p1, p2, pchi, zprt, prot, ekev, bkg, ntor, nprt, nplot, pdist, krip, perturb_subroutine)

    """
    create fbm_dist.plt
    """
#    if pdist == 2:
#        gen_fbm.gen_fbm(nprt, rmaj, a, ekev)

    """
    make and submit files
    """

    if sys.version[0] == '2':
        sub.sub_task(comment, submit)


if __name__ == '__main__':
    main(numeric, a, rmaj, rx, krip, q0, qed, qrx, mp0, 
         modes, harm, nmod, mmod, omegv, alfv, amp, dele, a1, wdt, cnt, ptrb_file,
         npert, polo, p1, p2, pchi, zprt, prot, ekev, bkg, ntor, nprt, nplot, pdist, perturb_subroutine,
         comment, submit)