#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""


from fabric.api import *
from os import path
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    now = datetime.now().strftime("%Y%m%d%H%M%S")
    file_path = "versions/web_static_{}.tgz".format(now)
    local("mkdir -p versions")
    result = local("tar -cvzf {} web_static".format(file_path))
    if result.failed:
        return None
    return file_path
