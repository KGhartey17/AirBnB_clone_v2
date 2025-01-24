#!/usr/bin/python3
"""
Fabric script to generate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Create an archive from the web_static folder.
    """

    time = datetime.now()
    archive = 'web_static_' + time.strftime("%Y%m%d%H%M%S") + '.tgz'
    local('mkdir -p versions')  # Create the versions directory if it doesn't exist
    create = local('tar -cvzf versions/{} web_static'.format(archive))  # Create the tarball

    if create.succeeded:  # Check if the command was successful
        return 'versions/' + archive
    else:
        return None

