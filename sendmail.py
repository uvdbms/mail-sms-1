#!/bin/env python
#-*-coding:utf-8-*-

import string
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')
import smtplib
from email.mime.text import MIMEText
from email.message import Message
from email.header import Header


mail_host = '你的邮箱服务器'
mail_port = 25
mail_user = '你的邮件地址'
mail_pass = '你的密码'
mail_send_from = '你的展示的名称'


def send_mail(tos,subject,content):
    '''
    tos:发给谁
    subject:主题
    content:内容
    send_mail("aaa@126.com","sub","content")
    '''
    me=mail_send_from
    msg = MIMEText(content, _subtype='html', _charset='utf8')
    msg['Subject'] = Header(subject,'utf8')
    msg['From'] = Header(me,'utf8')
    msg['To'] = ','.join(tos) 
    try:
        smtp = smtplib.SMTP()
        smtp.connect(mail_host,mail_port)
        smtp.login(mail_user,mail_pass)
        smtp.sendmail(me, tos, msg.as_string())
        smtp.close()
        return True
    except Exception, e:
        print str(e)
        return False
