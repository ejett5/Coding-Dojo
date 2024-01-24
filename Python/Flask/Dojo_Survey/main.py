from flask import Flask, render_template, redirect, session, request


app = Flask(__name__,template_folder='Template', static_folder='static') #need to have template_folder with template folder name for it to retrieve the index.html file
@app.route('/', methods =['GET','POST'])#
def home():
    session['Name'] = request.form['Name']
    session['Programming Language'] = request.form['Programming Language']
    session['Dojo Location'] = request.form['Dojo Location']
    return render_template('index.html')
    return redirect('/result/')
    # print(render_template('index.html')) #working on console debugger method to find fail points similar to console.log in js

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
        

# route for rendering submitted info
@app.route('/result/')
def process():
    return render_template('result.html')


if __name__ =='__main__':
    app.run(debug=True, port= 5000)