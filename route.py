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
        not_found_any_unit_url = True # whether any unit outline url is found
        # check if the unit code is valid
        for unit_code in unit_codes.split():
            if not args.valid_unit_code(unit_code):
                flash("Unit \"" + unit_code.upper() + "\" is not in correct format! A valid unit code should be 4 letters followed by 4 digits.")

            else:
                result = crawl.get_unit_outline_url(unit_code, year, False)
                if result == None:
                    flash("Unit \"" + unit_code.upper() + "\" was not found!")
                elif len(result) == 0:
                    flash("Unit code \"" + unit_code.upper() + f"\" outline in  {year} was not found!")
                else:
                    units[unit_code.upper()] = result
                    not_found_any_unit_url = False

        # if unit_codes is empty, return to index page
        if not_found_any_unit_url:
            return render_template("index.html")
        else:
            return render_template("result.html", unit_codes=unit_codes, units=units)
    
    else:
        return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")