from flask import render_template,session,redirect,url_for

from . import main
from .froms import NameFrom
from .. import db
from ..models import User

@main.route('/',method=['GET','POST'])
def index():
    return 