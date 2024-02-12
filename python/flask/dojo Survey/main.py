from flask import Flask, render_template, redirect, session


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

@app.route('/result/')
def result():
    return render_template('results.html')


# final line to execute code
if __name__ == '__main__':
    app.run(debug=True, port= 8443, host='0.0.0.0')