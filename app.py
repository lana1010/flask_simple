import click
from flask import Flask, render_template


app = Flask(__name__)
#app = Flask(static_folder='C:\\Programming\\Git\\flask_simple\\templates\\static')

@app.route("/")
def home():
    return "Welcome to the Home Page!"

@app.route("/hi")
@app.route("/hello")
def say_hello():
    return render_template("index.html")

# dynamic route, URL variable default
@app.route('/greet', defaults={'name': 'Programmer'})
@app.route('/greet/<name>')
def greet(name):
    return '<h1>Hello, %s!</h1>' % name

# custom flask cli command
@app.cli.command()
def hello():
    """Just say hello."""
    click.echo('Hello, Human!')

if __name__ == "__main__":
    app.debug = True
    app.run()    