from flask import flash
from datetime import datetime
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User
from pprint import pprint

# CLASS INITIALIZER BEGIN

class Restaurant:
    DB = "group_project"

    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.cuisine = data["cuisine"]
        self.street = data["street"]
        self.city = data["city"]
        self.state = data["state"]
        self.zip_code = data["zip_code"]
        self.phone_number = data["phone_number"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        #self.AvgRating =  data["AvgRating"]

# CLASS INITIALIZER END




# CREATE METHODS BEGIN

    @classmethod
    def create(cls, form_data):
        query = """INSERT INTO restaurants
        (name, cuisine, street, city, user_id)
        VALUES
        (%(name)s, %(cuisine)s, %(street)s, %(city)s, 
        %(user_id)s)"""
        restaurant_id = connectToMySQL(Restaurant.DB).query_db(query, form_data)
        return restaurant_id

# CREATE METHODS END




# READ METHODS BEGIN

# Form validator
    @staticmethod
    def form_is_valid(form_data):
        is_valid = True

        if len(form_data["name"]) == 0:
            flash("Please enter name.")
            is_valid = False
        elif len(form_data["name"]) < 3:
            flash("name must be at least three characters.")
            is_valid = False

        if len(form_data["cuisine"]) == 0:
            flash("Please enter cuisine.")
            is_valid = False
        elif len(form_data["cuisine"]) < 3:
            flash("cuisine must be at least three characters.")
            is_valid = False

        if len(form_data["city"]) == 0:
            flash("Please enter city.")
            is_valid = False
        elif len(form_data["city"]) < 3:
            flash("city must be at least three characters.")
            is_valid = False

        # Data Validator
        if len(form_data["street"]) == 0:
            flash("Please enter Release Date.")
            is_valid = False
        else:
            try:
                datetime.strptime(form_data["street"], "%Y-%m-%d")
            except:
                flash("Invalid Release Date.")
                is_valid = False

        return is_valid

    @classmethod
    def find_all(cls):
        query = """SELECT * FROM restaurants JOIN users ON restaurants.user_id = users.id"""
        list_of_dicts = connectToMySQL(Restaurant.DB).query_db(query)

        restaurants = []
        for each_dict in list_of_dicts:
            restaurant = Restaurant(each_dict)
            restaurants.append(restaurant)
        return restaurants

    @classmethod
    def find_all_with_ratings(cls):
        query = """with cte1 as(
                SELECT restaurant_id
                ,round(AVG(rating),0) AS AverageRating
                FROM ratings
                GROUP BY restaurant_id
                )
                SELECT restaurants.name as 'name',
                restaurants.cuisine as 'cuisine', 
                restaurants.id as 'id'
                ,coalesce(CAST(cte1.AverageRating as char), 0) AS 'AvgRating'
                FROM restaurants
                LEFT JOIN cte1
                on restaurants.id = cte1.restaurant_id;"""
        results = connectToMySQL(cls.DB).query_db(query)
        all_restaurants = []
        for row in results:
            one_restaurant = cls(row)
            one_restaurants_info = {
                "AvgRating": row['AvgRating'], 
                "name": row['name'],
                "cuisine": row['cuisine'],
                "id": row['id']
            }
            print(one_restaurants_info)
            one_restaurant.avg = one_restaurants_info
        for one_restaurant in results:
            all_restaurants.append(cls(one_restaurant))
        return all_restaurants

    @classmethod
    def find_by_id(cls, restaurant_id):
        query = """SELECT * FROM restaurants WHERE id = %(id)s"""
        data = {'id': restaurant_id}
        result = connectToMySQL(cls.DB).query_db(query, data)
        if result:
            return cls(result[0])
        else:
            return None

# Method to count how many restaurants there are with a specific name
    @classmethod
    def count_by_name(cls, name):
        query = """SELECT COUNT(name) AS "count"
        FROM restaurants WHERE name = %(name)s"""
        data = {"name": name}
        list_of_dicts = connectToMySQL(Restaurant.DB).query_db(query, data)
        pprint(list_of_dicts)
        return list_of_dicts[0]["count"]

# READ METHODS END




# UPDATE METHODS BEGIN

    @classmethod
    def update(cls, form_data):
        query = """UPDATE restaurants
        SET
        name=%(name)s,
        cuisine=%(cuisine)s,
        street=%(street)s,
        city=%(city)s
        WHERE id = %(restaurant_id)s;"""
        connectToMySQL(Restaurant.DB).query_db(query, form_data)
        return

# UPDATE METHODS END




# DELETE METHODS BEGIN

    @classmethod
    def delete_by_id(cls, restaurant_id):
        query = """DELETE FROM restaurants WHERE id = %(restaurant_id)s;"""
        data = {"restaurant_id": restaurant_id}
        connectToMySQL(Restaurant.DB).query_db(query, data)
        return

# DELETE METHODS END


