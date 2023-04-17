FROM python:3.9.6

WORKDIR /app
ADD . /app

RUN pip3 install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

CMD ["python", "app.py" ]
