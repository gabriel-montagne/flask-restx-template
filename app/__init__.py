from flask_restx import Api
from flask import Blueprint

from .main.controller.user_controller import api as user_ns
from .main.controller.user_role_controller import api as user_role_ns
from .main.controller.auth_controller import api as auth_ns

blueprint = Blueprint('api', __name__, url_prefix='/api')

api = Api(
    blueprint,
    title='OGRE WIND SOLAR RESTX API',
    version='1.0',
    description='a flask restx api web service',
    doc='/doc/'
)

api.add_namespace(user_ns, path='/api/user')
api.add_namespace(user_role_ns, path='/api/user_role')
api.add_namespace(auth_ns, path='/api/auth')
