from flask_app import app 
from flask_app.models.players_classes import Player
from flask import redirect, render_template, request, session, flash

# landing page to take user login or register
@app.route('/', methods=['POST'])
def index():
    return render_template('index.html')

# dashboard page for user when they login
@app.route('/home/')
def view_player():
    one_player = Player.view_player()
    return render_template('dashboard.html')

@app.route('/placeholder/')
def temp():