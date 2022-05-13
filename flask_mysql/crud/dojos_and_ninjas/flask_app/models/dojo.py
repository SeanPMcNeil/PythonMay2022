from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        self.ninjas = [];

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"

        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos = []

        for dojo in results:
            dojos.append( cls(dojo) )
        
        return dojos
    
    @classmethod
    def create_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at) VALUES (%(name)s, NOW())";
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

        this_dojo = cls( results[0] )

        for row_from_db in results:
            ninja_data = {
                'id' : row_from_db['ninjas.id'],
                'dojo_id' : row_from_db['id'],
                'first_name' : row_from_db['first_name'],
                'last_name' : row_from_db['last_name'],
                'age' : row_from_db['age'],
                'created_at' : row_from_db['created_at'],
                'updated_at' : row_from_db['updated_at']
            }
            this_dojo.ninjas.append( ninja.Ninja(ninja_data) )

        return this_dojo