# import the function that will return an instance of a connection
from mysqlconnection import connectToMySQL


# model the class after the friend table from our database
class Friend:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.occupation = data['occupation']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # Now we use class methods to query our database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM friends;"

        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('first_flask_schema').query_db(query)

        # Create an empty list to append our instances of friends
        friends = []

        # Iterate over the db results and create instances of friends with cls.
        for friend in results:
            friends.append( cls(friend) )

        # return new list we created from our results
        return friends

    # Method to Create a Friend
    @classmethod
    def create_friend(cls, data):
        query = "INSERT INTO friends (first_name, last_name, occupation, created_at) VALUES (%(first_name)s, %(last_name)s, %(occupation)s, NOW());"
        return connectToMySQL('first_flask_schema').query_db(query, data)


    # Method to Update a Friend
    @classmethod
    def update_friend(cls, data):
        query = "UPDATE friends SET first_name = %(first_name)s, last_name = %(last_name)s, occupation = %(occupation)s, updated_at = NOW() WHERE id = %(id)s;"
        connectToMySQL('first_flask_schema').query_db(query, data)

    # Method to Delete a Friend
    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM friends WHERE id = %(id)s;"
        connectToMySQL('first_flask_schema').query_db(query, data)