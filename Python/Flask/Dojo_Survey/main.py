from flask import Flask, render_template, redirect

app = Flask(__name__,template_folder='Template') #need to have template_folder with template folder name for it to retrieve the index.html file
@app.route('/')
def home():
    return render_template('index.html')
    # print(render_template('index.html')) #working on console debugger method to find fail points similar to console.log in js

if __name__ =="__main__":
    app.run(debug=True, port= 5000)