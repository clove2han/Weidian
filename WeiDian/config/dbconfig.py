import os
database = os.environ.get('DB_NAME', "weidian")
host = os.environ.get('DB_HOST', "127.0.0.1")
port = "3306"
username = os.environ.get('DB_USER', 'root')
password = os.environ.get('DB_PWD', '')
charset = "utf8"
sqlenginename = 'mysql+pymysql'
