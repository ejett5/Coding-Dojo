from flask import app 
from flask_app.controllers import player 



if __name__ == "__main__":
    app.run(debug=True, port = 8443)