from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

EMAIL_REGEX = re.compile( r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')



class Player():
    db = 'login_and_registration'
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @staticmethod
    def validate_user(new_user):
        is_valid = True
        if len(new_user['first_name']) < 1:
            flash('First Name is Required!')
            is_valid = False
        if len(new_user['first_name']) <= 3:
            flash('First Name Must be 3+ characters!')
            is_valid = False

        if len(new_user['last_name']) < 1:
            flash('Last Name is Required!')
            is_valid = False
        if len(new_user['last_name']) <= 3:
            flash('Last Name Must be 3+ characters!')
            is_valid = False

        # Valid Email Format
        if not EMAIL_REGEX.match(new_user['email']):
            flash('Please enter a valid email!')
            is_valid = False
        else:
            # Valid if this email is already in the DB
            query = "SELECT * FROM users WHERE email = %(email)s;"
            results = connectToMySQL(Player.DB).query_db(query, new_user)
            if len(results) >= 1:
                flash("Email taken, try a different Email!")
                is_valid = False

        if new_user['password'] != new_user['confirm_password']:
            flash('Passwords must match!')
            is_valid = False
        if len(new_user['password']) < 1:
            flash('Password is required!')
            is_valid = False
        if len(new_user['password']) < 5:
            flash('Password Must be 5+ characters!')
            is_valid = False

        return is_valid

    @classmethod
    def create_player(cls, data):
        query = """ INSERT INTO players (first_name, last_name, email, password)
        VALUES ( %(first_name)s, %(last_name)s, %(email)s, %(password)s);
        """
        return connectToMySQL(cls.db).query_db(query,data)
        

    @classmethod
    def view_player(cls):
        query = "SELECT * FROM players;"
        results = connectToMySQL(cls.db).query_db(query)
        players = []
        for player in results:
            players.append( cls(player))
        return players
    

    # viewing user by ID
    @classmethod
    def GetUserById(cls, data):
        query = """
        SELECT * FROM players
        WHERE id = %(id)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)

    # getting by email
    @classmethod
    def GetPlayerByEmail(cls, data):
        query = """
        SELECT * FROM players
        WHERE email = %(email)s;
        """
        results = connectToMySQL(cls.db).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])