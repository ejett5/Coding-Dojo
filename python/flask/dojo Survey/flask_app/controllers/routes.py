from flask_app import app 
from flask import render_template, redirect, request, session, flash
from flask_app.models.dojos import Dojo 
from flask_app.models.ninjas import Ninjas 



@app.route('/')
def index():
    return "test complete. page loaded, please proceed to /home"

@app.route('/home/')
def home():
    return render_template('index.html')

@app.route('/process/', methods=['POST'])
def submit():
    session['Name'] = request.form['Name']
    session['Location'] = request.form['Location']
    session['Favorite_Language'] =  request.form['Favorite_Language']
    session['Comments'] = request.form['Comments']
    return redirect('/result/')

@app.route('/result/')
def result():
    return render_template('results.html')