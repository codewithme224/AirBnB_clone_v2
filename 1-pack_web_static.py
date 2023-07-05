#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""


from fabric.api import *
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    local("sudo mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    file_name = "versions/web_static_{}.tgz".format(date)
    results = local("sudo tar -cvzf {} web_static".format(file_name))
    if results.succeeded:
        return file_name
    else:
        return None
