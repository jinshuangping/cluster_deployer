import time
from datetime import datetime
from cluster_collector.core.collect_plugin.plugin import PluginController


class Executor(object):
    def __init__(self):
        pass

    def execute(self):
        controller = PluginController()
        methods = controller.find_plugin_method()

        for m in methods:
            result = self._exe(m)

    def _exe(self, func_name):
        time_start = time.time()
        result = eval(func_name)()
        time_end = time.time()
        time_collapsed = time_end - time_start

        result['_collect_time'] = datetime.now()
        result['_spend_time'] = time_collapsed
        result['_node_ip'] = '127.0.0.1'
        return result

    def _get_result(self):
        pass
