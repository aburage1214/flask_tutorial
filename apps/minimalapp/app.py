# Flaskクラスをimportする
from flask import Flask, render_template, url_for, current_app, g, request

# Flaskクラスをインスタンス化
app = Flask(__name__)

# URLと実行する関数をマッピングする
@app.route("/")
def index():
    return "Hello, Flaskbook--!"

@app.route("/hello/<name>",
           methods=["GET", "POST"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}!!!"

# show_nameエンドポイントを作成する
@app.route("/name/<name>")
def show_name(name):
    # 変数をテンプレートエンジンに渡す
    return render_template("index.html" , name=name)

with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/<name>
    print(url_for("show_name", name="shishiro", page="1"))

# アプリケーションコンテキストを取得してスタックへpushする
ctx = app.app_context()
ctx.push()

# current_appにアクセスが可能になる
print(current_app.name)

# グローバルなテンポラリ領域に値を設定する
g.connection = "connection"
print(g.connection)

with app.test_request_context("/users?updated=true"):
    # trueが出力される
    print(request.args.get("updated"))