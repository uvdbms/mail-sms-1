#coding:utf-8
from flask import Flask
from flask import jsonify
from flask import request
from sendmail import send_mail
from smsapi import sendsms
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)

status = [
    {
        'status': 200,
        'info': '发送成功'
    }
]
error = [
   {
        'status': 400,
        'info': '参数错误'
   }
]

@app.route('/sms/sender', methods=['GET', 'POST'])
def sms():
    if request.method == 'POST':
        s = request.form.get('tos')
        phones = s.split(',')
        content = request.form.get('content')
        sendsms(phones,content)
        return jsonify({'resp':status})
    elif request.method == 'GET':
        return jsonify({'resp':error})
    else:
        return 'no data'

@app.route('/mail/sender', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        s = request.form.get('tos')
        tos = s.split(',')
        content = request.form.get('content')
        subject = request.form.get('subject')
        send_mail(tos,subject,content)
        return jsonify({'resp':status})
    elif request.method == 'GET':
        return jsonify({'resp':error})
    else:
        return 'no data'


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5555,debug=True)
