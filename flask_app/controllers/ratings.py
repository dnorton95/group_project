from flask_app import app
from flask_app.models.rating import Rating
from flask_app.models.restaurant import Restaurant
from flask import flash, render_template, redirect, request, session

# CREATE BEGIN

@app.post("/ratings/create")
def create_rating():
    restaurant_id = request.form["restaurant_id"]
    if not Rating.form_is_valid(request.form):
            return redirect(f"/restaurants/{restaurant_id}")
    Rating.create(request.form)
    return redirect(f"/restaurants/{restaurant_id}")

# CREATE END


# UPDATE BEGIN

@app.route("/ratings/<int:rating_id>/edit")
def rating_edit(rating_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    rating = Rating.find_by_id(rating_id)  # Find the rating object
    if not rating:
        flash("Rating not found.", "error")
        return redirect("/")
    return render_template("edit_rating.html", rating=rating)

@app.post("/ratings/update")
def rating_update():
    restaurant_id = request.form["restaurant_id"]
    rating_id = request.form["rating_id"]
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")
    if not Rating.form_is_valid(request.form):
        session["comment"] = request.form["comment"]
        return redirect(f"/ratings/{rating_id}/edit")  
    if "comments" in session:
        session.pop("comments")
    Rating.update(request.form)
    return redirect(f"/restaurants/{restaurant_id}")

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
    return redirect(f"/restaurants/{restaurant_id}")

# DELETE END