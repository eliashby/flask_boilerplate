from flask import Blueprint


bp = Blueprint('modules', __name__)

from app.modules import *
