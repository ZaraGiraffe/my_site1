from flask import Flask, redirect, render_template, request
from MapCreator import create_map

app = Flask(__name__)
username = None


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def get_id():
    global username
    username = request.form.get("username")
    if not username:
        return render_template("error.html", message="Missing username")
    create_map(username)
    return redirect("/map")


@app.route("/map")
def map():
    return render_template("map.html")


app.run()
