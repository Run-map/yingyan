# 使用flask

部署参考：
Python Flask 在Sina App Engine (SAE)上安家 - 火狐设计的专栏 - 博客频道 - CSDN.NET
http://blog.csdn.net/firefox1/article/details/38228765

1. 根目录创建myApp.py
代码如下：
    from flask import Flask, render_template

    app = Flask(__name__)
    app.debug = True

    @app.route('/')
    def index():
        return render_template('index.html')

        
    if __name__ == '__main__':
            app.run()

            
2. 根目录新建templates文件夹，并将index.html放入其中
3. 运行myApp.py,浏览器中输入：http://127.0.0.1:5000/

OK


2015/12/14 14:58:42 部署至SAE

目录结构：

    rmap
    └─1
        ├─static
        │  ├─css
        │  │  └─fontawesome
        │  │      ├─css
        │  │      └─fonts
        │  ├─data
        │  ├─images
        │  └─js
        │      ├─esl
        │      └─track
        └─templates

1. 加载sae的dev_server.py文件至根目录
2. 在\\1目录下：`git init`
3. 复制dev_server.py文件至1目录
4. `git add`
5. `git commit -m "Runmap V1.0"`
6. `git push sae master:1`

本地测试：[http://127.0.0.1:8080/](http://127.0.0.1:8080/)



