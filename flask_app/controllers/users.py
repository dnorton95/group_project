# This will be in your controllers folder.  Remember to 'pipenv install flask pymysql flask_bcrypt' in your main project folder!
from flask_app import app, bcrypt
from flask_app.models.user import User
from flask import flash, render_template, redirect, request, session

# Replace all "Users/user" with your class name!


@app.route("/")
def index():
    """This route displays the landing page."""

    return render_template("landing_page.html")


@app.route("/login-reg")
def log_reg():
    """This route displays the login and registration forms."""

    return render_template("login_registration.html")


@app.post("/users/register")
def register():
    """This route process the register form."""

    if not User.validate_register(request.form):
        return redirect("/login-reg")

    potential_user = User.find_by_email(request.form["email"])

    if potential_user != None:
        flash("Email in user!  Please log in!", "register")
        return redirect("/login-reg")

    hashed_pw = bcrypt.generate_password_hash(request.form["password"])
    user_data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": hashed_pw,
    }
    user_id = User.register(user_data)
    session["user_id"] = user_id
    return redirect("/restaurants/all")


@app.post("/users/login")
def login():
    """This route process the login form."""

    if not User.validate_login(request.form):
        return redirect("/login-reg")
    potential_user = User.find_by_email(request.form["email"])
    if potential_user == None:
        flash("Invalid credentials", "login")
        return redirect("/login-reg")

    user = potential_user

    if not bcrypt.check_password_hash(user.password, request.form["password"]):
        flash("Invalid credentials", "login")
        return redirect("/login-reg")

    session["user_id"] = user.id
    return redirect("/restaurants/all")


@app.route("/users/logout")
def logout():
    """This route clears session"""
    session.clear()
    return redirect("/")
