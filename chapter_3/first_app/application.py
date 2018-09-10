from flask import  Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>hworld!</h1>"

#respond to variable address
@app.route('/name/<specific_name>')
def name(specific_name):
    return specific_name 

