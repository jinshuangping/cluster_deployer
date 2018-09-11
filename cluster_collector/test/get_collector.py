# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.


import os
import sys
import importlib


def scan_modules():
    dir_name = 'collector_plugin'
    sys.path.append('D:\Code\cluster_collector')
    print(sys.path)
    dirs = get_dirs()
    for t in dirs:
        print(t)
    name = importlib.import_module('collector_plugin')
    return name


def list_dirs(dirs):
    file_list = []
    for i in os.listdir(dirs):
        file_path = dirs + os.sep + i
        if os.path.isfile(file_path):
            file_list.append(file_path)
        elif os.path.isdir(file_path):
            file_list.append(list_dirs(file_path))
    return file_list


def find_module():
    name = importlib.import_module('test_p1')
    return name


def find_method(m):
    for i in dir(m):
        attr_type = type(eval('m.{}'.format(i)))
        if attr_type.__name__ == 'function':
            print(i)
            print(type(eval('m.{}'.format(i))))


#n = find_module()
#find_method(n)

scan_modules()
