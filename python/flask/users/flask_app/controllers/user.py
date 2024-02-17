from flask_app import app 
from flask import render_template,redirect, request, session, flash
from flask_app.models.user_lookup import User 



# landing page for users website
@app.route('/')
def index():
    return render_template('index.html')

# making users for the table
@app.route('/user_form')
def user_form():
    return render_template('submit_profile.html')

@app.route('/submit_profile/', methods=['POST'])
def create_user():
    data = {
        'first_name': request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    User.create_user(data)
    return redirect('/read.html/')


# retrieving users and displaying the information
@app.route('/view_users/')
def view_users():
    all_users = User.view_user()
    return render_template('read.html', all_users=all_users)

