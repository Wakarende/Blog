import os

class Config:
  '''
  parent configurations class
  '''
  QUOTES_URL = 'http://quotes.stormconsultancy.co.uk/random.json'
  SECRET_KEY = os.environ.get('SECRET_KEY')
  
  SQLALCHEMY_TRACK_MODIFICATIONS = False

  UPLOADED_PHOTOS_DEST ='app/static/photos'

  # email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  

class ProdConfig(Config):
  '''
  class for production configurations, inheriting from config parent class
  '''
  SQLALCHEMY_DATABASE_URI = "postgresql://ejsbozzvadgurq:767b6ddfba44d481de55310fb6e921c939424f7a02091a7516a60a84cb16ab7d@ec2-23-23-128-222.compute-1.amazonaws.com:5432/df9v0q154cpooj?sslmode=require"

class DevConfig(Config):
  '''
  class for development configurations, inheriting from config parent class
  '''
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joykirii:kirii@localhost/blog'
  DEBUG=True

class TestConfig(Config):
  pass

config_options={
  'development':DevConfig,
  'production':ProdConfig,
  'test':TestConfig
}
