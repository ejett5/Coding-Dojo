from flask_app import app 
from flask import render_template,redirect, request, session, flash, query
from flask_app.models.user_lookup import User 
from flask_app.config.mysqlconnection import connectToMySQL


# landing page for users website
@app.route('/')
def index():
    return render_template('index.html')

# making users for the table
@app.route('/submit_profile/')
def create_user(cls,data):
    query = """INSERT INTO user(first_name,last_name, email)
    VALUES( $(first_name)s, %(last_name)s, $(email)s);
"""
    return redirect('read.html')


# retrieving users and displaying the information
@app.route('/view_users/')
def users_view_all():
    query = "SELECT * FROM users;"
    results = connectToMySQL(cls.DB).query_db(query)
    users = []
    for user in results:
        user.append( cls(user))    
    users_view_all.save(request.form)
    return render_template('read.html')

