from flask import Flask, render_template, request
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index_template.html')

@app.route('/calculate', methods = ['POST', 'GET'])
def calculate_fibonacci():
    error = None
    if request.method == 'POST':
        number_request = int(request.form['number_request'])
        calculated_value, time = fib_helper(number_request) 
        return '<h1> The value is {} <br> It took {:.5} second to process your request'.format(calculated_value, time)
    else:
        return 'oops!! you were not meant to be here on your own'
    return error

def fib_helper(n):
    start = time.time()
    calc = fib(n)
    stop = time.time()
    return (calc, stop-start)

def fib(n):
    if n<3:
        return 1
    return fib(n-1) + fib(n-2)


