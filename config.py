# 数据库配置
HOSTNAME = '192.168.50.100'
PORT = '3306'
DATABASE = 'TEST-GUO'
USERNAME = 'root'
PASSWORD = ''
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)

# DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=uft8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI

# 邮箱配置
# juzoeuboaacybfjh
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '642011447@qq.com'
MAIL_PASSWORD = 'juzoeuboaacybfjh'
MAIL_DEFAULT_SENDER = '642011447@qq.com'
