# !/usr/bin/python3
""" Function that compress a folder """
# from datetime import datetime
# from fabric.api import *
# import shlex
# import os


# env.hosts = ['44.211.97.124', '34.228.52.136']
# env.user = "ubuntu"


# def do_deploy(archive_path):
#     """ Deploys """
#     if not os.path.exists(archive_path):
#         return False
#     try:
#         name = archive_path.replace('/', ' ')
#         name = shlex.split(name)
#         name = name[-1]

#         wname = name.replace('.', ' ')
#         wname = shlex.split(wname)
#         wname = wname[0]

#         releases_path = "/data/web_static/releases/{}/".format(wname)
#         tmp_path = "/tmp/{}".format(name)

#         put(archive_path, "/tmp/")
#         run("mkdir -p {}".format(releases_path))
#         run("tar -xzf {} -C {}".format(tmp_path, releases_path))
#         run("rm {}".format(tmp_path))
#         run("mv {}web_static/* {}".format(releases_path, releases_path))
#         run("rm -rf {}web_static".format(releases_path))
#         run("rm -rf /data/web_static/current")
#         run("ln -s {} /data/web_static/current".format(releases_path))
#         print("New version deployed!")
#         return True
#     except:
#         return False


def do_deploy(archive_path):
    """Distributes an archive to different servers"""
    from fabric.api import env, put, run
    import os

    env.hosts = ["54.160.120.73", "54.210.52.90"]
    env.user = "ubuntu"
    env.key_filename = "~/.ssh/id_rsa)"

    if not os.path.exists(archive_path):
        return False
    release_path = archive_path.replace('/', ' ')
    re_list = release_path.split(" ")
    rel_path = re_list[-1]
    r_path = rel_path.split(".")
    g_name = r_path[0]
    f_path = "/data/web_static/releases/{}".format(g_name)
    
    try:
        put("archive_path", "/tmp/")
        run("tar -xzvf /tmp/{} -C {}".format(rel_path, f_path))
        run("rm /tmp/{}".format())
        run("rm -rf /data/web_static/current")
        run("ln -sf {} /data/web_static/current".format(f_path))
        return True

    except Exception:
        print("Error Executing the file")
        return False
