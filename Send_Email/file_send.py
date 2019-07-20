def withfile(Receive,SUBJECT,BODY,Filename):
    import smtplib
    import time
    import string
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart
    #***************************************************************
    HOST = "smtp.qq.com"
    FROM = "1186571527@qq.com"
    TO = Receive
    msg = MIMEMultipart('related')
    #get time
    dtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    msgtext = MIMEText("""
                       <table width ="800" border ="0" cellspacing ="0" cellspacing = "4" >
                       <tr>
                            <td bgcolor="#CECFAD" height = "20" style = "font-size:14px">
                            Today is """ + dtime + """. This e-mail is from Feng Donghai. Hope you have a good time !
                            </td>
                       </tr>
                       <tr>
                            <td bgcolor="EFEBDE" height = "100" style = "font-size :13px">
                        """+BODY+"""
                            </td>
                       </tr>
                       </table>""","html","utf-8")
    msg.attach(msgtext)
    attach = MIMEText(open(Filename ,"rb").read(),"base64","utf-8")
    attach["Content-Type"]="application/octet-stream"
    attach["Content-Disposition"]="attachment;filename=\"" + Filename +"" #.decode("utf-8").encode("gb18030")
    msg.attach(attach)
    msg['Subject']=SUBJECT
    msg['From']=FROM
    msg['To']=TO
    try:
        server = smtplib.SMTP()
        server.connect(HOST,"25")
        server.starttls()
        server.login("1186571527","vdxieqalruhsibie")
        server.sendmail(FROM,[TO],msg.as_string())
        server.quit()
        print "Send E-mail sucessfully!"
    except Exception,e:
        print "Failure:",str(e)
