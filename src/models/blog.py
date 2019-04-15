"""Blog class."""
from uuid import uuid4
from datetime import datetime
from post import Post
from database import Database

blog = Blog(author='Joe', title='Some title', description='stuff and things')

blog.new_post()

blog.save_to_mongo()

Blog.get_from_mongo()

blog.get_posts()


class Blog():
    def __init__(self, author, title, description, _id=None):
        self.author = author
        self.title = title
        self.description = description
        self._id = uuid4().hex if _id is None else _id

    def new_post(self):
        title = input('Enter post title: ')
        content = input('Enter post content: ')
        date = input('Enter post date (DDMMYY) or leave blank for today: ')
        if date == '':
            date = datetime.datetime.utcnow()
        else:
            datetime.strptime(date, '%d%m%Y')
        post = Post(blog_id=self._id,
                    title=title,
                    content=content,
                    author=self.author
                    date=date)
        post.save_to_mongo()

    def get_posts(self):
        return Post.from_blog(self._id)

    def save_to_mongo(self):
        Database.insert(collection='blogs', data=self.json())

    def json(self):
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            '_id': self._id
        }

    @classmethod
    def from_mongo(cls, id):
        blog_data = Database.find_one(collection='blogs', query={'_id': id})
        return cls(author=blog_data['author'],
                    title=blog_data[''],
                    description=blog_data['description'],
                    _id=blog_data['_id'])
