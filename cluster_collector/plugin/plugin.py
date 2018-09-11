# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.


import pkgutil
import importlib


class CollectorPlugin(object):
    def __init__(self):
        pass


class CheckerPlugin(object):
    def __init__(self):
        pass


class Plugin(object):
    def __init__(self):
        pass

    def find_package(self):
        plugins = []
        for _, module_name, ispkg in pkgutil.iter_modules():
            if not ispkg or not module_name.endswith('_plugin'):
                continue
            try:
                plugins.append(module_name)
            except Exception:
                pass
        return plugins


def import_module():
        importlib.import_module('../test/test_import')


import_module()
