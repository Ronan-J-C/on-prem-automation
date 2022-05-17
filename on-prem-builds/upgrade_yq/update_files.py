import os
import subprocess
import shutil 
from shutil import copytree, Error

i=0
REPO_PATH="/Users/ronancunningham/repos/harness/harness-core"
FILE_OF_INTEREST='replace_configs.sh'
BACKUP_FILE='replace_configs.sh_bak'

def process_deletes(line):

    leading_spaces=len(line) - len(line.lstrip())
    chopped=line.split()
    conf_file=chopped[3]
    to_chop=chopped[4].strip("'")        
    updated_line="yq -i 'del(.{})' {}".format(to_chop, conf_file)
    return updated_line.rjust(len(updated_line)+leading_spaces)



def process_writes(line):

    # yq write -i $CONFIG_FILE logging.loggers.[$LOGGER] "${LOGGER_LEVEL}"
    # yq -i '.a.b[0].c = "cool"' file.yaml

    leading_spaces=len(line) - len(line.lstrip())
    chopped=line.split()

    conf_file=chopped[3]

    key=chopped[4]
    value=chopped[5]

    updated_line="yq -i '.{} = {}' {}".format(key,value,conf_file)
    return updated_line.rjust(len(updated_line)+leading_spaces)


def delete_files(files):

    for file in files:
        print(file)
        try:
            print('Deleting {}'.format(file))
            os.remove(file)
        except OSError as err:
            raise(err)



def backup_scripts():

    print('Backing up')
    i=0
    orig_files=[]
    for root, dirs, files in os.walk(REPO_PATH):
        for file in files:
            if(file == FILE_OF_INTEREST):
                bak_file="{}_bak".format(file)
                print('Backing up {}'.format(os.path.join(root,file)))
                orig_files.append(os.path.join(root,file))
                try:
                    shutil.copy(os.path.join(root,file), os.path.join(root,bak_file))
                except OSError as err:
                    raise(err)
    return orig_files

def update_files():

    print('Writing new file')
    i=0

    back_up_files=[]

    for root, dirs, files in os.walk(REPO_PATH):

        for file in files:

            new_file=[]

            if(file == BACKUP_FILE):

                # READ FILE

                back_up_files.append(os.path.join(root,BACKUP_FILE))

                orig_file=os.path.join(root,FILE_OF_INTEREST)
                print('Rewriting {}'.format(orig_file))

                text_file = open(os.path.join(root,file), "r")
                lines = text_file.readlines()


                for line in lines:

                    new_line=line

                    if ( 'yq delete -i' in line):
                        new_line=process_deletes(line)

                    if ( 'yq write -i' in line):
                        new_line=process_writes(line)  

                    # new_file.append(new_line.strip('\n'))
                    new_file.append(new_line.strip('\n'))
                try:
                    f = open(orig_file, "w+")
                    for line in new_file:
                        f.write(line +'\n')
                    f.close()
                except OSError as err:
                    raise(err)

    return back_up_files

orig_files=backup_scripts()
delete_files(orig_files)
backup_files=update_files()
delete_files(backup_files)