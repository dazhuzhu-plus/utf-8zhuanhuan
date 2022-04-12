#!/usr/bin/env python
#-*- coding:utf-8 -*-

# 作者        :lou
# 时间        :2022/4/11 下午2:16
# 文件        :utf-8.py
import os,sys

def run():
    # 获取运行地址目录
    dirss=os.getcwd()
    # 获取文件名
    dirs=sys.argv[1]
    # 转换文件名
    newdirs=bytes(dirs,encoding='ISO-8859-1').decode('gbk')
    # 合并地址
    newaddress=dirss+'/aiqich_clear/'+newdirs
    print(newaddress)
    # newfilename=dirss+dirs.replace(bytes(dirs,encoding='ISO-8859-1').decode('gbk'),"")
    print(dirss+'/aiqich_clear/'+dirs)
    os.rename(dirss+'/aiqich_clear/'+dirs,newaddress)
    # print(bytes(dirs,encoding='ISO-8859-1').decode('gbk'))
    print(dirs)


if __name__ == '__main__':
    dirr=os.walk('../aqctj/data')
    for root, dirs, files in dirr:
        # print('root'+root)
        #for d in dirs:
            #print(os.path.join(root, d))
        for f in files:
            #print(f)
            if os.path.isfile(os.path.join(root, f)):
                newfilename=os.path.join(root,f.encode('ISO-8859-1').decode('gbk'))
                os.rename(os.path.join(root, f), newfilename)
            print(os.path.join(root, f))

