from flask_app import app 
from flask_app.controllers import routes




# final line to execute code
if __name__ == '__main__':
    app.run(debug=True, port= 8443, host='0.0.0.0')