import json, string, random
from flask import Blueprint, request
from exts import mail
from flask_mail import Message
from email_validator import validate_email, EmailNotValidError

bp = Blueprint('auth', __name__, url_prefix='/auth')


@bp.route('/login')
def login():
    pass

@bp.route('/register')
def register():
    pass

@bp.route('/mail/test', methods=["POST"])
def mail_test():
    # args 一般用于get   data用于post 获取请求头:cookies
    # email = request.args.get('email')
    data = json.loads(request.data)
    data_email = data['email']

    is_check = check_email(data_email)
    print(is_check)
    if is_check == 'false':
        return {'code': 200, 'msg': '邮箱填写有误，请重新填写'}
    else:
        source = string.digits * 10
        captcha = random.sample(source, 4)
        captcha = "".join(captcha)
        message = Message(subject='验证码', recipients=[data_email], body=f"您的验证码是:{captcha}")
        mail.send(message)
        return {'code': 200, 'msg': '邮箱发送成功'}


# 检测email是否合规
def check_email(email):
    try:
        email = str(email)
        validate_email(email)
        return 'true'
    except EmailNotValidError:
        return 'false'
