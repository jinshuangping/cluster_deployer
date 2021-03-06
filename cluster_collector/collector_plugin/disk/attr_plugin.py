# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.


def collect_disk_size():
    info = [
        {
            '_name': 'num',
            '_label': {
                'zh_CN': '磁盘数量'
            },
            '_desc': {
                'zh_CN': '描述磁盘的数量'
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
