from flask import Flask, render_template
from players import users

app = Flask( __name__ )

@app.route('/')
def home():
    return render_template('index.html')





if __name__ == "__main":
    app.run(debug = True, port = 443)