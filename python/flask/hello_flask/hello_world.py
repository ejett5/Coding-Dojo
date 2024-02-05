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
@app.route('/say/<string:name>')
def say(name):
    return f'Hi, {name}'


#returns repeats message stated number of times on page
@app.route('/repeat/<string:name>/<int:num>')
def repeat(name, num):
    return(f'{name}\n'*num)


if __name__== "__main__":
    app.run(debug = True, host="localhost", port = '8443')


