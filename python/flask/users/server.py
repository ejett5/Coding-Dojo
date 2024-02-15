from flask_app  import app

@app.route('/')
def index():
    return render_template('index.html')



#closing statement to run all the routes
if __name__ == '__main__':
    app.run(debug=True, port=8443)