from flask import Flask,request,render_template,url_for,redirect,flash
from flask_sqlalchemy import SQLAlchemy
from pathlib import Path
import json
import time


app = Flask(__name__)
app.secret_key = "secret_key"

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///tmp/user_data.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class UserNetInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_action = db.Column(db.String(10))
    user_net_income =db.Column(db.String())
    user_item_type = db.Column(db.String())
    time_stamp = db.Column(db.String())

    def __repr__(self):
        return "<UserNetInfo {0}>".format(self.id)


@app.route("/",methods = ["GET","POST"])
def dashboard():
    if request.method == "GET":
        users = get_from_db()
        total_income = sum([float(u.user_net_income) for u in users])
        return render_template("dashboard.html",net_income=total_income,user_info = users)

@app.route("/add/",methods = ["GET","POST"])
def addItem_to_list():
    # Validation for the fields incase JS is disabled
    if request.method == "POST":
        if request.form["income"] == "" or request.form["action-type"] == "":
            flash("Please fill in the daily income gains")
            return redirect(url_for("errorPage"))

        # add new fields here
        user_daily_income = request.form["income"]
        user_action_type  = request.form["action-type"]
        user_item_type = None
        if request.form["item-type"]:
            user_item_type = request.form["item-type"]
        if user_action_type == "spent":
            user_daily_income = float(user_daily_income) * -1
            user_daily_income = str(user_daily_income)
        # add to db
        add_to_db(uincome = user_daily_income,uactiontype = user_action_type,user_item_type=user_item_type)
        return redirect(url_for("dashboard"))
    return "OK"

@app.route("/remove",methods = ["GET","POST"])
def remove_item():
    return "deletion succesful!"

def add_to_db(uincome = None,uactiontype = None,user_item_type = None):
    time_stamp = round(time.time())
    user_data = UserNetInfo(user_action = uactiontype,user_net_income = uincome,user_item_type=user_item_type,time_stamp=time_stamp)
    db.session.add(user_data)
    db.session.commit()

def get_from_db():
    info = UserNetInfo.query.order_by(UserNetInfo.time_stamp).all()
    return info

@app.route("/error/",methods = ["GET","POST"])
def errorPage():
    return render_template("error_page.html")



if __name__ == "__main__":
    app.run(debug=True,port=5000)
