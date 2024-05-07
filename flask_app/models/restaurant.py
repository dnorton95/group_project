from flask_app.config.mysqlconnection import connectToMySQL

class Restaurants:
    db = "group_project"
    def __init__( self , data ):
        self.id = data["id"]
        self.name = data["name"]
        self.cuisine = data["cuisine"]
        #self.street = data["street"]
        #self.city = data["city"]
        #self.state = data["state"]
        #self.zip_code = data["zip_code"]
        #self.phone_number = data["phone_number"]
        #self.created_at = data["created_at"]
        #self.updated_at = data["updated_at"]
        self.avg = None

    @classmethod
    def find_all_with_ratings(cls):
        query = """SELECT SUM(rating)/count(*) as 'avg',
                restaurants.name as 'name',
                restaurants.cuisine as 'cuisine', 
                restaurants.id as 'id' FROM ratings
                LEFT JOIN restaurants
                ON ratings.restaurant_id = restaurants.id
                GROUP BY restaurant_id
                ORDER BY restaurant_id;"""
        results = connectToMySQL(cls.db).query_db(query)
        all_restaurants = []
        for row in results:
            one_restaurant = cls(row)
            one_restaurants_info = {
                "avg": row['avg'], 
                "name": row['name'],
                "cuisine": row['cuisine'],
                "id": row['id']
            }
            print(one_restaurants_info)
            one_restaurant.avg = one_restaurants_info
        for one_restaurant in results:
            all_restaurants.append(cls(one_restaurant))
        return all_restaurants