
from app import app

@app.route("/",methods = ["GET","POST"])
def dashboard():
    if request.method == "GET":
        return render_template("dashboard.html",data="udata")

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
        # add to db
        add_to_db(uincome = user_daily_income,uactiontype = user_action_type)
        return redirect(url_for("dashboard"))
    return "OK"

def add_to_db(uincome = None,uactiontype = None):
    user_data = UserNetInfo(user_action = uactiontype,user_net_income = uincome)
    db.session.add(user_data)
    db.session.commit()

@app.route("/error/",methods = ["GET","POST"])
def errorPage():
    return render_template("error_page.html")
