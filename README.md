#¿¿¿¿
yum install -y python-virtualenv

#¿¿¿¿¿¿
virtualenv ./env

#¿¿¿¿¿
./env/bin/pip install -r pip_requirements.txt

#¿¿¿¿
./control start

#¿¿¿¿
./control stop

#¿¿¿¿
./control tail

#¿¿¿¿
#¿¿¿¿
curl -d "tos=a@aaa.com,bbb@b.com&subject=test&content=test" http://127.0.0.1:5555/mail/sender
¿¿¿¿
curl -d "tos=1300000000,1700000000&content=test" http://127.0.0.1:5555/sms/sender

#¿¿
¿¿¿¿¿¿¿¿¿¿¿¿API¿¿¿post¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿¿
