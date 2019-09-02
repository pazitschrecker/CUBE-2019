from datetime import datetime
from flaskblog import db

# create User class (inherits from db.model)
class User(db.Model):
        id = db.Column(db.Integer, primary_key=True) # primary key = unique id for user
        username = db.Column(db.String(20), unique=True, nullable=False) # nullable = False means that username cannot be null (there must be a username)
        email = db.Column(db.String(120), unique=True, nullable=False)
        image_file = db.Column(db.String(20), nullable=False, default='default.jpg') # image_file = user's profile picture
        password = db.Column(db.String(60), nullable=False)
        posts = db.relationship('Post', backref='author', lazy=True)

        def __repr__(self):
            return f"User('{self.username}', {self.email}', {self.image_file}')"

# create Post class (inherits from db.model)
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"
