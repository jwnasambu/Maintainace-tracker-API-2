from flask import unittest
import json
from app import app_config, app
from app.api.request.views import request_list
from app.api.user.views import users_list

class BaseTestCase(unittest.TestCase):
    def create_app(self):
        """
        Create an instance of the app with the testing configuration
        """
        app.config.from_object(app_config["testing"])
        return app

    def setUp(self):
        self.client = app.test_client("")
        # user_data = {
        #     "username": username,
        #     "email": email,
        #     "password":password
        # }

    def tearDown(self):
        """
        Drop the data structure data
        """
        users_list[:] = []
        request_list[:] = []

    

    def register_user(self, fullname, username, email, password):
        """
        Method for registering a user with dummy data
        """
        return self.client.post(
            'api/v1/auth/signup',
            data=json.dumps(dict(
                fullname=fullname,
                username=username,
                email=email,
                password=password
            )
            ),
            content_type='application/json'
        )

    # def login_user(self, username, password):
    #     """
    #     Method for logging a user with dummy data
    #     """
    #     return self.client.post(
    #         'api/v1/auth/login',
    #         data=json.dumps(
    #             dict(
    #                 username=username,
    #                 password=password
    #             )
    #         ),
    #         content_type='application/json'
    #     )

    # def get_token(self):
    #     """
    #     Returns a user token
    #     """
    #     response = self.login_user("odetta","pearls")
    #     data = json.loads(response.data.decode())
    #     return data['token']

    # def add_request(self, token, category, name, priority):
    #     """
    #     Function to create a request
    #     """
    #     return self.client.post(
    #         'api/v1/users/requests',
    #         data=json.dumps(
    #             dict(
    #                 category=category,
    #                 name=name,
    #                 priority=priority
    #             )
    #         ),
    #         content_type='application/json',
    #         headers=({"token": token})
    #     )
    # def get_requests(self, token):
    #     """
    #     function to return get
    #     """
    #     return self.client.get('api/v1/users/requests', headers=({"token": token}))

    # def get_one_request(self, token):
    #     """
    #     function to return get
    #     """
    #     return self.client.get('api/v1/users/requests/{}'.format(id), headers=({"token": token}))

    # def put_request(self, token, category, name, priority):
    #     """
    #     function to edit a request
    #     """
    #     return self.client.put('api/v1/users/requests/{}'.format(id),
    #                            data=json.dumps(dict(
    #                                category=category,
    #                                 name=name,
    #                                 priority=priority))
    #                          content_type='application/json', headers=({"token": token}))