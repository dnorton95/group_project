from flask_app import app
from flask_app.models.restaurant import Restaurant
from flask_app.models.user import User
from flask_app.models.rating import Rating
from flask import flash, render_template, redirect, request, session

@app.route("/dashboard")
def restaurants():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    
    user_id = session["user_id"]
    restaurants = restaurant.find_all_restaurants_with_users()
    user = User.find_user_by_id(session["user_id"])
    user_restaurants = restaurant.find_restaurants_by_user_id(user_id)

    return render_template("dashboard.html", restaurants=restaurants, user=user, user_restaurants = user_restaurants)

@app.get("/restaurants")
def get_all_restaurants():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    
    
    restaurants = restaurant.find_all_restaurants_with_users_and_rating()
    user = User.find_user_by_id(session["user_id"])

    for restaurant in restaurants:
        restaurant_rating = Rating.all_rating(restaurant.id)
        restaurant.total_rating = sum(rating.rating for rating in restaurant_rating)

    return render_template("all_restaurants.html", restaurants=restaurants, user=user)


@app.post("/restaurants/create")
def create_restaurant():
    # Check Session for User
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    user_id = session["user_id"]
    # Check Session for User

    # Run restaurant class validator
    if not restaurant.form_is_valid(request.form):
        return redirect("/dashboard")
    # Run restaurant class validator

    if "rating" in request.form:
        session["rating"] = request.form["rating"]

    # Check if the restaurant name is unique
    if restaurant.count_by_recipe(request.form["recipe"]) >= 1:
        flash("restaurant already exists!")
        return redirect("/dashboard")
    # Check if the restaurant name is unique


    if "rating" in session:
        session.pop("rating")

    restaurant.create(request.form)
    flash("restaurant succesfully posted")
    return redirect("/dashboard")

@app.get("/restaurants/<int:restaurant_id>")
def restaurant_details(restaurant_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    restaurant_rating = Rating.all_rating(restaurant_id)
    restaurant = restaurant.find_restaurant_by_id_with_user(restaurant_id)
    user = User.find_user_by_id(session["user_id"])
    user_id = session.get('user_id')
    has_submitted_rating = Rating.has_submitted_rating(restaurant_id, user_id)

    user_rating_id = None  # Initialize user_rating_id

    if has_submitted_rating:
        user_rating_id = Rating.get_user_rating_id(restaurant_id, user_id)  # Retrieve user's rating ID

    if restaurant_rating:
        average_rating = sum(rating.rating for rating in restaurant_rating) / len(restaurant_rating)
    else:
        average_rating = None

    return render_template('restaurant_details.html', restaurant=restaurant, restaurant_rating=restaurant_rating, user=user, average_rating=average_rating, has_submitted_rating=has_submitted_rating, user_rating_id=user_rating_id)

@app.get("/restaurants/<int:restaurant_id>/edit")
def edit_restaurant(restaurant_id):

    # Check if user is in session
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    # Check if user is in session
    
    # Pass in the restaurant and user variables
    restaurant = restaurant.find_restaurant_by_id(restaurant_id)
    user = User.find_user_by_id(session["user_id"])
    # Pass in the restaurant and user variables
    
    return render_template("edit_restaurant.html", restaurant=restaurant, user=user)


@app.post("/restaurants/update")
def update_restaurant():
    # Check if user is in session
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    # Check if user is in session
    
    # Check for restaurant_id
    if "restaurant_id" not in request.form:
        flash("restaurant ID is missing.", "error")
        return redirect("/")
    # Check for restaurant_id

    restaurant_id = request.form["restaurant_id"]
    restaurant = restaurant.find_restaurant_by_id(restaurant_id)

    # Check if the restaurant name is being changed
    if restaurant.recipe != request.form["recipe"]:
        if restaurant.count_by_recipe(request.form["recipe"]) >= 1:
            flash("A restaurant with this name already exists.", "edit_restaurant_error")
            return redirect(f"/restaurants/{restaurant_id}/edit")

    # Validate the existence of restaurant_id and other necessary form fields
    if not restaurant.form_is_valid(request.form):
        flash("Invalid restaurant data.", "error")
        return redirect(f"/restaurants/{restaurant_id}/edit")
    
    # Update the restaurant using restaurant.update() method
    restaurant.update(restaurant_id, request.form)

    flash("restaurant successfully updated")
    return redirect(f"/restaurants/{restaurant_id}")

@app.post("/restaurants/<int:restaurant_id>/delete")
def delete_restaurant(restaurant_id):
    if "user_id" not in session:
        flash("Please log in.")
        return redirect("/")

    user_id = session["user_id"]
    restaurant = restaurant.find_restaurant_by_id(restaurant_id)

    # Check if the logged-in user owns the restaurant
    if restaurant.user_id != user_id:
        flash("You do not have permission to delete this restaurant.", "delete_restaurant_error")
        return redirect("/")

    restaurant.delete_by_id(restaurant_id)
    flash("restaurant successfully deleted")
    return redirect("/dashboard")
