from flask_app import app
from flask_app.models.restaurant import Restaurants
from flask import render_template

#route for displaying dashboard
@app.route('/')
def dashboard():
    #if "user_id" not in session:
    #    return redirect('/')
    #user=Users.get_one_by_id(session["user_id"])
    restaurant = Restaurants.find_all_with_ratings()
    return render_template('all_restaurants.html', all_restaurants = restaurant)