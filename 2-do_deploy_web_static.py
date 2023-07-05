#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the
function do_deploy"""


from fabric.api import *
from os.path import exists

env.hosts = ['54.162.90.117', '34.229.49.93']


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1].split(".")[0]
        put(archive_path, "/tmp/")

        run("mkdir -p /data/web_static/releases/{}".format(file_name))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
            file_name, file_name))
        run('rm -rf /tmp/{}.tgz'.format(file_name))

        run(('mv /data/web_static/releases/{}/web_static/* ' +
            '/data/web_static/releases/{}/').format(
                file_name, file_name))
        run('rm -rf /data/web_static/releases/{}/web_static'.format(file_name))
        run('rm -rf /data/web_static/current')
        run(('ln -s /data/web_static/releases/{}/' +
            '/data/web_static/current').format(file_name))
        return True
    except Exception:
        return False
