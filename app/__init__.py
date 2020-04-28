"""
Main documentation for this module
"""
from flask_restplus import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.user_role_controller import api as user_role_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint,
          title='FLASK RESTPLUS API',
          version='1.0',
          description='a flask restplus web service'
          )

api.add_namespace(user_ns, path='/api/user')
api.add_namespace(user_role_ns, path='/api/user_role')
api.add_namespace(auth_ns, path='/api/auth')
