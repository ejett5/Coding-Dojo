from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def greetings():
    return f'Welcome! This is the base loading test page.'

users= [
    {'first_name': 'Michael', 'last_name' : 'Choi'},
    {'first_name': 'John', 'last_name' : 'Supsupin'},
    {'first_name': 'Mark', 'last_name' : 'Guillen'},
    {'first_name': 'KB', 'last_name' : 'Tonel'},
]

#pulling user table info
@app.route('/form/', methods=['GET', 'POST'])
def html_table():    
    # return users
    # if request.method == "POST":
    return render_template('index.html')  # can put an if loop here if using a login page in the future   
    # else:
    #     return "Pardon the dust. This page is still under construction."


@app.route("/<user>")
def user(name):
    return f"{name}, Welcome Back!"



if __name__ =="__main__":
    app.run(debug=True)