# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:50:00 2019

@author: LJ
"""

from __future__ import division

def mod_eqs(numeric, a, rmaj, rx, krip, q0, qed, qrx, mp0):
    # modify eqs.f, new file will be output to main dir.
    # read files - rewrite certain lines - write to new files
    r_eqs = open('./source_file/eqs.f', 'r')
    w_eqs = open('./eqs.f', 'w')
    eqs = r_eqs.readlines()
    eqs[19] = '      numeric = ' + str(numeric) + '\n'
    eps = a / rmaj
    # convert rx from a normalized to rmaj normalized
    rx = rx * a / rmaj
    eqs[24] = "            mp0 = '" + mp0 + "'\n"
    eqs[50] = '        rmaj = ' + str(rmaj) + '\n'
    eqs[106] = '      eps = ' + str(a) + '.D0/rmaj\n'
    eqs[61] = '      krip = ' + str(krip) + '\n'
    eqs[109] = '      q0 = ' + str(q0) + '\n'
    eqs[110] = '      qed = ' + str(qed) + '\n'
    eqs[111] = '      rqx = ' + str(rx) + '\n'
    eqs[113] = '      qx = ' + str(float(qrx)) + '\n'
    det_qr = (eps ** 2 * rx ** 3 - eps ** 3 * rx ** 2)
    det_qr2 = (qed - q0) * rx ** 3 - eps ** 3 * (qrx - q0)
    det_qr3 = eps ** 2 * (qrx - q0) - rx ** 2 * (qed - q0)
    qr3 = det_qr3 / det_qr
    qr2 = det_qr2 / det_qr
    eqs[126] = '      qr2 = ' + str(qr2)[0:9] + '\n'
    eqs[127] = '      qr3 = ' + str(qr3)[0:9] + '\n'
    w_eqs.writelines(eqs)
    r_eqs.close()
    w_eqs.close()


def mod_perturb(npert, modes, harm, nmod, mmod, omegv, alfv, amp, dele, a1, wdt, cnt, ptrb_file):
    r_ptrb = open('./source_file/perturb.f', 'r')
    w_ptrb = open('./perturb.f', 'w')
    ptrb = r_ptrb.readlines()
    ptrb[17] = '      modes = ' + str(modes) + '\n      md1 = 1  \n      md2 = modes \n'

    # set mode params, e.g.
    #      harm(1) = 1
    #      mmod(1) = 2
    #      nmod(1) = 1
    #      amp(1) = 5.0D-4
    #      omegv(1) = 0.0*2.D3*pi/omeg0
    #      alfv(1) = 1
    if npert == 1: 
        mode_params = ''
        for i in range(modes):
            j = i + 1
            one_param = '''
             harm(%d) = %d
             mmod(%d) = %d
             nmod(%d) = %d
             amp(%d) = %.3e
             omegv(%d) = %.3f*2.0D3*pi/omeg0
             alfv(%d) = %d
             wdt(%d) = %.3f
             cnt(%d) = %.3f
             '''%(j,harm[i],j,mmod[i],j,nmod[i],j,amp[i],j,omegv[i],j,alfv[i],j,wdt[i],j,cnt[i])
            mode_params += one_param
        ptrb[18] = mode_params
    ptrb[19] = '      dele = ' + str(dele) + '\n'
    
    # set a1-alpha
    # a1(j,md) = exp(-((xd-cnt(md))/wdt(md))**2)   ! gaussian
    # a1(j,md) = a1(j,md)*(rm/rn - qdum)    !  gaussian MHD
    # a1(j,md) = (eps*xd)**m*(1-n*qdum/m)/(gdum*qdum)    ! MHD
    # a1(j,md) = (eps*xd)**m*(pw - px)    ! resistive
    mode_type = ['exp(-((xd-cnt(md))/wdt(md))**2)',
                 'a1(j,md)*(rm/rn-qdum)',
                 '(eps*xd)**m*(1-n*qdum/m)/(gdum*qdum)',
                 '(eps*xd)**m*(pw-px)']
    if a1 == 2:
        ptrb[51] = '         a1(j,md) = ' + mode_type[0] + '\n         a1(j,md) = ' + \
                   mode_type[1] + '\n'
    else:
        ptrb[51] = '         a1(j,md) = ' + mode_type[a1 - 1] + '\n'
    ptrb[373] ="       plabel = '" + ptrb_file + "'\n"
    
    if npert == 4:
        mode_params = ''
        for i in range(modes):
            j = i + 1
            one_param = '''
             alfv(%d) = %d
             amp(%d) = %.3e
             omegv(%d) = %.3f*2.0D3*pi/omeg0
             nmod(%d) = %d
             mmod(%d) = %d
             '''%(j,alfv[i],j,amp[i],j,omegv[i],j,nmod[i],j,mmod[i])
            mode_params += one_param
        ptrb[387] = mode_params + '\n'
    ptrb[432] ="       plabel = '" + ptrb_file + "'\n"
    w_ptrb.writelines(ptrb)
    r_ptrb.close()
    w_ptrb.close()


def mod_orbit(npert, polo, p1, p2, pchi, zprt, prot, ekev, bkg, ntor, nprt, nplot, pdist, krip, perturb_subroutine):
    r_orbit = open('./source_file/orbit.F', 'r')
    w_orbit = open('./orbit.F', 'w')
    orbit = r_orbit.readlines()
    orbit[117] = '        npert = ' + str(npert) + '\n'
    orbit[126] = '        polo = ' + str(polo) + '*pw\n'
    orbit[127] = '        p1 = ' + str(p1) + '*pw\n'
    orbit[128] = '        p2 = ' + str(p2) + '*pw\n'
    orbit[129] = '        pchi = ' + str(pchi) + '\n'
    orbit[133] = '      zprt = ' + str(zprt) + '.D0\n'
    orbit[134] = '      prot = ' + str(prot) + '.D0\n'
    orbit[135] = '      ekev = ' + str(ekev) + '\n'
    orbit[112] = '      krip = ' + str(krip) + '\n'
    orbit[108] = '      bkg = ' + str(bkg) + '\n'
    orbit[94] = '        ntor = ' + str(ntor) + '\n'
    orbit[79] = '        nprt = ' + str(nprt) + '\n'
    orbit[75] = '      nplot = ' + str(nplot) + '\n'
    ndist = ['shelldep', 'sampledep', 'poindep', 'poinkdep', 'fulldepe']
    orbit[242] = '        call ' + ndist[pdist - 1] + '\n'
    perturb_f = ['readptrba','readptrbx']
    if npert == 4:
        orbit[181] = '      call ' + perturb_f[perturb_subroutine] + '\n'
    w_orbit.writelines(orbit)
    r_orbit.close()
    w_orbit.close()
