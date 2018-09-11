# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.


import sys
import importlib


def find_module():
    name = importlib.import_module('test_p1')
    return name


def find_method(m):
    for i in dir(m):
        attr_type = type(eval('m.{}'.format(i)))
        if attr_type.__name__ == 'function':
            print(i)
            print(type(eval('m.{}'.format(i))))


n = find_module()
find_method(n)
