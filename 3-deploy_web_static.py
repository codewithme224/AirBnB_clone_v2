#!/usr/bin/python3
"""Script that creates and distributes an archive to your web servers"""

import os.path
import time
from fabric.api import local
from fabric.operations import env, put, run

env.hosts = ['54.162.90.117', '34.229.49.93']


def do_pack():
    """Generates a .tgz archive from the contents of the web_static"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return ("versions/web_static_{}.tgz".format(time.
                                                    strftime("%Y%m%d%H%M%S")))
    except Exception:
        return None


def do_deploy(archive_path):
    """Distributes an archive to your web servers"""
    if (os.path.isfile(archive_path) is False):
        return False

    try:
        file_name = archive_path.split("/")[-1]
        new_folder = ("/data/web_static/releases/" + file_name.split(".")[0])
        put(archive_path, "/tmp/")
        run("sudo mkdir -p {}".format(new_folder))
        run("sudo tar -xyf /tmp/{} -C {}".format(file_name, new_folder))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv {}/web_static/* {}/".format(new_folder, new_folder))
        run("sudo rm -rf {}/web_static".format(new_folder))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(new_folder))
        print("Deployment done")
        return True
    except Exception:
        return False


def deploy():
    """Creates and distributes an archive to your web servers"""
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
