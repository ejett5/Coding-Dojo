from flask_app import app 
from flask_app.models.players_classes import Player
from flask import redirect, render_template, request, session, flash





# landing page to take user login or register
@app.route('/')
def index():

    return render_template('index.html')

# dashboard page for user when they login
@app.route('/home/') #TODO why is method not alloweed when there is no method? GET is default and the one needed to view info
def view_player():
    # insert validation check that user is logged in and session still valid
    if 'email' not in session:
        flash('Please sign in')
        return redirect('/')
    
    

    one_player = Player.GetUserById({'id': session['player_id'] })

    
    return render_template('dashboard.html', one_player=one_player)


# player registration and redirect to dashboard
@app.route('/register/', methods = ['POST']) #TODO figure out why not reading from DB
def CreatePlayer():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email' : request.form['email'],
        'password' : request.form['password']
    }
    Player.create_player(data)
    return redirect('/dashboard/') 


# login route
@app.route('/login/', methods = ['POST'])
def login():

    return redirect ('/dashboard/')


# route to view player information
@app.route('/dashboard/')   
def player_dash():
    

    one_player = Player.view_player()

    return render_template('dashboard.html', one_player=one_player)