from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def index():
    return "Hallo, Wie gehts? Microsoft technologie hasse mich ."


# # main route for homepage
@app.route('/home/')
# @app.route('/play/<color>/<number>/')
def home():
    return render_template('index.html')

# make a page view that displays color boxes and repeats them
@app.route('/play/<phrase>/<int:number>/')
# @app.route('/play/<x>/<y>')
def box_playground(phrase, number):
    return render_template('game.html', phrase = phrase, number = number)

# final line of code that runs the preceeding code
if __name__ == "__main__":
    app.run(debug=True, port= 8443)