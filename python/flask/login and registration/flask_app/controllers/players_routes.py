from flask_app import app 
from flask_app.models.players_classes import Player
from flask import redirect, render_template, request, session, flash





# landing page to take user login or register
@app.route('/')
def index():

    return render_template('index.html')

# dashboard page for user when they login
@app.route('/home/')
def view_player():
    # insert validation check that user is logged in and session still valid
    
    one_player = Player.view_player()
    return render_template('dashboard.html')









#! context processor function that retrieves the flash messages
#! Context processor makes flash messages available in all templates
# @app.context_processor
# def inject_flash_messages():
#     messages = get_flashed_messages()
#     return dict(messages=messages)
#? I don't need to explicitly pass flash messages to each template rendering call in your routes.
#? The messages variable will be available globally in all templates.