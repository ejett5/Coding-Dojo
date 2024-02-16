from flask_app.config.mysqlconnection import connectToMySQL

class User():
    DB = "users_schema"
    def __init__(self, data):
        # accessing the data that is housed in the database
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls,data):
        query = """INSERT INTO users (first_name,last_name, email)
        VALUES( %(first_name)s, %(last_name)s, %(email)s);
        """
        result = connectToMySQL('users_schema').query_db(query,data)
        return result
    
    @classmethod
    def view_user(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.DB).query_db(query)
        users = []
        for user in results:
            users.append( cls(user))
        return users