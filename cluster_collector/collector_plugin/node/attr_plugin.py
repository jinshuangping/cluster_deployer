# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.


def collect_node():
    info = [
        {
            '_name': 'hostname',
            '_label': {
                'zh_CN': '节点hostname'
            },
            '_desc': {
                'zh_CN': '描述节点的hostname'
            },
            '_collect_time': '',
            '_spend_time': '',
            '_node_ip': '',

            '_data': 3
        },
        {
            '_name': 'health',
            '_desc': {
                'zh_CN': '磁盘健康状态'
            },
            '_collect_time': '',
            '_data': {
                'sda': 'ok',
                'sdb': 'ok'
            }
        }
    ]
    return info
