from flask import Flask

app = Flask(__name__)
app.secret_key = 'rootroot'

# DataBase name change per project (CHECK DB NAME!)
DB = 'loot_sellerDB'

print('Flask app spinned up successefully!')
