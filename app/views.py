from app import app
from flask import render_template
from app.web import Affected, Countries, today, New


@app.route("/")
def index():
    return render_template("home/index.html", cases=Affected, countries=Countries, date=today, new_cases=New)

#@app.route("/rend")
#def rend():
   # return render_template("home/home.html", cases=Affected, countries=Countries, date=today, new_cases=New)
   