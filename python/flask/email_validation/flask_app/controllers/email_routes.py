from flask_app import app 
from flask import render_template, request, redirect, flash
from flask_app.models.email_class import Email

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_email/', methods = ['POST'])
def submission():
    data = {
        'email':request.form['email']
    }
    Email.submit_email(data)
    return redirect('emailList.html')

@app.route('/view_emails/')
def view_emails():
    all_emails = Email.submit_email()
    return render_template('emailList.html', all_emails = all_emails)