from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash
import re


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

class Email():
    DB = 'email_validation_schema'
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']

    @classmethod
    def submit_email(cls, data):
        query = """ INSERT INTO email (email)
        VALUES( %(email)s );
        """
        result = connectToMySQL('email_validation_schema').query_db(query, data)
        return result