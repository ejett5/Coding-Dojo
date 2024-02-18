from flask_app.config.mysqlconnection import connectToMySQL

class Dojo():
    DB = "dojos_ninja_schema"
    def __dojo__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #making method to create new dojo
    @classmethod
    def create_user(cls,data):
        query = """INSERT INTO users (first_name,last_name, email)
        VALUES( %(first_name)s, %(last_name)s, %(email)s);
        """
        result = connectToMySQL('users_schema').query_db(query,data)
        return result
    
    # view all dojos information
    @classmethod
    def view_user(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append( cls(user))
        return users