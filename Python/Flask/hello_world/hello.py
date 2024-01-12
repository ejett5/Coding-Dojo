from flask import Flask
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World'
if __name__ =="__main__":
    app.run(debug=True, host = "localhost", port = 8443)

@app.route('/Dojo')
    def Dojo(dojo):
    print(Dojo)
    return "Dojo!"
# says hi to entered name
@app.route('/Hi/<name>')
    def Hi(name):
    return f"Hi, "+ <name>

# route that handles name and number inputes
@app.route('/hello/<name>/<int:num>')
def hello(name,num):
    return f"Hello, {name * num}"

#examples of individual routes for potential entries
# @app.route('/say/flask')
#     def say(flask):
#     return f"Hi Flask!"

# @app.route('/say/Michael')
#     def say(Michael):
#     return f"Hi Michael!"

# @app.route('/say/flask')
#     def say(flask):
#     return f"Hi Flask!"