from flask import Flask, render_template, url_for, redirect 


app = Flask(__name__)

@app.route("/")
def index():
    return redirect('/page0')

@app.route("/page<index>")
def page(index):
    return render_template('page_template.html', title = index, page_number=index)

