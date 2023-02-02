import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash



bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route("/signup", methods = ("GET", "POST"))
def signup():
    ...
    return {"status": "Success"}

@bp.route("/login", methods=("GET", "POST"))
def login():


    return {"status": "success"}
