#!/usr/bin/python3
# Fabfile to delete out-of-date archives.
import os
from fabric.api import env, local, run

env.hosts = ['34.239.250.75', '100.25.17.31']
env.user = 'ubuntu'


def do_clean(number=0):
    """ CLEANS """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local('cd versions ; ls -t | tail -n +{} | xargs rm -rf'.format(number))
    path = '/data/web_static/releases'
    run('cd {} ; ls -t | tail -n +{} | xargs rm -rf'.format(path, number))
