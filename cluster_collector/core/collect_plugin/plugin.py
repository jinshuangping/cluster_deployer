import os
import importlib


class PluginController(object):
    def __init__(self):
        self.module = 'collector_plugin'
        self.plugins = []

    def _load_plugin(self, module_dir, parent):
        plugin_list = []
        for i in dir(module_dir):
            file_path = module_dir + os.sep + i
            if os.path.isdir(file_path):
                plugin_list.append(self._load_plugin(file_path, parent + '.' + i))
            else:
                importlib.import_module(parent + '.' + i)

        return plugin_list

    def load_plugin(self):
        module_import = importlib.import_module(self.module)
        module_dir = module_import.__file__.rstrip('/__init__.py')
        self.plugins = self._load_plugin(module_dir, self.module)

    def call_plugin_method(self):
        pass
