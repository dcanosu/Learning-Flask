from ast import Nonlocal
from flask import (
    Blueprint, render_template, request, url_for, redirect, flash, session, g
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

@bp.route("/login", methods = ("GET", "POST"))
def login():
    if request.method == "POST":
        username = request.form["username"].lower()
        password = request.form["password"]
                
        error = None
        # Validated user and password
        user = User.query.filter_by(username = username).first()
        if user == None:
            error = ("The user is incorrect")
        elif not check_password_hash(user.password, password):
            error = ("The password is incorrect")
        
        # Login
        if error is None:
            session.clear()
            session["user_id"] = user.id
            return redirect(url_for("todo.index"))

        flash(error)
    return render_template("auth/login.html")

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    
    if user_id is None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)
        
@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("index"))

import functools

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("auth.login"))
        return view(**kwargs)
    return wrapped_view