#!/usr/bin/python3
# Fabfile to generates a .tgz archive from the contents of web_static.
# """import os.path
# from datetime import datetime
# from fabric.api import local


# def do_pack():
#     """Create a tar gzipped archive of the directory web_static."""
#     dt = datetime.utcnow()
#     file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
#                                                          dt.month,
#                                                          dt.day,
#                                                          dt.hour,
#                                                          dt.minute,
#                                                          dt.second)
#     if os.path.isdir("versions") is False:
#         if local("mkdir -p versions").failed is True:
#             return None
#     if local("tar -cvzf {} web_static".format(file)).failed is True:
#         return None
#     return file
# """


from datetime import datetime
import os
from fabric.api import local


def do_pack():
    zip_name = "web-static_{}.tgz".format(
        datetime.now().strftime("%Y%m%d%H%M%S"))
    if not os.path.exists("versions"):
        local("mkdir versions")
    if local("tar -czvf versions/{} web_static".format(zip_name)).failed is False:
        return zip_name
    else:
        return None
