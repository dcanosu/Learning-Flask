from flask import (
    Blueprint, render_template, request, url_for, redirect, flash
    )

from flask.cli import F
from werkzeug.security import generate_password_hash, check_password_hash

# from . import models
from .models import User
from todor import db

bp = Blueprint("auth", __name__, url_prefix="/auth")

# @bp.route("/register")
@bp.route("/register", methods = ("GET", "POST"))
def register():
    if request.method == "POST":
        username = request.form["username"].lower()
        password = request.form["password"]
        
        user = User(username, generate_password_hash(password))
        
        error = None
        user_name = User.query.filter_by(username = username).first()
        if user_name == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("auth.login"))
        else:
            error = (f"The user {username} is already use")
        flash(error)
        
    return render_template("auth/register.html")

@bp.route("/login")
def login():
    return render_template("auth/login.html")