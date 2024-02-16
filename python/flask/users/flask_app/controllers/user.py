from flask_app import app 
from flask import render_template,redirect, request, session, flash
from flask_app.models.user_lookup import User 


# landing page for users website
@app.route('/')
def index():
    return render_template('index.html')

# retrieving users and displaying the information
@app.route('/view_users/')
def users_view_all():
    users_view_all.save(request.form)
    return render_template('read.html')

