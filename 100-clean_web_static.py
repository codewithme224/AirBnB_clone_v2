#!/usr/bin/python3
""" The deploy function """

import os
from datetime import datetime
import tarfile
from fabric.api import *


env.hosts = ['54.162.90.117', '34.229.49.93']
env.user = 'ubuntu'


def do_clean(number=0):
    """Function that deletes out-of-date archives"""
    number = int(number)

     if number < 2:
        number = 1
    number += 1
    number = str(number)
    with lcd("versions"):
        local("ls -1t | grep web_static_.*\.tgz | tail -n +" +
              number + " | xargs -I {} rm -- {}")
    with cd("/data/web_static/releases"):
        run("ls -1t | grep web_static_ | tail -n +" +
            number + " | xargs -I {} rm -rf -- {}")
