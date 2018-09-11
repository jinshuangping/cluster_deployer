# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.


from plugin.plugin import Plugin


class Controller(object):
    def __init__(self):
        pass

    def collect(self):
        plugin_ins = Plugin()
        plugin_list = plugin_ins.find_package()
