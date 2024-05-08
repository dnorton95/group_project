from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import rating
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
        self.AvgRating =  data["AvgRating"]

# CLASS INITIALIZER END


# READ METHODS BEGIN

    @classmethod
    def find_all_with_ratings(cls):
        query = """with cte1 as(
                SELECT restaurant_id
                ,round(AVG(rating),0) AS AverageRating
                FROM ratings
                GROUP BY restaurant_id
                )
                SELECT *
                ,coalesce(CAST(cte1.AverageRating as char), 0) AS 'AvgRating'
                FROM restaurants
                LEFT JOIN cte1
                on restaurants.id = cte1.restaurant_id;"""
        results = connectToMySQL(cls.DB).query_db(query)
        all_restaurants = []
        for row in results:
            one_restaurant = cls(row)
            one_restaurants_info = {
                "id": row["id"],
                "name": row["name"],
                "cuisine" : row["cuisine"],
                "street": row["street"],
                "city": row["city"],
                "state": row["state"],
                "zip_code": row["zip_code"],
                "phone_number": row["phone_number"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "AvgRating": row["AvgRating"],
            }
            print(one_restaurants_info)
            one_restaurant.avg = one_restaurants_info
        for one_restaurant in results:
            all_restaurants.append(cls(one_restaurant))
        return all_restaurants

    @classmethod
    def find_one_with_rating(cls, restaurant_id):
        query = """with cte1 as(
                SELECT restaurant_id
                ,round(AVG(rating),0) AS AverageRating
                FROM ratings
                GROUP BY restaurant_id
                )
                SELECT *
                ,coalesce(CAST(cte1.AverageRating as char), 0) AS 'AvgRating'
                FROM restaurants
                LEFT JOIN cte1
                on restaurants.id = cte1.restaurant_id
                WHERE restaurants.id = %(restaurant_id)s;"""
        data = {'restaurant_id': restaurant_id}
        results = connectToMySQL(cls.DB).query_db(query, data)
        if len(results) == 0:
            return None
        restaurant = []
        for row in results:
            one_restaurant = cls(row)
            one_restaurants_info = {
                "id": row["id"],
                "name": row["name"],
                "cuisine" : row["cuisine"],
                "street": row["street"],
                "city": row["city"],
                "state": row["state"],
                "zip_code": row["zip_code"],
                "phone_number": row["phone_number"],
                "created_at": row["created_at"],
                "updated_at": row["updated_at"],
                "AvgRating": row["AvgRating"],
            }
            print(one_restaurants_info)
        for one_restaurant in results:
            restaurant.append(cls(one_restaurant))
        return restaurant

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


