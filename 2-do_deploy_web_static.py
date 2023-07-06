#!/usr/bin/python3
"""Fabric script (based on the file 1-pack_web_static.py) that
distributes an archive to your web servers, using the
function do_deploy"""


from fabric.api import *
from datetime import datetime
from os.path import exists

env.hosts = ['54.162.90.117', '34.229.49.93']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_pack():
    """
    Generate a compressed archive of the web_static folder
    """
    try:
        now = datetime.now().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        file_path = "versions/web_static_{}.tgz".format(now)
        local("tar -cvzf {} web_static".format(file_path))
        return file_path
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if exists(archive_path) is False:
        return False
    try:
        archive_filename = archive_path.split("/")[-1]
        archive_folder = "/data/web_static/releases/{}".format(
                archive_filename.split(".")[0])
        put(archive_path, "/tmp/{}".format(archive_filename))
        run("mkdir -p {}".format(archive_folder))
        run("tar -xzf /tmp/{} -C {}".format(archive_filename, archive_folder))
        run("rm /tmp/{}".format(archive_filename))
        run("mv {}/web_static/* {}/".format(archive_folder, archive_folder))
        run("rm -rf {}/web_static".format(archive_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(archive_folder))
        return True
    except Exception:
        return False
