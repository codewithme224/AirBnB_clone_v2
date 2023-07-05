#!/usr/bin/python3
"""Fabric script that generates a .tgz archive"""


from fabric.api import local
from datetime import datetime as dt


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    time = dt.now()

    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    create = local('tar -cvzf versions/{} web_static'.format(archive))
    if create is not None:
        return archive
    else:
        return None
