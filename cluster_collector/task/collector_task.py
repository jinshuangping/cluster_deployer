from cluster_collector.task.task import Task
from cluster_collector.executor.executor import Executor


class CollectorTask(Task):
    def __init__(self, node_list):
        super(CollectorTask).__init__(node_list)
        self.executor = None

    def start(self):
        self.executor = Executor('collect.yaml')

    def stop(self):
        pass

    def get_status(self):
        pass
