#!/usr/bin/python3
"""
Use fabric to create tgz file of static code and deploy
to web servers
"""
from fabric.api import local, task, env, run, put
from datetime import datetime


env.hosts = ['34.73.123.2', '35.237.69.24']
env.user = 'ubuntu'


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


@task
def do_deploy(archive_path):
    """
    Deploy archive file to web servers
    """
    if not archive_path:
        return False
    file_name = archive_path.split('/')[1]
    try:
        put(archive_path, "/tmp")
        run("sudo mkdir -p /data/web_static/releases/{}".format(
                file_name.split('.')[0]
            ))
        run("sudo tar xzf /tmp/{} -C /data/web_static/releases/{}".format(
                file_name, file_name.split('.')[0]
            ))
        run("sudo rm /tmp/{}".format(file_name))
        run("sudo mv /data/web_static/releases/{0}/web_static/*"
            " /data/web_static/releases/{0}/".format(
                file_name.split('.')[0]
            ))
        run("sudo rm -rf /data/web_static/releases/{}/web_static".format(
                file_name.split('.')[0]
            ))
        run("sudo rm -rf /data/web_static/current/")
        run("sudo ln -s /data/web_static/releases/{}"
            " /data/web_static/current/".format(
                file_name.split('.')[0]
            ))
    except:
        return False
    return True


@task
def deploy():
    """
    Compress files and deploy to web servers
    """
    file_path = do_pack()
    if file_path:
        return False
    return (do_deploy(file_path))
