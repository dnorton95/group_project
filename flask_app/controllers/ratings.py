from flask_app import app
from flask_app.models.rating import Rating
from flask import flash, render_template, redirect, request, session

# CREATE BEGIN

@app.post("/ratings/create")
def create_rating():
    restaurant_id = request.form.get("restaurant_id")
    form_data = dict(request.form)
    
    # Manually set user_id for testing
    form_data['user_id'] = 1  # Set this to the appropriate user_id
    
    try:
        Rating.create(form_data)
    except Exception as e:
        print("Error occurred:", e)
        flash('Error occurred while creating the rating. Please try again later.', 'error')
    
    return redirect(f"/restaurants/{restaurant_id}")



# CREATE END



# READ BEGIN

# READ END



# UPDATE BEGIN

@app.get("/ratings/<int:rating_id>/edit")
def rating_edit(rating_id):
    # if "user_id" not in session:
    #     flash("Please log in.", "login")
    #     return redirect("/")

    rating = Rating.find_by_id(rating_id)  # Find the rating object
    if not rating:
        flash("Rating not found.", "error")
        return redirect("/")

    return render_template("edit_rating.html", rating=rating)


# UPDATE END



# DELETE BEGIN

@app.post("/ratings/<int:rating_id>/delete")
def rating_delete(rating_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    rating_id = request.form["rating_id"]
    restaurant_id = request.form["restaurant_id"]

    Rating.delete_rating(rating_id)
    flash('Vote removed')


    return redirect(f"/restaurants/{restaurant_id}")

# DELETE END