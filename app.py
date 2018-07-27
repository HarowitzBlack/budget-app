from flask import Flask,request,render_template,url_for,redirect,flash
from pathlib import Path
import json
import time


app = Flask(__name__)
app.secret_key = "secret_key"

@app.route("/",methods = ["GET","POST"])
def dashboard():
    if request.method == "GET":
        udata = getAll_userData()
        print(type(udata))
        return render_template("dashboard.html",data=udata)

@app.route("/add/",methods = ["GET","POST"])
def addItem_to_list():
    # Validation for the fields incase JS is disabled
    if request.method == "POST":
        # add new fields here
        user_daily_income = request.form["income"]
        user_action_type  = request.form["action-type"]
        create_jsonDoc(uincome = user_daily_income,uactiontype = user_action_type)
        if request.form["income"] == "":
            flash("Please fill in the daily income gains")
            return redirect(url_for("errorPage"))
        return "Added to list"
    return "OK"

def getAll_userData():
    with open("data.json","r") as docfile:
        data = json.load(docfile)
        return data

def create_jsonDoc(uincome = None,uactiontype = None):
        with open("data.json","w") as docfile:
            data = {"income":uincome,"action":uactiontype,"timestamp":time.time()}
            docfile.write(json.dumps(data))


@app.route("/error/",methods = ["GET","POST"])
def errorPage():
    return render_template("error_page.html")



if __name__ == "__main__":
    app.run(debug=True,port=5000)
