from flask_app  import app
from flask_app.controllers import user





#closing statement to run all the routes
if __name__ == '__main__':
    app.run(debug=True, port=8443)