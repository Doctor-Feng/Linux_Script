import sys
import os

#generate README.md

os.system('bash readme.sh')

os.system('rm -rf readme.sh')

os.system('git init')

add_files_name = raw_input("Please select files of Enter : ")

if add_files_name == 'n':
    print "Upload is cancelled!"
    sys.exit()
elif add_files_name == '':

    os.system("git add -A")
else:
    add_files_command = "git add " +  add_files_name
    os.system(add_files_command)

COMMIT = raw_input ('Please Input the commit : ')
if COMMIT == 'n':
    print "Upload is cancelled!"
    sys.exit()
else:
    commit_command = "git commit -m " + "\"" +  str(COMMIT) + "\"" 

    os.system(commit_command)

REPOSITORY = raw_input('Please select the  repository :  ')
if REPOSITORY == 'n':
    print "Upload is cancelled!"
    sys.exit()
else:
    urls = 'https://github.com/Doctor-Feng/' + REPOSITORY + '.git'
    remote_command = "git remote add " +  COMMIT[0]  + " " +  urls
    os.system(remote_command)

    pull_command = "git pull -u " +  COMMIT[0]  + " master"
    os.system(pull_command)
    
    push_command = "git push -u " +  COMMIT[0]  + " master"
    os.system(push_command)
    print "Upload is finished successfully!"
