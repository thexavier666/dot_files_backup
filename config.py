# location of the users active dot files
# default value is ".config/"
def CONFIG_DIRECTORY():
    return ".config/"

# the current user's username
# it can be replaced by system call
def USERNAME():
    return "xavier666"

# name of the file which contains 
# the dot files directory whose backup needs to be taken
def BACKUP_LIST():
    return "dot_list"

# directory which contains all backups for all machines
def BACKUP_DIRECTORY():
    return "dot_files"

def GIT_USERNAME():
    return "thexavier666"

def GIT_USEREMAIL():
    return "sumitros@gmail.com"

def GIT_REMOTE_URL():
    return "https://github.com/{}/dot_files_backup.git".format(GIT_USERNAME)
