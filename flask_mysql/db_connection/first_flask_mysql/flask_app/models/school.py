from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import friend

class School:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.friends = []

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM schools;"

        results = connectToMySQL('first_flask_schema').query_db(query)
        schools = []

        for school in results:
            schools.append( cls(school) )

        return schools

    @classmethod
    def get_school_with_friends(cls, data):
        query = "SELECT * FROM schools LEFT JOIN friends ON friends.school_id = schools.id WHERE schools.id = %(id)s;"
        results = connectToMySQL('first_flask_schema').query_db(query, data)

        this_school = cls( results[0] )

        for row_from_db in results:
            friend_data = {
                'id' : row_from_db['friends.id'],
                'school_id' : row_from_db ['id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'occupation' : row_from_db['occupation'],
                'created_at' : row_from_db['friends.created_at'],
                'updated_at' : row_from_db['friends.updated_at']
                }
            this_school.friends.append( friend.Friend(friend_data) )
        
        return this_school
