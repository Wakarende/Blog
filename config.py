import os

class Config:
  '''
  parent configurations class
  '''
  SECRET_KEY = os.environ.get('SECRET_KEY')

  @staticmethod
  def init_app (app):
    pass

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
