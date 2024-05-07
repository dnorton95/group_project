from flask_app.config.mysqlconnection import connectToMySQL

class Rating:
    db = "group_project"
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

    @classmethod
    def all_ratings(cls, restaurant_id):
        data = {"restaurant_id": restaurant_id}
        query = """SELECT *
                FROM ratings
                JOIN users ON ratings.user_id = users.id
                WHERE ratings.restaurant_id = %(restaurant_id)s
                ORDER BY ratings.created_at DESC; """
        list_of_dicts = connectToMySQL(Rating.db).query_db(query, data)

        ratings = []
        for each_dict in list_of_dicts:
            rating = Rating(each_dict)
            ratings.append(rating)
        return ratings