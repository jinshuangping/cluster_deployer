import os
import cluster_collector
import importlib


class PluginController(object):
    def __init__(self):
        self.module = 'cluster_collector.collector_plugin'
        self.plugins = []
        self.load_plugin()

    def _load_plugin(self, module_dir, parent):
        plugin_list = []
        for i in os.listdir(module_dir):
            file_path = module_dir + os.sep + i
            if os.path.isdir(file_path):
                plugin_list.extend(self._load_plugin(file_path, parent + '.' + i))
            else:
                if i.endswith('plugin.py'):
                    importlib.import_module(parent + '.' + i[:-3])
                    plugin_list.append(parent + '.' + i[:-3])

        return plugin_list

    def load_plugin(self):
        module_import = importlib.import_module(self.module)
        dir_pos = module_import.__file__.find('/__init__.py')
        module_dir = module_import.__file__[:dir_pos]
        self.plugins = self._load_plugin(module_dir, self.module)

    def find_plugin_method(self):
        methods = []
        for m_str in self.plugins:
            m = importlib.import_module(m_str)
            for i in dir(m):
                attr_type = type(eval('m.{}'.format(i)))
                if attr_type.__name__ == 'function' and i.startswith('collect'):
                    methods.append(m_str + '.' + i)
        return methods
