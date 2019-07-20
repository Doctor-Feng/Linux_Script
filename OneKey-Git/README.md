# OneKey-Git

Install 
=======
```python
First, you should install git

Debian: sudo apt-get install git
Fedora: sudo yum install git

Then run the following commands: 

git clone https://github.com/Doctor-Feng/OneKey-Git.git

cp gitt git_upload.py readme.sh /usr/bin
```
Setting
========
vim git_upload.py
------------
```python
import sys
import os
#generate README.md

os.system('bash readme.sh')

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

    push_command = "git push -u " +  COMMIT[0]  +" master"
    os.popen(push_command)
    print "Upload is finished successfully!"
```
注意，需要把git_upload.py里面的Doctor-Feng改成自己的github账户名。

Usage
=======
```python
gitt
```
