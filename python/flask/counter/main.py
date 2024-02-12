from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "underwear"

@app.route('/')
def index():
    if "count" not in session: #making a way to count and see if that method is not in the session
        session['count'] = 0  #initialise session to the count
    session['count'] += 1
    return render_template('index.html')

# destroy the users session cookies info reseting the browser counter
@app.route('/destroy_session')
def destroy():
    session.clear()
    # session.pop("underwear")
    return redirect ('/')


#add to the session counter
@app.route('/increment')
def increment():
    if "count" not in session: #making a way to count and see if that method is not in the session
        session['count'] = 0  #initialise session to the count
    session['count'] += 2
    return render_template ('/')
    



if __name__ == '__main__':
    app.run(debug = True, port = 443)