from flask_app.config.mysqlconnection import connectToMySQL

class user():
    def __init__(self, data):
        # accessing the data that is housed in the database
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']