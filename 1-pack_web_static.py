#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""


from fabric.api import local
from datetime import datetime as dt, timedelta
import os.path


def pack(folder):
    """Generates a .tgz archive from the contents of the web_static"""
    if not os.path.exists('versions'):
        os.makedirs('versions')
    now = dt.now()
    name = "web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day,
            now.hour, now.minute, now.second)
    local("tar -cvzf versions/{} {}".format(name, folder))
    return name
