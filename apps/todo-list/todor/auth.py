from flask import Blueprint

bp = Blueprint("auth", __name__, url_prefix="/auth")

@bp.route("/register")
def register():
    return "Sign up an usert"

@bp.route("/login")
def login():
    return "login"