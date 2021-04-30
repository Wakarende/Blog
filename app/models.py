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
  __tablename__='posts'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
  content = db.Column(db.Text, nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

  def __repr__(self):
    return f"Post('{self.title}', '{self.date_posted}')"
        
  def save_post(self):
    db.session.add(self)
    db.session.commit()

  def delete_post(self):
    db.session.delete(self)
    db.session.commit()

  @classmethod
  def get_user_posts(cls,id):
    posts = Post.query.filter_by(user_id = id).order_by(Post.posted_at.desc()).all()
    return posts

  @classmethod
  def get_all_posts(cls):
    return Post.query.order_by(Post.posted_at).all()