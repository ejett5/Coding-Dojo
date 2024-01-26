from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import connectToMySQL  #the from statement is the module being imported(also able to import another file for sql connection)



app = Flask(__name__) #need to have template_folder with template folder name for it to retrieve the index.html file
@app.route('/', methods =['GET'])#need to have logic to access get and post, especially when combined
def index():
    return render_template('index.html')
    # print(render_template('index.html')) #working on console debugger method to find fail points similar to console.log in js

@app.route('/', methods = ['POST'])
def home():
    session['Name'] = request.form['Name']
    session['Programming Language'] = request.form['Programming Language']
    session['Dojo Location'] = request.form['Dojo Location']
    return render_template('index.html')
    return redirect('/result/')

#creating class to hold the survey results
class Survey_Results:
    DB = "Local instance MySQL83"
    def __init__(self, data):
        self.id = data[id]
        self.Name = data['Name']
        self.Location = data['Location']
        self.Language = data['Favorite Language']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

# adding more results to the survey
@app.route('/result/add_new/')
def add_new():
    query = """ INSERT into {table name} (Name, Location, Favorite Language, Comments)
            VALUES(%(Name)s,%) """
    return render_template('index.html/result/add_new/')

# route for rendering submitted info
@app.route('/Survey_Results/')
def process():
    return render_template('result.html')


#making form validation 
# class thing:
# @staticmethod
# def validate_users(thing):
#     is_valid = Trueif len(users['first_name']) < 3:
#         flash("name must be a minimum of 3 characters.")
#         is_valid = False
#     is_valid = Trueif len(users['last_name']) < 3:
#         flash("name must be a minimum of 3 characters.")
#         is_valid = False
#     is_valid = Trueif len(users['email']) < 3:
#         flash("must be a minimum of 3 characters.")
#         is_valid = False
#     return is_valid


if __name__ =='__main__':
    app.run(host = '0.0.0.0' ,debug=True, port= 5000)