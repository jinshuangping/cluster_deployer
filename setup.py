import os
from setuptools import (
    setup,
    find_packages,
)

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

setup(name='cluster_deployer',
      version='1.0.0',
      description='python command line and a Restful web server',
      author='shuangping',
      url='shuangping.com',
      classifiers=[
          'Environment :: Shuangping',
          'Intended Audience :: Information Technology',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
      ],
      license="Test License",
      packages=find_packages(
          PROJECT_ROOT
      ),
      include_package_data=True
      )
