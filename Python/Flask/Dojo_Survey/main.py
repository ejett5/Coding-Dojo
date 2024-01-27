from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import connectToMySQL #the from statement is the module being imported(also able to import another file for sql connection)
from survey import Survey


app = Flask(__name__) #need to have template_folder with template folder name for it to retrieve the index.html file
@app.route('/', methods =['GET'])#need to have logic to access get and post, especially when combined
def index():
    return render_template('index.html')
    # print(render_template('index.html')) #working on console debugger method to find fail points similar to console.log in js


@app.route('/result/add_new', methods = ['POST'])
def add_new():
    Survey.save(request.form)
    return redirect('/result/')

@app.route('/result/')
def result():
    return render_template('result.html')


@classmethod
def get_all(cls):
    query = "SELECT * FROM dojo_survey_schema WHERE id = %(id)s;"
    results = connectToMySQL(cls.DB).query_db(query)
    Survery = []
    for [id] in Survey:
        id.append( cls(Survey) )
    return Survey


# validating 

import re	# the regex module
# create a regular expression object that we'll use later   
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 
class User:
    @staticmethod
    def validate_user( user ):
        is_valid = True
        # test whether a field matches the pattern
        if not EMAIL_REGEX.match(user['email']): 
            flash("Invalid email address!")
            is_valid = False
        return is_valid


# @app.route('/login', methods=["POST"])
# def login():
#     data = {
#         "email" : request.form['email'],
#         "password" : request.form['password']
#     }
#     if not User.validate_login(data):
#         return redirect('/')
#     user_in_db = User.get_by_email(data)
#     if not user_in_db:
#         flash('Invalid Email and/or Password')
#         return redirect('/')
#     if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
#         flash('Invalid Email and/or Password')
#         return redirect('/')
#     session['user_id'] = user_in_db.id
#     return redirect('/dashboard')
# #home page=>after login
# @app.route('/home')
# def home():
#     #check for session
#     if 'user_id'not in session:
#         return redirect('/')
#     else:
#         return render_template('home.html')


# #register page to get account.
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     print(request.form)

# **password**
#     hashed_pw= bcrypt.generate_password_hash(request.form['password'])
#     print(hashed_pw)
#     print(bcrypt.check_password_hash(hashed_pw, 'password'))

# **login to db*
#     temp_reg = {
#         'first_name' : request.form['first_name'],
#         'last_name' : request.form['last_name'],
#         'email' : request.form['email'],
#         'password' : hashed_pw
#     }

#     user = User.save(temp_reg)
#     print(user)


#     # ***SESSION**
#     session['user_id'] = user
#     session ['first_name'] = request.form['first_name']
#     session['last_name'] = request.form['last_name']

#     return redirect('/home')









if __name__ =='__main__':
    app.run(host = '0.0.0.0' ,debug=True, port= 5000)