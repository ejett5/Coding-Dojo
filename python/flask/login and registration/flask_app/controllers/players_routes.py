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
    if 'email' not in session:
        flash('Please sign in')
        return redirect('/')
    

    one_player = Player.GetUserById({'id': session['player_id'] })

    one_player = Player.view_player()
    return render_template('dashboard.html', one_player=one_player)

@app.route('/register/', methods = ['POST'])
def CreatePlayer():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password']
    }
    Player.create_player(data)
    return redirect('/home/')












#! context processor function that retrieves the flash messages
#! Context processor makes flash messages available in all templates
# @app.context_processor
# def inject_flash_messages():
#     messages = get_flashed_messages()
#     return dict(messages=messages)
#? I don't need to explicitly pass flash messages to each template rendering call in your routes.
#? The messages variable will be available globally in all templates.