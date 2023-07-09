#!/usr/bin/python3
""" The deploy function """

from fabric.api import *


env.hosts = ['54.162.90.117', '34.229.49.93']
env.user = 'ubuntu'


def do_clean(number=0):
    """Function that deletes out-of-date archives"""
    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
