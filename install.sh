#!/bin/bash
echo "removing old zips"
rm -rf master.zip
rm -rf *.py source_file
echo "downloading"
wget https://github.com.cnpmjs.org/LiuJin3042/gen-ORBIT-config-file/archive/master.zip
echo "unzipping files"
unzip master.zip
echo "deploying"
mv -f ./gen-ORBIT-config-file-master/* .
echo "removing downloaded files"
rm -rf master.zip gen-ORBIT-config-file-master
echo "all done"
