# 生成ORBIT配置文件

[更新日志](./updatelog.md)

## 项目说明

本项目主要用于自动编辑生成ORBIT导心运动代码的关键文件. ORBIT代码参数众多, 分布凌乱, 难以正确全部设置, 因此本项目将所有参数集成到`configuration.py`文件中. 用户只要调整该文件内部的参数, 然后通过python脚本提交运行, 大大减小了因为参数设错而出错的可能. 

## 脚本功能介绍

* `configuration.py`: ORBIT代码中主要的参数, 用户设置的主要文件.
* `make.py`: 程序运行的主文件, 用户编辑完配置文件后直接运行该文件, 该文件会编译ORBIT代码并调用`sub.py`提交服务器运行. 
* `modify.py`: 根据`configuration.py`中的参数, 编辑`./source_file`中的各个文件, 然后将编辑后的文件放到`./`目录下. 
* `sub.py`: 负责提交任务给服务器. 
* `use.py`: 内含有两个函数, 一个用来隔一段时间请求服务器查看已提交的任务运行情况, 另一个用来将运行结果放到名为`今日日期-[comment]`的文件夹里. 当运行use.py时, 两个程序先后被调用. 
* `gen_fbm.py`: 生成`fbm_dist.dat`, 需要手动配置密度函数.
* `batch_test.py`: 扫描参数使用, 批量进行参数代入然后提交服务器运行. 需要用户写循环. 
* `source_file`: 文件夹, 里面有需要被修改的ORBIT代码. 这个文件夹不需要修改.
* `yae_sakura.py`: 一张我爱人的字符照片. 没有什么用. 

## 安装和更新

安装程序已经集成在`install.sh`中, 当然也可以手动将脚本(所有的py文件和source_file文件夹)放到ORBIT代码同一个目录下.

1. 在ORBIT文件夹中, 输入命令, 下载`install.sh`

   ```
   wget https://raw.githubusercontent.com/LiuJin3042/gen-ORBIT-config-file/master/install.sh
   ```

2. 修改权限

   ```
   chmod 755 install.sh
   ```

3. 执行安装

   ```
   ./install.sh
   ```

4. 这个脚本也可以用来一键更新, 与远程保持同步

## 如何使用

有两种使用方式

1. 提交一次运行

   根据自己需要的参数编辑`configuration.py`

   ```
   $ vi configuration.py
   ```

   提交服务器并运行

   ```
   $ python make.py // 或者
   $ nohup python make.py &
   ```

2. 扫描参数, 批量运行

   需要修改batch_test.py, 对要扫描的参数写一个循环

   ```
   $ vi batch_test.py
   ```

   然后用python运行, 运行时间一般较长, 选择后台运行

   ```
   $ nohup python batch_test.py &
   ```

   查看任务

   ```
   $ jobs
   ```

   程序会自动识别任务号, 并且在小任务完成后自动开启下一个小任务. 因此你可以**在不同的文件夹中**同时运行`batch_test.py`

3. 如果并没有通过此方法就提交了服务器, 想要监视服务器运算情况, 使用`use.py`

   ```
   $ python use.py
   ```

   它会每隔一定的时间向服务器询问运行情况并打印在屏幕上

4. 运行结果会放到一个名为'日期-备注'的文件夹里, 格式为`20190901-[comment]`