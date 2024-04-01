from flask_app import app
from flask_app.models.show import Show
from flask_app.models.user import User
from flask_app.models.comment import Comment
from flask import flash, render_template, redirect, request, session


@app.route("/shows/all")
def shows():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    shows = Show.find_all_with_users()
    user = User.find_by_id(session["user_id"])
    return render_template("all_shows.html", shows=shows, user=user)


@app.get("/shows/new")
def new_show():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    user = User.find_by_id(session["user_id"])
    return render_template("new_show.html", user=user)


@app.post("/shows/create")
def create_show():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    if not Show.form_is_valid(request.form):
        session["comments"] = request.form["comments"]
        return redirect("/shows/new")

    if Show.count_by_title(request.form["title"]) >= 1:
        session["comments"] = request.form["comments"]
        flash("Show already exists!")
        return redirect("/shows/new")

    if "comments" in session:
        session.pop("comments")

    Show.create(request.form)

    return redirect("/shows/all")


@app.get("/shows/<int:show_id>")
def show_details(show_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    show_comments = Comment.all_comments(show_id)
    show = Show.find_by_id_with_user(show_id)
    user = User.find_by_id(session["user_id"])
    return render_template(
        "show_details.html", user=user, show=show, show_comments=show_comments
    )


@app.get("/shows/<int:show_id>/edit")
def edit_show(show_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    show = Show.find_by_id(show_id)
    user = User.find_by_id(session["user_id"])
    return render_template("edit_show.html", show=show, user=user)


@app.post("/shows/update")
def update_show():
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    show_id = request.form["show_id"]
    if not Show.form_is_valid(request.form):
        session["comments"] = request.form["comments"]
        return redirect(f"/shows/{show_id}/edit")

    if Show.count_by_title(request.form["title"]) >= 1:
        session["comments"] = request.form["comments"]
        flash("Show already exists!")
        return redirect(f"/shows/{show_id}/edit")

    if "comments" in session:
        session.pop("comments")

    Show.update(request.form)
    return redirect("/shows/all")


@app.post("/shows/<int:show_id>/delete")
def delete_show(show_id):
    if "user_id" not in session:
        flash("Please log in.", "login")
        return redirect("/")

    Show.delete_by_id(show_id)
    return redirect("/shows/all")
