from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/index")
def inex():
    return ("<h1>This is the index page!<h1>")

# @app.route("/hello")
# def hello():
#     return ("<h1>Hello world !<h1>")

# @app.route("/hello/<string:name>/<int:age>")
# def hello_name(name, age):
#     return (f"<h1>Hello {name} y tu edad es {age}!<h1>")

@app.route("/hello")
@app.route("/hello/<string:name>")
@app.route("/hello/<string:name>/<int:age>")
def hello_name(name = None, age = None):
    if name == None and age == None:
        return ("<h1>Hello world !<h1>")
    elif age == None:
        return (f"<h1>Hello {name}!<h1>")
    else:
        return (f"<h1>Hello {name} y tu edad es {age}!<h1>")

from markupsafe import escape
@app.route("/code/<path:code>")
def code(code):
    return (f"<code>{escape(code)}<code>")
