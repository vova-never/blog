from flask import Flask, render_template,url_for, redirect
import os
import setting as stg
import db_scripts as db



dirname = os.getcwd()

app = Flask(__name__, static_folder=stg.path_static )
app.config["secret_key = "] = stg.secret_key 

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/post/category")
def post_category():
    return "тут будуть категорії постів"

@app.route("/post/view")
def post_view():
    return "тут буде пост"

@app.route("/about")
def about():
    user = db.getUser()
    print(user)
    return render_template("about.html", user = user)



app.run(debug = True)