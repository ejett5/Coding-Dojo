from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
if __name__ =="__main__":

    app.run(debug=True, host = "localhost", port = 8443)

#adding another route to the server
@app.route('/hello/<name>')
#passing variable of name
def hello(name):
    print(name)
    return "Hello, " + name