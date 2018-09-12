# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.


from subprocess import Popen, PIPE


class AnsibleExecutor(object):
    def __init__(self, ansible_playbook):
        self.playbook = ansible_playbook
        self.process = None

    def start(self):
        cmd = "cd {0}; ansible-playbook  -i {1} {2} --extra-vars '{3}'".format(
            os.path.dirname(INVENTORY_FILE), self.inventory, self.playbook,
            args_str
        )
        self.process = Popen(cmd, stdout=PIPE, stderr=PIPE, bufsize=1,
                             shell=True)

    def get_status(self):
        pass
