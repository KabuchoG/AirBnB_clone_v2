#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
# import os.path
# from datetime import datetime
# from fabric.api import local


# def do_pack():
#     """Create a tar gzipped archive of the directory web_static."""
#     file = "versions/web_static_{}.tgz".format(
#         datetime.now().strftime("%Y%m%d%H%M%S"))
#     if os.path.isdir("versions") is False:
#         if local("mkdir -p versions").failed is True:
#             return None
#     if local("tar -cvzf {} web_static".format(file)).failed is True:
#         return None
#     return file

from datetime import datetime
import os
from fabric.api import local


def do_pack():
    """Create an archive"""
    zip_name = "web_static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    if not os.path.exists("versions"):
        local("mkdir -p versions")
    z_path = "versions/{}".format(zip_name)
    if local("tar -czvf {} web_static".format(z_path)).failed is False:
        return z_path
    else:
        return None
