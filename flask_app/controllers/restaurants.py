
from flask_app import app
from flask_app.models.restaurant import Restaurant
from flask_app.models.user import User
from flask_app.models.rating import Rating
from flask import flash, render_template, redirect, request, session

@app.route("/restaurants/all")
def all_restaurants():
    # if "user_id" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")

    restaurants = Restaurant.find_all_with_users()
    user = User.find_by_id(session["user_id"])
    return render_template("all_restaurants.html", restaurants=restaurants, user=user)


@app.get("/restaurants/new")
def new_restaurant():
    # if "user_id" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")

    user = User.find_by_id(session["user_id"])
    return render_template("new_restaurant.html", user=user)


@app.post("/restaurants/create")
def create_restaurant():
    # if "user_id" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")

    if not Restaurant.form_is_valid(request.form):
        session["comments"] = request.form["comments"]
        return redirect("/restaurants/new")

    if Restaurant.count_by_name(request.form["name"]) >= 1:
        session["comments"] = request.form["comments"]
        flash("Restaurant already exists!")
        return redirect("/restaurants/new")

    if "comments" in session:
        session.pop("comments")

    Restaurant.create(request.form)

    return redirect("/restaurants/all")


@app.route("/restaurants/<int:restaurant_id>")
def restaurant_details(restaurant_id):
    restaurant = Restaurant.find_by_id(restaurant_id)
    restaurant_ratings = Rating.all_ratings(restaurant_id)
    return render_template("restaurant_details.html", restaurant=restaurant, restaurant_ratings=restaurant_ratings)


@app.get("/restaurants/<int:restaurant_id>/edit")
def edit_restaurant(restaurant_id):
    # if "user_id" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")

    restaurant = Restaurant.find_by_id(restaurant_id)
    user = User.find_by_id(session["user_id"])
    return render_template("edit_restaurant.html", restaurant=restaurant, user=user)


@app.post("/restaurants/update")
def update_restaurant():
    # if "user_id" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")

    restaurant_id = request.form["restaurant_id"]
    if not Restaurant.form_is_valid(request.form):
        session["comments"] = request.form["comments"]
        return redirect(f"/restaurants/{restaurant_id}/edit")

    if Restaurant.count_by_name(request.form["name"]) >= 1:
        session["comments"] = request.form["comments"]
        flash("Restaurant already exists!")
        return redirect(f"/restaurants/{restaurant_id}/edit")

    if "comments" in session:
        session.pop("comments")

    Restaurant.update(request.form)
    return redirect("/restaurants/all")


@app.post("/restaurants/<int:restaurant_id>/delete")
def delete_restaurant(restaurant_id):
    # if "user_id" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")

    Restaurant.delete_by_id(restaurant_id)
    return redirect("/restaurants/all")
