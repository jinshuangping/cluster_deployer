# -*- coding: utf-8 -*-
# Copyright (c) 2013-2018, SMARTX
# All rights reserved.


from celery import Celery

app = Celery('task', broker='')


@app.task
def add(x, y):
    return x + y
