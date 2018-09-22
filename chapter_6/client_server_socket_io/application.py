from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)


vote_count = {'yes_count'  : 0, 
              'no_count'   : 0,
              'maybe_count': 0}



@app.route('/')
def index():
    return render_template('index.html', **vote_count)

@app.route('/submit', methods=['post', 'get'])
def submit():
    response = request.form['vote'];
    if response == 'yes':
        vote_count['yes_count'] += 1
    elif response == 'no':
        vote_count['no_count'] += 1
    else:
        vote_count['maybe_count'] += 1
    
    return 'vote successful'
