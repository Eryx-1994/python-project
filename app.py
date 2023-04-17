# from flask import Flask


import config
import flask
from exts import db, mail
from models import UserModel
from flask_migrate import Migrate
# 接口
from views.auth import bp as auth_bp
from views.qa import bp as qa_bp

app = flask.Flask(__name__)

app.config.from_object(config)  # 引入配置文件

db.init_app(app)
mail.init_app(app)
# blur print(蓝图的意思，顾名思义做模块化用的)
app.register_blueprint(auth_bp)
app.register_blueprint(qa_bp)

migrate = Migrate(app, db)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=50056)
