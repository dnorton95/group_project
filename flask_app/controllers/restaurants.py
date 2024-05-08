from flask_app import app
from flask_app.models.restaurant import Restaurant
from flask_app.models.user import User
from flask_app.models.rating import Rating
from flask import render_template, session, flash, redirect



# READ BEGIN

@app.route("/restaurants/all")
def all_restaurants():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    restaurant = Restaurant.find_all_with_ratings()
    user = User.find_by_id(session["user_id"])
    return render_template("all_restaurants.html", all_restaurants = restaurant, user=user)



@app.route("/restaurants/<int:restaurant_id>")
def restaurant_details(restaurant_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    restaurant_ratings = Rating.all_ratings(restaurant_id)
    restaurant = Restaurant.find_one_with_rating(restaurant_id)
    user = User.find_by_id(session["user_id"])
    return render_template("restaurant_details.html", restaurant_ratings=restaurant_ratings, restaurant=restaurant, user=user)


# READ END