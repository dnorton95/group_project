from flask_app import app
from flask_app.models.comment import Comment
from flask import flash, render_template, redirect, request, session


@app.post("/comments/create")
def create_comment():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    show_id = request.form["show_id"]

    if not Comment.form_is_valid(request.form):
        return redirect(f"/shows/{show_id}")

    Comment.create(request.form)
    return redirect(f"/shows/{show_id}")


@app.post("/comments/<int:comment_id>/delete")
def comment_delete(comment_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    comment_id = request.form["comment_id"]
    show_id = request.form["show_id"]

    Comment.delete_comment(comment_id)

    return redirect(f"/shows/{show_id}")
