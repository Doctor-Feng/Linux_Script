#!/bin/sh
basepath = $(cd 'dirname $0'; pwd)
npath = $(cd 'pwd'; pwd)
cd $basepath
python -c "import send_mails; send_mails.mailqq('$npath/') "
