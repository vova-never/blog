from flask import Flask,url_for, redirect
import os
import setting as stg



dirname = os.getcwd()

app = Flask(__name__, static_folder=stg.path_static )
app.config["secret_key = "] = stg.secret_key  

@app.route("/")
def index():
    url = url_for("templates/index.html")

@app.route("/post/category")
def post_category():
    return "тут будуть категорії постів"

@app.route("/post/view")
def post_view():
    return "тут буде пост"

@app.route("/about")
def about():
    return "інфо про автора автора"



app.run(debug = True)