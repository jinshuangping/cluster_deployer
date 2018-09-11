# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.

import time

from huey.contrib.minimal import MiniHuey


hey = MiniHuey()


class Executor(object):
    def __init__(self):
        pass

    def func_wrap(self, method_name):
        exec('import test')
        return eval(method_name)

    def execute(self, method_list):
        result_list = []

        for method_name in method_list:
            result_list.append(hey.task()(self.func_wrap(method_name))())

        hey.start()

        print('start')
        for y in result_list:
            print(type(y))
            print(y.get())
