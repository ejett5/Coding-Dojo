from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class Dojo():
    DB = "dojo_survey_schema"
    def __dojo__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    #making method to create new dojo
    @classmethod
    def create_user(cls,data):
        query = """INSERT INTO dojos (name)
        VALUES( %(name)s, %(location)s, %(language)s, %(comment)s);
        """
        result = connectToMySQL('dojo_survey_schema').query_db(query,data)
        return result
    
    # view all dojos information
    @classmethod
    def view_dojo(cls):
        query = "SELECT * FROM dojo;"
        results = connectToMySQL(cls.DB).query_db(query)
        Dojo = []
        for Dojo in results:
            Dojo.append( cls(Dojo))
        return Dojo
    
    @classmethod
    def validate_dojo(Dojo):
        is_valid = True
        if len(Dojo)['name'] < 5:
            flash("Name mjust be at least 5 characters.")
            is_valid = False
        if len(Dojo)['location'] < 5:
            flash('location must be at least 5 character.')
            is_valid = False
        if len(Dojo['language']) < 5:
            flash("must be at least 5 characters.")
            is_valid = False
        if len(Dojo['comment']) < 5:
            flash("must be at least 5 characters")
            is_valid = False
        return is_valid

