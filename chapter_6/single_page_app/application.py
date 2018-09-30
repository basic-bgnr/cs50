from flask import Flask, render_template, url_for, redirect 


app = Flask(__name__)

pages = ["This is a content for page 1",
        "This might not be content for page 1 but for page 2"]




@app.route("/")
def index():
    return render_template('master_page_template.html')

@app.route("/page/<page_number>")
def page(page_number):
    page_number = int(page_number) - 1
    return pages[page_number] 
