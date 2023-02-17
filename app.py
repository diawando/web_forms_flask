from flask import Flask, render_template, request, url_for, flash, redirect

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your secret key'



messages = [{
    'title' : 'Message One',
    'content' : 'Message one content'
    },
    {
    'title': 'Message Two',
    'content': 'Message Two Content'
    }
    ]

@app.route('/')
def index():
    return render_template('index.html', messages=messages)

@app.route('/create/', methods=('GET', 'POST'))
def create():
    return render_template('create.html')