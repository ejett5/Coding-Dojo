from flask import Flask

app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

#returns Hi Flask on page
@app.route('/flask')
def flask():
    return 'Hi Flask!'


#returns Hi and given name on page
@app.route('/say/{name}')
def say():
    return 'Hi {name}'



if __name__== "__main__":
    app.run(debug = True, host="localhost", port = '8443')


