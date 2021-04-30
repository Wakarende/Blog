from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin

class User(UserMixin,db.Model):
    
  __tablename__ = 'users'
  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(255),index=True)
  email = db.Column(db.String(255),unique = True)
  pass_secure = db.Column(db.String(255))

class Quote:
  """
  Class for quotes consumed from API
  """
  def __init__(self,id,author,quote):
    self.id = id
    self.author = author
    self.quote = quote

  