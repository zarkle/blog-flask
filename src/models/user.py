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
        """Find if user exists in database by email."""
        data = Database.find_one('users', {'email': self.email})
        if data:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        """Find if user exists in database by id."""
        data = Database.find_one('users', {'_id': self._id})
        if data:
            return cls(**data)

    @classmethod
    def login_valid(email, password):
        """
        Verify user is logged in by entering correct password.
        User.login_valid("email@email.com", "password")
        """
        user = cls.get_by_email(email)
        if user:
            # check the password
            return user.password == password
        return False  # user doesn't exist

    @classmethod
    def register(cls, email, password):
        """Register a new user."""
        user = cls.get_by_email(email)
        if user:
            new_user = cls(email, password)
            new_user.save_to_mongo
            return True
        else:  # user already exists; TODO: add feedback as to why registration failed
            return False

    def login(self):
        pass

    def get_blogs(self):
        pass

    def json(self):
        pass

    def save_to_mongo(self):
        pass