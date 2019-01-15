#!/usr/bin/python3
"""
Use fabric to create tgz file of static code
"""
from fabric.api import local, task, env
from datetime import datetime


@task
def do_pack():
    """
    Run tar command to compress files
    """
    now = datetime.now()
    file_name = "web_static_{}{}{}{}{}{}.tgz".format(
            now.year,
            now.month,
            now.day,
            now.hour,
            now.minute,
            now.second
        )
    try:
        local("sudo tar -cvzf {} ./web_static".format(file_name))
        local("sudo mkdir -p versions")
        local("sudo mv ./{} versions/".format(file_name))
    except:
        return (None)
    return ("versions/{}".format(file_name))
