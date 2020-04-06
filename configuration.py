# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 17:55:23 2019

Read the configuration file, read the file to be changed, and write the new file

@author: LJ
"""

"""
修改平衡文件eqs.f
"""

# numeric: 平衡的类型,numeric = 1, 数值平衡
# numeric = 0, 解析平衡, 需要提供设备参数, 包括rmaj和a
numeric = 1
# rmaj, 大径, 半径, 单位: cm
rmaj = 185
# a, 小径, 直径, 单位: cm
a = 45
# 安全因子, q = q0 + qr2*r^2 + qr3*r^3, r是归一化的r
# r在源代码中是以rmaj归一, 但是为了便于设置, 这里还是采用以a归一
# q0: r = 0时的q值
# qed: r = 1时的q值
# qrx: r = rx时的q值为qrx. 需要设置qrx.
# 通过以上三组值解出qr2, qr3.
q0 = 1.3
qed = 4.9
rx = 0.5
qrx = 2

# mp0: 数值平衡的文件, 默认是map01.cdf
mp0 = 'map01.cdf'

# 波纹种类,krip
# krip = 0-无波纹; krip = 1-TFTR
# krip = 2-Tore Supra; krip = 3-ITER
# krip = 4-NSTX; krip = 5-Ignitor
# krip = 6-EAST
krip = 0

"""
修改扰动文件perturb.f
"""
# modes: 模数, 如果有8个模, 设置modes = 8
# 以下变量要将值写在数组[]里, 元素的个数务必等于modes
# wnt: 高斯扰动的方差
# cnt: 高斯扰动的平均值
# mmod: m值, 对应每个模的m
# nmod: n值, 对应每个模的n
# amp: 模幅度
# omegv: 频率, 单位为千赫兹
# dele: 能量改变的步长, 只有在omegv不为0的时候才要设置
modes = 9
dele = 10
wdt = [0.3]
cnt = [0.4]
harm = [1]
mmod = [2,2,2,2,13,1,3,9,7]
nmod = [1,2,4,1,2,3,7,1,9]
amp = [5e-5,6e-5,6e-5,6e-5,6e-5,6e-5,6e-5,6e-5,6e-5]
omegv = [3,4,5,6,7,8,9,1,2]
alfv = [1,1,1,1,1,1,1,1,1]

# 解析扰动的表达式, 只有解析扰动才需要设置
# a1 = 1-gaussian, a1 = 2-gaussian MHD
# a1 = 3-MHD, a1 = 4-resistive
a1 = 4

# npert: 扰动模式
# npert = 0-无扰动
# npert = 1-有磁扰动
# npert = 2-有势扰动
# npert = 3-两者都有
# npert = 4-调用readptrbx或readptrba读取扰动
npert = 4

# perturb_subroutine: 调用哪个函数读取扰动
# 仅当npert = 4时需要使用
# perturb_subroutine = 0-调用readptrba
# perturb_subroutine = 1-调用readptrbx
perturb_subroutine = 1

# ptrb_file: 数值扰动的文件
# 仅当npert = 4时需要使用
ptrb_file = 'filea.txt'

# nplot: 运行模式
# nplot = 1-单粒子
# nplot = 2-多粒子
# nplot = 3-庞加莱图
# nplot = 4-均匀分布
nplot = 2

# pdist, 粒子分布模式
# pdist = 1-shelldep
# pdist = 2-sampledep, 从fbm_dist.dat里读取分布
# pdist = 3-poindep, 庞加莱分布
# pdist = 4-poinkdep
# pdist = 5-fulldepe, 画相位图
pdist = 1

# nprt: 粒子数
nprt = 10000

# ntor: 程序运行时间, 粒子绕环ntor周, 程序停止
ntor = 3000

# bkg: 磁场强度, 千高斯
bkg = 24.2

# polo, shelldep粒子起始分布磁面
# p1, p2, poindep粒子分布的起始结束磁面
# pchi, 粒子起始俯仰角
polo = 0.8
p1 = 0.01
p2 = 0.99
pchi = 0.7

# zprt, 粒子带电荷数, 单位为1个单位电荷
# prot, 粒子质量, 单位为单个质子质量
# ekev, 粒子能量, 单位为千电子伏
zprt = 1
prot = 2
ekev = 10

# submit: 编译完成后是否提交运行
# submit = 1-提交
# submit = 0-不提交
submit = 1

# comment: 对本文件的目的说明, 可以随意修改, 会被用作新生成的文件夹名称
comment = 'east-shelldep-test'






