"""User model."""
import uuid
from src.common.database import Database


class User:
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid4().hex if not _id else _id

    @classmethod
    def get_by_email(cls, email):
        """Find if user exists in database."""
        data = Database.find_one('users', {'email': self.email})
        if data:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        data = Database.find_one('users', {'_id': self._id})
        if data:
            return cls(**data)

    def login_valid(self):
        pass

    def registerself):
        pass

    def login(self):
        pass

    def get_blogs(self):
        pass

    def json(self):
        pass

    def save_to_mongo(self):
        pass
