from flask import Flask, render_template


app = Flask(__name__)

# main route for homepage
@app.route('/')
def index():
    return render_template("index.html")



# final line of code that runs the preceeding code
if __name__ == "__main__":
    app.run(debug=True, localhost = 8443)