from flask_app import app
from flask_app.models.restaurant import Restaurant
from flask_app.models.user import User
from flask_app.models.rating import Rating
from flask import flash, render_template, redirect, request, session


@app.route("/restaurants/all")
def restaurants():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    restaurants = restaurant.find_all_with_users()
    user = User.find_by_id(session["user_id"])
    return render_template("all_restaurants.html", restaurants=restaurants, user=user)


@app.get("/restaurants/new")
def new_restaurant():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.find_by_id(session["user_id"])
    return render_template("new_restaurant.html", user=user)


@app.post("/restaurants/create")
def create_restaurant():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    if not restaurant.form_is_valid(request.form):
        session["comments"] = request.form["comments"]
        return redirect("/restaurants/new")

    if restaurant.count_by_title(request.form["title"]) >= 1:
        session["comments"] = request.form["comments"]
        flash("restaurant already exists!")
        return redirect("/restaurants/new")

    if "comments" in session:
        session.pop("comments")

    restaurant.create(request.form)

    return redirect("/restaurants/all")


@app.get("/restaurants/<int:restaurant_id>")
def restaurant_details(restaurant_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    restaurant_comments = Comment.all_comments(restaurant_id)
    restaurant = restaurant.find_by_id_with_user(restaurant_id)
    user = User.find_by_id(session["user_id"])
    return render_template(
        "restaurant_details.html", user=user, restaurant=restaurant, restaurant_comments=restaurant_comments
    )


@app.get("/restaurants/<int:restaurant_id>/edit")
def edit_restaurant(restaurant_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    restaurant = restaurant.find_by_id(restaurant_id)
    user = User.find_by_id(session["user_id"])
    return render_template("edit_restaurant.html", restaurant=restaurant, user=user)


@app.post("/restaurants/update")
def update_restaurant():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    restaurant_id = request.form["restaurant_id"]
    if not restaurant.form_is_valid(request.form):
        session["comments"] = request.form["comments"]
        return redirect(f"/restaurants/{restaurant_id}/edit")

    if restaurant.count_by_title(request.form["title"]) >= 1:
        session["comments"] = request.form["comments"]
        flash("restaurant already exists!")
        return redirect(f"/restaurants/{restaurant_id}/edit")

    if "comments" in session:
        session.pop("comments")

    restaurant.update(request.form)
    return redirect("/restaurants/all")


@app.post("/restaurants/<int:restaurant_id>/delete")
def delete_restaurant(restaurant_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    restaurant.delete_by_id(restaurant_id)
    return redirect("/restaurants/all")
