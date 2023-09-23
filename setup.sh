# Either add "sudo" before all commands or use "sudo su" first
# Amazon Linux 2023

#!/bin/bash
sudo su
dnf install git -y
git clone https://github.com/jason6356/aws-live.git
cd aws-live
dnf install python-pip -y
pip3 install flask 
pip3 install pymysql 
pip3 install boto3 
pip3 install python-dotenv 
pip3 install Flask-Session
python3 app.py



