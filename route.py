from modules import *
from flask import Flask, render_template, request, redirect, url_for, session, flash


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        unit_codes = request.form["unitCodes"]

        return render_template("result.html", unit_codes=unit_codes.split())
    else:
        return render_template("result.html")