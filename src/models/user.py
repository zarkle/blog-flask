"""User model."""
import uuid
from datetime import datetime
from src.common.database import Database
from .blog import Blog


class User:
    def __init__(self, email, password, _id=None):
        self.email = email
        self.password = password
        self._id = uuid4().hex if not _id else _id

    @classmethod
    def get_by_email(cls, email):
        """Find if user exists in database by email."""
        data = Database.find_one('users', {'email': email})
        if data:
            return cls(**data)

    @classmethod
    def get_by_id(cls, _id):
        """Find if user exists in database by id."""
        data = Database.find_one('users', {'_id': self._id})
        if data:
            return cls(**data)

    @classmethod
    def login_valid(cls, email, password):
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
            session['email'] = email
            return True
        else:  # user already exists; TODO: add feedback as to why registration failed
            return False

    @staticmethod
    def login(user_email):
        # login_valid has already been called
        session['email'] = user_email

    @staticmethod
    def logout():
        session['email'] = None

    def get_blogs(self):
        return Blog.find_by_author_id(self._id)

    def new_blog(self):
        blog = Blog(author=self.email,
                    title=title,
                    description=description,
                    author_id=self._id)

        blog.save_to_mongo()

    @staticmethod
    def new_post(title, content, date=datetime.utcnow()):
        blog = Blog.from_mongo(blog_id)
        blog.new_post(title=title,
                      content=content,
                      date=date)


    def json(self):
        return {
            'email': self.email,
            '_id': self._id,
            'password': self.password  # not encrypted yet
        }

    def save_to_mongo(self):
        Database.insert('users', self.json())
