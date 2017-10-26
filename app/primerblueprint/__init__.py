from flask import Blueprint
primerblueprint = Blueprint('primerblueprint',__name__,template_folder='templates')
from . import routes