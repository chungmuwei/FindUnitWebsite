from datetime import date
from modules import args, crawl
from flask import Flask, render_template, request, redirect, url_for, session, flash


app = Flask(__name__)

app.secret_key = "OjGRROjsOGJO#rJOJR#4jf#O#J@rfeOEOE"

@app.route("/")
def index():
    return render_template("index.html", current_year = date.today().year)

@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        unit_codes = request.form["unitCodes"]
        
        # check if the year is valid
        year = int(request.form["year"])
        if not args.valid_year(year):
            flash(str(year) + " is not a valid year!")
            # return redirect(url_for("index"))

        units = dict()
        # check if the unit code is valid
        for unit_code in unit_codes.split():
            if not args.valid_unit_code(unit_code):
                flash(unit_code.upper() + " is not a unit of study code!")
                # return redirect(url_for("index"))
            else:
                units[unit_code] = crawl.get_unit_outline_url(unit_code, year, False)
                # return redirect(url_for("index"))
        return render_template("result.html", unit_codes=unit_codes, units=units)
    
    else:
        return render_template("result.html")