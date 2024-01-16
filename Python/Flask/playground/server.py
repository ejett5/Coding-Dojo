from flask import Flask

app = Flask(__name__)

# import statements, maybe some other routes
    
@app.route('/')
def success():
  return "success"
    
    # app.run(debug=True) should be the very last statement! 

#allow app to run blue box and set number of boxes to display

#allow user to change color of boxes as well
