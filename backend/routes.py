# Extra end point
from . import api
from .api import UserResource

api.add_resource(UserResource, '/api/user', '/api/user/<int:id>')