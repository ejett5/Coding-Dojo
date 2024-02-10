from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = "underwear"

@app.route('/')
def index():
    # session[''] = session ['']
    return render_template('index.html')

# destroy the users session cookies info reseting the browser counter
@app.route('/destroy_session')
def destroy():
    session.clear()
    session.pop('underwear')
    redirect ('/')



if __name__ == '__main__':
    app.run(debug = True, port = 443)