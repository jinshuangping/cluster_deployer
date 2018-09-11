#from executor import Executor

#ex = Executor()
#ex.execute(['test.attr', 'test.attr2'])

from test import hey  # import our "huey" object
from test import attr  # import our task


if __name__ == '__main__':
    attr()
