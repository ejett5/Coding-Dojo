from flask_app import app 
from flask import render_template, request, redirect, flash
from flask_app.models.email_class import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_email/')
def submission():
    data = {
        'email':request.form['email']
    }
    Email.submission(data)
    return redirect('emailList.html')

