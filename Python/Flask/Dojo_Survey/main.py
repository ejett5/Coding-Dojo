from flask import Flask, render_template, redirect, session, request, flash
from mysqlconnection import connectToMySQL  #the from statement is the module being imported(also able to import another file for sql connection)
from survey import Survey


app = Flask(__name__) #need to have template_folder with template folder name for it to retrieve the index.html file
@app.route('/', methods =['GET'])#need to have logic to access get and post, especially when combined
def index():
    return render_template('index.html')
    # print(render_template('index.html')) #working on console debugger method to find fail points similar to console.log in js


@app.route('/result/add_new', methods = ['POST'])
def add_new():
    Survey.save(request.form)
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')


@classmethod
def get_all(cls):
    query = "SELECT * FROM dojo_survey"











if __name__ =='__main__':
    app.run(host = '0.0.0.0' ,debug=True, port= 5000)