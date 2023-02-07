#!/usr/bin/python3
""" Function that deploys """
from 1-pack_web_static import do_pack
from 2-do_deploy_web_static import do_deploy
from fabric.api import *


# env.hosts = ['35.231.33.237', '34.74.155.163']
# env.user = "ubuntu"


# def deploy():
#     """ DEPLOYS """
#     try:
#         archive_path = do_pack()
#     except:
#         return False

#     return do_deploy(archive_path)


# def do_pack():
#     try:
#         if not os.path.exists("versions"):
#             local('mkdir versions')
#         t = datetime.now()
#         f = "%Y%m%d%H%M%S"
#         archive_path = 'versions/web_static_{}.tgz'.format(t.strftime(f))
#         local('tar -cvzf {} web_static'.format(archive_path))
#         return archive_path
#     except:
#         return None


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

def deploy():
    """deploy"""
    env.hosts = ["54.160.120.73", "54.210.52.90"]
    env.user = 'ubuntu'
    new_gz = do_pack()
    if new_gz is False:
        return False
    dep_path = do_deploy(new_gz)
    return dep_path
