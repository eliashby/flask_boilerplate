from flask import render_template, request
from app.main import bp
import json


@bp.route('/')
def index():
    return render_template('index.html', title='Home')
