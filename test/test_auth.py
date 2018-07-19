import json

from test.base import BaseTestCase


class Test_auth(BaseTestCase):
    def test_successful_signup(self):
        """
        Test a user is successfully created through the api
        """
        with self.client:
            response = self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "User successfully created")
            # Add the same user and see...
            res = self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            data1 = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertEqual(data1.get('message'), "email already in use")

   