#main python routing file

from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = ''

#route to verify functionality
@app.route('/test')
def test():
    return "Congrats the page loaded successfully! Now try '/Home/' "

#counter for user visits
@app.route('/counter/', methods=['POST'])
def counter():
    print("Users session visits")
    #here goes the info for tracking user visits
    return redirect('/Welcome')

#destroys users cookies
@app.route('/reset/', methods=['POST'])
def exterminate():
    return "The Doctor is no more"



#last section to run the code
app.run()