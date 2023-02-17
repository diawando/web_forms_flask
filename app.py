from flask import Flask, render_template    

app = Flask(__name__)

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