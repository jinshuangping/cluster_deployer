import time
from huey.contrib.minimal import MiniHuey


hey = MiniHuey()


@hey.task()
def attr():
    info = {
        'desc': {
            'zh_CN': 'a'
        }
    }
    # register_info(info)
    print('in collect attr')
    yield 2000
    print('end attr')
    yield 'a'


@hey.task()
def attr2():
    print('in attr2')
    yield 2000
    print('end attr2')
    yield 'b'


re = attr()
re2 = attr2()
hey.start()
x = re.get()
y = re2.get()

print('1')
for a in x:
    print(a)
for b in y:
    print(b)
