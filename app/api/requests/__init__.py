from flask import Blueprint
from flask_restful import Api
from .views import AddRequest, GetRequests

request = Blueprint('requests', __name__)
maintainance_api = Api(request)
maintainance_api.add_resource(AddRequest, '/api/v1/users/requests')
maintainance_api.add_resource(GetRequests, '/api/v1/users/requests')

