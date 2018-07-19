import json

from .base import BaseTestCase

class Tests_Requests(BaseTestCase):
    """Test for requests"""
    def test_add_request_successfully(self):
        """Tests when the requests are submitted successfully"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = self.get_token()
            response = self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 201)
            self.assertEqual(data.get('message'), "Request successfully created and sent")
            res = self.add_request(self.get_token(), "Repair", "printer failed to pick papers from the tray", "moderate")
            data1 = json.loads(res.data.decode())
            self.assertEqual(res.status_code, 400)
            self.assertEqual(data1.get('message'), "Request title already exists")

    def test_get_all_requests(self):
        """Tests when all requests are retrieved successfully"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = self.get_token()
            self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
            response = self.get_requests(token)
            self.assertEqual(response.status_code, 200)

    def test_get_no_requests(self):
        """Tests when no requests are retrieved"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pe")
            token = self.get_token()
            self.add_request(token, "", "", "")
            response = self.get_requests(token)
            self.assertEqual(response.status_code, 404)

    def test_add_request_with_no_token(self):
        """Tests when the requests are submitted successfully"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = ""
            response = self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get('message'), "Token is missing")

    def test_gets_all_requests_with_no_token(self):
        """Tests when the no token is provided when getting requests """
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = ""
            self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
            response = self.get_requests(token)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get('message'), "Token is missing")

    def test_gets_all_requests_with_expired_token(self):
        """Tests when the token expires when retrieving requests"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = "aszdfvk."
            self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
            response = self.get_requests(token)
            self.assertEqual(response.status_code, 401)    
     
    def test_add_request_with_invalid_title(self):
        """Tests when the requests are submitted with short title"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = self.get_token()
            response = self.add_request(token, "R", "printer failed to pick papers from the tray", "moderate")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Title should be more than 2 letters")

    def test_add_request_with_title_with_character(self):
        """Tests when the requests are submitted with characters in title"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = self.get_token()
            response = self.add_request(token, "@", "printer failed to pick papers from the tray", "moderate")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 400)
            self.assertEqual(data.get('message'), "Invalid characters not allowed")

    # def test_get_one_request(self):
    #     """Tests when one request is retrieved successfully"""
    #     with self.client:
    #         self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
    #         token = self.get_token()
    #         self.add_request(Repair", "printer failed to pick papers from the tray", "moderate")
    #         response = self.get_one_request(token)
    #         self.assertEqual(response.status_code, 200)

    # def test_edit_request(self):
    #     """Tests when one request is edited successfully"""
    #     with self.client:
    #         self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
    #         token = self.get_token()
    #         self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
    #         response = self.put_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
    #         data = json.loads(response.data.decode())
    #         self.assertEqual(response.status_code, 201)
    #         self.assertEqual(data.get('message'), "request updated succesfully")

    def test_edits_requests_with_no_token(self):
        """Tests when the no token is provided when editing requests """
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = ""
            self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
            response = self.put_request(token, "Repair", "printer failed to pick papers from the tray", "item")
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get('message'), "Token is missing")

    def test_edits_requests_with_expired_token(self):
        """Tests when the expired token is provided when editing requests """
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = "zaxdchk"
            self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
            response = self.put_request(token, "Repair", "printer failed to pick papers from the tray", "item")
            self.assertEqual(response.status_code, 401)

    def test_get_one_request_with_no_token(self):
        """Tests when one request is retrieved with no token"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "12345")
            token = ""
            self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
            response = self.get_one_request(token)
            data = json.loads(response.data.decode())
            self.assertEqual(response.status_code, 401)
            self.assertEqual(data.get('message'), "Token is missing")

    def test_get_one_request_with_expired_token(self):
        """Tests when one request is retrieved with expired token"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = "zxcvb"
            self.add_request(token, "Repair", "printer failed to pick papers from the tray", "moderate")
            response = self.get_one_request(token)
            self.assertEqual(response.status_code, 401)

    def test_get_no_request_by_id(self):
        """Tests when a request is not found by id"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = self.get_token()
            self.add_request(token, "", "", "")
            response = self.get_one_request(token)
            self.assertEqual(response.status_code, 404)

    def test_edit_no_request_by_id(self):
        """Tests when no request is found by id when editing"""
        with self.client:
            self.register_user("Odetta Kale", "odetta", "odettak@gmail.com", "pearls")
            token = self.get_token()
            self.add_request(token, "", "", "")
            response = self.put_request(token, "Repair", "printer failed to pick papers from the tray", "item")
            self.assertEqual(response.status_code, 404)