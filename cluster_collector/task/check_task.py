from cluster_collector.task.task import Task


class CheckTask(Task):
    def __init__(self, node_list):
        super(CheckTask).__init__(node_list)

    def start(self):
        pass

    def stop(self):
        pass

    def get_status(self):
        pass
