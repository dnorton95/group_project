from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models.user import User
from pprint import pprint


# CLASS INITIALIZER BEGIN

class Rating:
    DB = "group_project"
    def __init__(self, data):
        self.id = data["id"]
        self.rating = data["rating"]
        self.comment = data["comment"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.restaurant_id = data["restaurant_id"]
        self.users = {
            "id": data["user_id"],
            "first_name": data["first_name"],
            "last_name": data["last_name"],
        }
        self.rating_id = data["id"]


# CLASS INITIALIZER END





# CREATE METHODS BEGIN

    @classmethod
    def create(cls, form_data):
        query = """INSERT INTO ratings (user_id, restaurant_id, rating, comment) 
                VALUES (%(user_id)s, %(restaurant_id)s, %(rating)s, %(comment)s);"""
        connectToMySQL("restaurants_schema").query_db(query, form_data)
        return

# CREATE METHODS END





# READ METHODS BEGIN

    @classmethod
    def all_ratings(cls, restaurant_id):
        data = {"restaurant_id": restaurant_id}
        query = """SELECT *
                FROM ratings
                JOIN users ON ratings.user_id = users.id
                WHERE ratings.restaurant_id = %(restaurant_id)s
                ORDER BY ratings.created_at DESC; """
        list_of_dicts = connectToMySQL(Rating.DB).query_db(query, data)
        pprint(list_of_dicts)

        ratings = []
        for each_dict in list_of_dicts:
            rating = Rating(each_dict)
            ratings.append(rating)
        return ratings
# Gets the rating ID where user and restaurant ID are available
    @classmethod
    def get_user_rating_id(cls, restaurant_id, user_id):
        query = "SELECT id FROM ratings WHERE restaurant_id = %s AND user_id = %s"
        result = connectToMySQL(cls.DB).query_db(query, (restaurant_id, user_id))
        if result:
            return result[0]['id']
        return None
# Checks if user has submitted a rating already
    @classmethod
    def has_submitted_rating(cls, restaurant_id, user_id):
        query = "SELECT COUNT(*) as count FROM ratings WHERE restaurant_id = %s AND user_id = %s"
        result = connectToMySQL(cls.DB).query_db(query, (restaurant_id, user_id))
        return result[0]['count'] > 0
# Validates comments by length and rating numbers
    @staticmethod
    def form_is_valid(form_data):
        is_valid = True

        if len(form_data.get("comment", "")) == 0:
            flash("Please enter a comment.")
            is_valid = False
        elif len(form_data["comment"]) < 3:
            flash("Comment must be at least three characters.")
            is_valid = False

        if form_data.get("rating", "") not in ["1", "2", "3", "4", "5"]:
            flash("Please select a valid rating.")
            is_valid = False

        return is_valid

# READ METHODS END





# UPDATE METHODS BEGIN

    @classmethod
    def update(cls, form_data):
        query = """UPDATE ratings
        SET
        rating=%(rating)s,
        comment=%(comment)s
        WHERE id = %(rating_id)s;"""
        connectToMySQL(Rating.DB).query_db(query, form_data)
        return

# UPDATE METHODS END





# DELETE METHODS BEGIN

    @classmethod
    def delete_rating(cls, rating_id):
        query = """DELETE FROM ratings WHERE id = %(rating_id)s"""
        data = {"rating_id": rating_id}
        connectToMySQL(Rating.DB).query_db(query, data)
        return
    
# DELETE METHODS END


