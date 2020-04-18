#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib import request
import zipfile
import os

version = '1.1.19.2_20190627';
filename = 'XTP_API_{}.zip'.format(version)
url = 'https://xtp.zts.com.cn/dl/{}'.format(filename)
print ("downloading xtp from {}".format(url))

request.urlretrieve(url, filename)

def un_zip(file_name):  
    """unzip zip file"""  
    zip_file = zipfile.ZipFile(file_name)
    dirname = "xtpapi"
    
    if os.path.isdir(dirname):  
        pass  
    else:  
        os.mkdir(dirname)
    
    for names in zip_file.namelist():  
        # zip_file.extract(names)  #加入到某个文件夹中 
        zip_file.extract(names, dirname)
    zip_file.close()

un_zip(filename)