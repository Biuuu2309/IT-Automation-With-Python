# This is not an excutable code block
from flask import Flask

app = Flask("myapp")

@app.route('/')
def hello_world():
    return 'Hello, World!'


from flask import Flask

app = Flask("hello")

@app.route('/hello/<name>')
def hello_world(name):
    return f'Hello, {name}!'