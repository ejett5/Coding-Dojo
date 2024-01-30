from mysqlconnection import connectToMySQL


#creating class to hold the survey results
class Survey:
    DB = "users_schema" #put name of schema to be used here inside db
    def __init__(self, data):
        self.id = data[id]
        self.name = data['first_name']
        self.name = data['last_name']
        self.email = data['email']
        self.location = data['location']
        self.favorite_language = data['favorite_language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

        
    def validate_survey(form_data):
        #validating data 
        if 'first_name' not in form_data or 'last_name' not in form_data:
            return False
        return True    
        



        
    @classmethod
    def save(cls, data):
        query = """ INSERT into survey (first_name, last_name, email,  location, favorite_language, comments)
                VALUES(%(name)s,%(location)s,%(favorite_language)s,%(comment)s) """
        result = connectToMySQL(cls.DB).query_db(query,data)
        return result
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM survey;"
        results = connectToMySQL(cls.DB).query_db(query)
        surveys = [cls(result) for result in results]
        return surveys



#making form validation 
# class thing:
# @staticmethod
# def validate_users(thing):
#     is_valid = Trueif len(users['first_name']) < 3:
#         flash("name must be a minimum of 3 characters.")
#         is_valid = False
#     is_valid = Trueif len(users['last_name']) < 3:
#         flash("name must be a minimum of 3 characters.")
#         is_valid = False
#     is_valid = Trueif len(users['email']) < 3:
#         flash("must be a minimum of 3 characters.")
#         is_valid = False
#     return is_valid