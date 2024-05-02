from flask_app import app
from flask_app.models.comment import Comment
from flask_app.models.user import User
from flask import flash, render_template, redirect, request, session


@app.post("/comments/create")
def create_comment():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    restaurant_id = request.form["restaurant_id"]

    if not Comment.form_is_valid(request.form):
        return redirect(f"/restaurants/{restaurant_id}")

    Comment.create(request.form)
    return redirect(f"/restaurants/{restaurant_id}")

@app.get("/comments/<int:restaurant_id>/edit")
def edit_comment(restaurant_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    restaurant = restaurant.find_by_id(restaurant_id)
    user = User.find_by_id(session["user_id"])
    return render_template("edit_comment.html", restaurant=restaurant, user=user)


@app.post("/comments/<int:comment_id>/delete")
def comment_delete(comment_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    comment_id = request.form["comment_id"]
    restaurant_id = request.form["restaurant_id"]

    Comment.delete_comment(comment_id)

    return redirect(f"/restaurants/{restaurant_id}")
