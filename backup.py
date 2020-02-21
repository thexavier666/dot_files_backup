#!/usr/bin/env python3

import sys
import os
import config
import subprocess as sp

from platform import node
from distutils.dir_util import copy_tree

# Argument 1 - Type of backup ("remote"/"local")

def main():

    # all static information
    # please check `config.py` for full documentation
    config_dir          = config.CONFIG_DIRECTORY()
    dot_file_list       = config.BACKUP_LIST()
    dot_file_backup_dir = config.BACKUP_DIRECTORY()
    user_name           = config.USERNAME()

    # getting device id
    dev_id              = node() 

    # whether backup will be local or on github
    backup_mode         = sys.argv[1]

    # directory of all local backups
    dev_backup_dir      = "{}/{}/".format(dot_file_backup_dir, dev_id)

    # creating the backup directory
    # this will host all the dot files for all machines
    if os.path.isdir(dot_file_backup_dir) is not True:
        os.mkdir(dot_file_backup_dir)

    # creating the device directory, 
    # which resides inside the backup directory
    # this will host all the dot files for a particular machine
    if os.path.isdir(dev_backup_dir) is not True:
        os.mkdir(dev_backup_dir)

    # creating a local copy of the dot files
    if backup_mode == 'local':

        with open(dot_file_list) as fp:
            for row in fp:

                # fetching the dot file directory
                app_dot_dir = "/home/{}/{}/{}".format(user_name, config_dir, row.strip())

                # checking if the app exists
                if os.path.isdir(app_dot_dir) is True:

                    # creating a backup directory for the current app
                    app_backup_dir = "{}/{}".format(dev_backup_dir,row.strip())

                    if os.path.isdir(app_backup_dir) is False:
                        os.mkdir(app_backup_dir)

                    # copying all the files of the current app
                    copy_tree(app_dot_dir, app_backup_dir)
                else:
                    print("[ERROR] Directory for APP {} does not exist!".format(row.strip()))

                print("[INFO] Backup complete for {}".format(row.strip()))

            print("[INFO] Backup complete for all apps of device {}".format(dev_id))

    # uploading local copy of the dot files to github
    elif backup_mode == 'remote':

        # if using for the first time
        if os.path.isdir(".git") is False:
            sp.call("git init", shell=True)
            sp.call("git config user.email {}".format(config.GIT_USEREMAIL()), shell=True)
            sp.call("git config user.name {}".format(config.GIT_USERNAME()), shell=True)
            sp.call("git add remote origin {}".format(config.GIT_REMOTE_URL()), shell=True)

        # pulling the latest branch
        sp.call("git pull origin master", shell=True)

        sp.call("git add . --force", shell=True)
        sp.call("git commit -m 'dot files pushed by user {} for machine {}'".format(user_name, dev_id), shell=True)
        sp.call("git push origin master", shell=True)
    else:
        print("[ERROR] Incorrect argument - remote or local backup?")
        return -1

if __name__ == '__main__':
    main()
