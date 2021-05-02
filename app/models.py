from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
  return User.query.get(int(user_id))



class User(UserMixin,db.Model):
    
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255),index=True)
  email = db.Column(db.String(255),unique = True)
  pass_secure = db.Column(db.String(255))
  bio = db.Column(db.String(255))
  profile_pic_path = db.Column(db.String())
  posts = db.relationship('Post', backref='user', lazy="dynamic")
  comments=db.relationship("Comment",backref='user',lazy='dynamic')

  @property
  def password(self):
    raise AttributeError('You cannot read the password attribute')

  @password.setter
  def password(self, password):
    self.pass_secure = generate_password_hash(password)


  def verify_password(self,password):
    return check_password_hash(self.pass_secure,password)

  def __repr__(self):
    return f'User {self.username}'


class Post(db.Model):
  __tablename__ = 'posts'
  id = db.Column(db.Integer,primary_key = True)
  title = db.Column(db.String(150))
  post_content = db.Column(db.String())
  short_description = db.Column(db.String())
  posted = db.Column(db.DateTime,default=datetime.utcnow)
  user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
  comments=db.relationship("Comment",backref='post',lazy='dynamic')

  def save_posts(self):
    db.session.add(self)
    db.session.commit()

  def delete_posts(self):
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def get_posts(cls,id):
    posts=Post.query.filter_by(id=id).first()
    return posts
  
  @classmethod
  def all_posts(cls):
    posts=Post.query.all()
    return posts

  @classmethod
  def get_user_posts(cls,id):
    posts=Post.query.filter_by(user_id=id).all()
    return 

  def __repr__(self):
    return f"Post {self.title}:{self.post_content}"


class Comment(db.Model):
  __tablename__='comments'

  id=db.Column(db.Integer,primary_key=True)
  contents=db.Column(db.String(255))
  posted_on=db.Column(db.DateTime,default=datetime.utcnow)
  user_id=db.Column(db.Integer,db.ForeignKey("users.id"))
  post_id=db.Column(db.Integer,db.ForeignKey("posts.id"))

  def save_comments(self):
    db.session.add(self)
    db.session.commit()

  def delete_comment(self):
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def get_comments(cls,id):
    comments=Comment.query.filter_by(post_id=id).order_by(Comment.posted_on.desc())
    return comments
  
  @classmethod
  def get_comment(cls,id):
    comment=Comment.query.filter_by(id=id).first()
    return comment

  def __repr__(self):
    return f"Comment {self.contents}"


class Subscribe(db.Model):
  __tablename__='subscribers'
  id=db.Column(db.Integer,primary_key=True)
  email=db.Column(db.String(255),unique=True)

  def save_subscriber(self):
    db.session.add(self)
    db.session.commit()

  def __repr__(self):
    return f"Subcribe {self.email}" 

class Quote:
  """
  Class for quotes consumed from API
  """
  def __init__(self,id,author,quote):
    self.id = id
    self.author = author
    self.quote = quote