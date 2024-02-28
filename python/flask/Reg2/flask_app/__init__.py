from flask import Flask

app = Flask(__name__)
app.secret_key = 'root'

# DataBase name change per project (CHECK DB NAME!)
DB = 'login_and_registration'

print('Flask app spinned up successefully!')
