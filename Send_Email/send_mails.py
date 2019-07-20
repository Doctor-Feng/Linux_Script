def mailqq(pathnow):
    import sys
    import file_send
    Receive=raw_input('Please input Receive address: ')
    if Receive == 'n':
        print "Send e-mail is cancelled!"
        sys.exit()
    SUBJECT = raw_input ('The Subject of email is: ')
    if SUBJECT == 'n':
        print "Send e-mail is cancelled!"
        sys.exit()
    BODY = raw_input('What do you want to say: ')
    if BODY == 'n':
        print "Send e-mail is cancelled!"
        sys.exit()
    files = raw_input('Is there any files? name/n: ')
    files = pathnow + files
    if files == 'n':
        nonfile(Receive,SUBJECT,BODY)
    else:
        file_send.withfile(Receive,SUBJECT,BODY,files)
