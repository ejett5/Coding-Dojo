#main python routing file

from flask import Flask, render_template, request, redirect, session, make_response
# from fastapi import Response    

app = Flask(__name__)
app.secret_key = ''

#TODO discover why str has no attribute for set_cookie, (https://www.pythonanywhere.com/forums/topic/28590/) had similar issue and caused by not having attribute table
@app.route('/')
def basic():
    count = int(request.cookies.get('basic', 0))
    count = count+1
    output = "You've visited the page " +str(count) + 'times!'
    resp = 'make_response(output)'
    resp.set_cookie('basic', str(count))
    return resp

#TODO why is the return not recognised when hosting?
#pulling cookie data
@app.route('/get/')
def get_visitors_count():
    count = request.cookies.get('basic')
    return count


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

#create cookies
@app.route('/setcookie')
def setcookie():
    #initializing response object
    resp = 'make_response'('Setting Cookie')
    resp.set_cookie('GFG', 'ComSci Portal') #here the response for the getcookie is set and the second value is the argument to be passed when called later(can be used to call another route or temp?)
    return resp

@app.route('/getcookie')
def getcookie():
    GFG = request.cookies.get('GFG')
    return 'GFG is a '+ GFG

#destroys users cookies
@app.route('/reset/', methods=['POST'])
def exterminate():
    count = basic * 0
    return "The Doctor is no more"



#last section to run the code
app.run(debug =True)