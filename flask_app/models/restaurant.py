from flask import flash
from datetime import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from pprint import pprint


class Restaurant:
    DB = "group_project"

    def __init__(self, data):
        self.id = data["id"]
        self.title = data["title"]
        self.network = data["network"]
        self.release_date = data["release_date"]
        self.comments = data["comments"]
        self.create_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.user_id = data["user_id"]
        self.user = None

    @staticmethod
    def form_is_valid(form_data):
        is_valid = True

        if len(form_data["title"]) == 0:
            flash("Please enter Title.")
            is_valid = False
        elif len(form_data["title"]) < 3:
            flash("Title must be at least three characters.")
            is_valid = False

        if len(form_data["network"]) == 0:
            flash("Please enter Network.")
            is_valid = False
        elif len(form_data["network"]) < 3:
            flash("Network must be at least three characters.")
            is_valid = False

        if len(form_data["comments"]) == 0:
            flash("Please enter Comments.")
            is_valid = False
        elif len(form_data["comments"]) < 3:
            flash("Comments must be at least three characters.")
            is_valid = False

        # Data Validator
        if len(form_data["release_date"]) == 0:
            flash("Please enter Release Date.")
            is_valid = False
        else:
            try:
                datetime.strptime(form_data["release_date"], "%Y-%m-%d")
            except:
                flash("Invalid Release Date.")
                is_valid = False

        return is_valid

    @classmethod
    def find_all(cls):
        query = """SELECT * FROM restaurants JOIN users ON restaurants.user_id = users.id"""
        list_of_dicts = connectToMySQL(restaurant.DB).query_db(query)

        restaurants = []
        for each_dict in list_of_dicts:
            restaurant = restaurant(each_dict)
            restaurants.append(restaurant)
        return restaurants

    @classmethod
    def find_all_with_users(cls):
        query = """SELECT * FROM restaurants JOIN users ON restaurants.user_id = users.id"""

        list_of_dicts = connectToMySQL(restaurant.DB).query_db(query)

        restaurants = []
        for each_dict in list_of_dicts:
            restaurant = restaurant(each_dict)
            user_data = {
                "id": each_dict["users.id"],
                "first_name": each_dict["first_name"],
                "last_name": each_dict["last_name"],
                "email": each_dict["email"],
                "password": each_dict["password"],
                "created_at": each_dict["users.created_at"],
                "updated_at": each_dict["users.updated_at"],
            }
            user = User(user_data)
            restaurant.user = user
            restaurants.append(restaurant)
        return restaurants

    @classmethod
    def find_by_id(cls, restaurant_id):
        query = """SELECT * FROM restaurants WHERE id = %(restaurant_id)s;"""
        data = {"restaurant_id": restaurant_id}
        list_of_dicts = connectToMySQL(restaurant.DB).query_db(query, data)

        if len(list_of_dicts) == 0:
            return None

        restaurant = restaurant(list_of_dicts[0])
        return restaurant

    @classmethod
    def find_by_id_with_user(cls, restaurant_id):
        query = """SELECT * FROM restaurants JOIN users ON restaurants.user_id = users.id 
        WHERE restaurants.id = %(restaurant_id)s"""

        data = {"restaurant_id": restaurant_id}
        list_of_dicts = connectToMySQL(restaurant.DB).query_db(query, data)

        if len(list_of_dicts) == 0:
            return None

        restaurant = restaurant(list_of_dicts[0])
        user_data = {
            "id": list_of_dicts[0]["users.id"],
            "first_name": list_of_dicts[0]["first_name"],
            "last_name": list_of_dicts[0]["last_name"],
            "email": list_of_dicts[0]["email"],
            "password": list_of_dicts[0]["password"],
            "created_at": list_of_dicts[0]["users.created_at"],
            "updated_at": list_of_dicts[0]["users.updated_at"],
        }
        restaurant.user = User(user_data)
        return restaurant

    @classmethod
    def create(cls, form_data):
        query = """INSERT INTO restaurants
        (title, network, release_date, comments, user_id)
        VALUES
        (%(title)s, %(network)s, %(release_date)s, %(comments)s, 
        %(user_id)s)"""
        restaurant_id = connectToMySQL(restaurant.DB).query_db(query, form_data)
        return restaurant_id

    @classmethod
    def update(cls, form_data):
        query = """UPDATE restaurants
        SET
        title=%(title)s,
        network=%(network)s,
        release_date=%(release_date)s,
        comments=%(comments)s
        WHERE id = %(restaurant_id)s;"""
        connectToMySQL(restaurant.DB).query_db(query, form_data)
        return

    @classmethod
    def delete_by_id(cls, restaurant_id):
        query = """DELETE FROM restaurants WHERE id = %(restaurant_id)s;"""
        data = {"restaurant_id": restaurant_id}
        connectToMySQL(restaurant.DB).query_db(query, data)
        return

    @classmethod
    def count_by_title(cls, title):
        query = """SELECT COUNT(title) AS "count"
        FROM restaurants WHERE title = %(title)s"""
        data = {"title": title}
        list_of_dicts = connectToMySQL(restaurant.DB).query_db(query, data)
        pprint(list_of_dicts)
        return list_of_dicts[0]["count"]
