from os import error
from pyclbr import Class
from flask import Flask, render_template, url_for, request

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = "dev"
)

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

# Register
@app.route("/auth/register", methods = ["GET", "POST"])
def register():
    # print(request.form) we can see the information that the user register in the form
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
            return f"username: {username} | password: {password}"
        else:
            error = """
            Username must be between 4 and 25 characters long.
            Password must be between 6 and 40 characters long.
            """
            return render_template("auth/register.html", error = error)
    return render_template("auth/register.html")

# Create a form using wtform
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length

class RegisterForm(FlaskForm):
    # username = StringField("Username: ")
    username = StringField("Username: ", validators= [DataRequired(), Length(min=4, max=25)])
    password = PasswordField("Password: ", validators= [DataRequired(), Length(min=4, max=25)])
    submit = SubmitField("Register")
    
# Register using wtf
@app.route("/auth/register/wtf", methods = ["GET", "POST"])
def register_wtf():
    form = RegisterForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        return f"username: {username} | password: {password}"
    # if request.method == "POST":
    #     username = request.form["username"]
    #     password = request.form["password"]
        
    #     if len(username) >= 4 and len(username) <= 25 and len(password) >= 6 and len(password) <= 40:
    #         return f"username: {username} | password: {password}"
    #     else:
    #         error = """
    #         Username must be between 4 and 25 characters long.
    #         Password must be between 6 and 40 characters long.
    #         """
    #         return render_template("auth/register-wtf.html", form = form, error = error)
    return render_template("auth/register-wtf.html", form = form)