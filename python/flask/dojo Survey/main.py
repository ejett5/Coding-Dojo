from flask import Flask, render_template, redirect


app = Flask(__name__)

@app.route('/')
def index():
    return "test complete. page loaded, please proceed to /home"

@app.route('/home/')
def home():
    return render_template('index.html')

@app.route('/process/', methods = ['POST'])
def submit():
    return redirect('/results.html')


# final line to execute code
if __name__ == '__main__':
    app.run(debug=True)