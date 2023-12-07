#!/usr/bin/python3
# Fabfile to distribute an archive to a web server.
import os
from fabric.api import env, put, run

env.hosts = ['34.239.250.75', '100.25.17.31', '100.25.31.110']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'

def do_deploy(archive_path):
    """Distributes an archive to a web server."""
    if not os.path.exists(archive_path):
        return False

    base_name = os.path.basename(archive_path)
    name = base_name.split(".")[0]

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, "/tmp")

        run("mkdir -p /data/web_static/releases/{}/".format(name))
        
        # Uncompress the archive on the web server
        run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/"
            .format(base_name, name))

        # Delete the archive from the web server
        run("rm /tmp/{}".format(base_name))

        run("mv /data/web_static/releases/{}/web_static/* \
            /data/web_static/releases/{}/".format(name, name))

        run("rm -rf /data/web_static/releases/{}/web_static/".format(name))

        # Delete the symbolic link from the web server
        run("rm -rf /data/web_static/current")

        # Create a new symbolic link on the web server
        run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
            .format(name))

        print("New version deployed!")
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False

