#!/usr/bin/python3
# Fabfile to generate a .tgz archive from contents of web_static folder
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """creates a tar gzipped archive of web_static directory"""
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
