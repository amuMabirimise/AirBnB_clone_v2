#!/usr/bin/python3
<<<<<<< HEAD
# Fabric script that generates a .tgz archive
# Web_static folder of your AirBnB Clone repo
# Use the function do_pack
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create a tar gzipped of web_static."""
    dt = datetime.utcnow()
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    return file
=======
# Generates a .tgz archive from the contents of the web_static folder
import os
from fabric.api import local
from datetime import datetime as dt

now = dt.now()


def do_pack():
    """Packs web_static files into .tgz file"""

    file_name = 'versions/web_static_{}.tgz'\
                .format(now.strftime("%Y%m%d%H%M%S"))

    if not os.path.isdir("versions"):
        if local("mkdir -p versions").failed:
            return None

    command = local("tar -cvzf {} web_static".format(file_name))
    if command.succeeded:
        return file_name
    return None
>>>>>>> 6c965a7858f9faa6258d83f9676082c551788ccc
