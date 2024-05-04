from flask_app import app
from flask_app.models.rating import Rating
from flask import flash, render_template, redirect, request, session

@app.post("/ratings/create")
def create_rating():
    print("Before retrieving restaurant_id from form")
    restaurant_id = request.form.get("restaurant_id")
    print("restaurant ID from form:", restaurant_id)

    form_data = dict(request.form)
    
    form_data['points'] = int(form_data['points'])
    print("Form data:", form_data)
    
    try:
        Rating.create(form_data)
    except Exception as e:
        print("Error occurred:", e)
        flash('Error occurred while creating the rating. Please try again later.', 'error')
    
    return redirect(f"/restaurants/{restaurant_id}")


@app.post("/ratings/<int:rating_id>/delete")
def rating_delete(rating_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    rating_id = request.form["rating_id"]
    restaurant_id = request.form["restaurant_id"]

    Rating.delete_rating(rating_id)
    flash('Vote removed')


    return redirect("/restaurants")
