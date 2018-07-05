from flask import jsonify, make_response
from flask_restful import Resource, reqparse

import re
import json

from app.api.models.request import Request


request_list=[]
class AddRequest(Resource):
    id=0
    def post(self):
        """
        Method for adding requests
        """
        parser = reqparse.RequestParser()
        parser.add_argument('category', type=str, required=True)
        parser.add_argument('name', type=str, required=True)
        parser.add_argument('priority', type=str, required=True)
        args = parser.parse_args()
        category = args['category']
        name = args['name']
        priority= args['priority']
        if category.strip() == "" or len(category.strip()) < 2:
            return make_response(jsonify({"message": "category should be more than 2 letters"}), 400)

        if re.compile('[!@#$%^&*:;?><.0-9]').match(category):
            return make_response(jsonify({"message": "Invalid characters not allowed"}), 400)
        
        global id
        if len(request_list)==0:
            id = len(request_list)+1
        else:
            id = id+1

        new_request = Request(id, category, name, priority)

        for request in request_list:
            if category == request['category']:
                return make_response(jsonify({"message": 'Request category already exists'}), 400)
        request = json.loads(new_request.json())
        request_list.append(request)
        return make_response(jsonify({
            'message': 'Request successfully created and sent',
            'status': 'success'},
        ), 201)


class GetRequests(Resource):
    def get(self):
        """
        Returns all requests made for authenticated admin
        token is required to get admin id
        """
        parser = reqparse.RequestParser()
        parser.add_argument('token', location='headers')
        args = parser.parse_args()
        my_requests = []
        for request in request_list:
            requests_data = {
                    "id": request["id"],
                    "category": request['category'],
                    "name": request['name'],
                    "priority": request['priority']
                }
            my_requests.append(requests_data)
        if my_requests:
            return make_response(jsonify({"requests": my_requests,
                                    "status": "success"}), 200)
        return make_response(jsonify({"message": "No requests found"}), 404)

