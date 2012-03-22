# -*- coding: utf-8 -*-

from setuptools import setup

setup (
    name = "pbl",
    version = "0.1",
    keywords = "pbl",
    url = "zhouxb.github.com",

    package_dir = {'': 'src',},
    packages = [
        'pbl',
        ],
    data_files = [('/etc/default', ['resources/etc/defalut/celeryd'])],
    include_package_data = True,
    install_requires = ["Celery == 2.5"],
    entry_points = {
        'console_scripts': [
            'pbl = pbl.main:main',
            ]
        },

)
