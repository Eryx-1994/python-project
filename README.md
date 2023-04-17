# 结构
    app.py是入口文件
    config.py是数据库配置文件
    exts.py是扩展文件
    models.py是模块文件，比如数据库的表啊等等
    

# 命令
    数据库生成表的命令
    flask db init 
    flask db migrate
    flask db upgrade

# docker命令
    docker build -t flask:0.1
    docker run -it --rm -p 50056:50056 flask:0.1