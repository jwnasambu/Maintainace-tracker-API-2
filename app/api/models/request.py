import uuid
import json


class Request:
    # constructor which initialises the whole class
    def __init__(self, id, category, name, priority):
        self.id = id
        self.category= category
        self.name = name
        self.priority = priority

    def json(self):
        """
        json representation of the Request model
        """
        return json.dumps({
            'id': self.id,
            'category': self.category,
            'name': self.name,
            'priority':self.priority
        })