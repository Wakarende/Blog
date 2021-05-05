import unittest
from app.models import Post
from app import db
from flask_login import current_user

class PitchModelTest(unittest.TestCase):
  def setUp(self):
    self.new_post = Post(title="title", post_content="description", short_description="Testing", posted='datetime.datetime(2021, 5, 5, 6, 38, 2, 602419)', id=1, user_id=user.username)
    db.session.add(self.new_post)
    db.session.commit()

  def tearDown(self):
    Post.query.delete()
    db.session.commit()

  def test_save_posts(self):
    self.new_post.save_posts()
    self.assertTrue(len(Post.query.all()) > 0)

  def test_check_instance_variables(self):
    self.assertEquals(self.new_post.title, 'title')
    self.assertEquals(self.new_post.post_content, 'description')
    self.assertEquals(self.new_post.short_description, 'Testing')
    self.assertEquals(self.new_post.posted, 'datetime.datetime(2021, 5, 5, 6, 38, 2, 602419)')

