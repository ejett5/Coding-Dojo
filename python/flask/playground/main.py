from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
# @app.route('/play/<color>/<number>/') #working on stacking routes
def index():
    return "Hallo, Wie gehts? Microsoft technologie hasse mich ."


# # main route for homepage
@app.route('/home/')

def home():
    
    return render_template('index.html')

# make a page view that displays color boxes and repeats them
@app.route('/trials/<phrase>/<int:number>/')
# @app.route('/play/<x>/<y>')
def box_playground(phrase, number):
    return render_template('game.html', phrase = phrase, number = number)


@app.route('/play/')
@app.route('/play/<int:x>/<color>/')
# @app.route('/play/<x>/<y>')
def box_playground_render(x, color):
    return render_template('boxs.html', x = x, color = color)

# final line of code that runs the preceeding code
if __name__ == "__main__":
    app.run(debug=True, port= 8443)