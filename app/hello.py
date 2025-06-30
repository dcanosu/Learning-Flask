from flask import Flask, render_template, url_for

app = Flask(__name__)

# Personalaize filter
@app.add_template_filter
def today(date):
    return date.strftime("%d-%m-%Y")
# app.add_template_filter(today, "today")

# Personalize function
@app.add_template_global
def repeat(phrase, times):
    return phrase * times

from datetime import datetime

@app.route("/")
# @app.route("/index")
def index():
    print(url_for("index"))
    print(url_for("hello", name = "Alex", age = 27))
    print(url_for("code", code = "print('Hello')"))
    name = "Daniel"
    friends = ["Alexander", "Carlos", "Camilo", "Juan"]
    date = datetime.now()
    return render_template(
        "index.html", 
        name = name, 
        friends = friends, 
        date = date,
        # repeat = repeat
    )

@app.route("/hello")
@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/<int:age>")
@app.route("/hello/<string:name>/<int:age>/<email>")
def hello(name = None, age = None, email = None):
    my_data = {
        "name": name,
        "age": age,
        "email": email
    }
    return render_template("hello.html", data = my_data)
    
from markupsafe import escape

@app.route("/code/<path:code>")
def code(code):
    return (f"<code>{escape(code)}<code>")
