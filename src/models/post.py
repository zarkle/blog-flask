"""Class definition for Post collection."""
from src.common.database import Database
from uuid import uuid4
from datetime import datetime


class Post():
    """Blog post."""

    def __init__(self, blog_id, title, content, author, date=datetime.utcnow(), _id=None):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        self._id = uuid4().hex if _id is None else _id

    def save_to_mongodb(self):
        """Save post to database. Grab post from self.json() method and insert into database."""
        Database.insert(collection='posts', data=self.json())

    def json(self):
        """Create JSON representation (key/value set) of the post."""
        return {
            '_id': self._id,
            'blog_id': self.blog_id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date,
        }

    @classmethod
    def from_mongo(cls, id):
        """Allows you to use `post.from_mongo(id)` to return the post that has the given id."""
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                    title=post_data['title'],
                    content=post_data['content'],
                    author=post_data['author'],
                    date=post_date['created_date'],
                    _id=post_data['_id'])

    @staticmethod
    def from_blog(_id):
        """Return all posts belonging to a specific blog."""
        return [post for post in Database.find(collection='posts', query={'blog_id': _id})]
