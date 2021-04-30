import os

class Config:
  '''
  parent configurations class
  '''
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joykirii:kirii@localhost/blog'


  UPLOADED_PHOTOS_DEST ='app/static/photos'

  #  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
  MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
  
  # @staticmethod
  # def init_app (app):
  #   pass

class ProdConfig(Config):
  '''
  class for production configurations, inheriting from config parent class
  '''
  pass

class DevConfig(Config):
  '''
  class for development configurations, inheriting from config parent class
  '''

  DEBUG=True

config_options={
  'development':DevConfig,
  'production':ProdConfig
}
