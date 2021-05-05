import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
  def setUp(self):
    """
    Set up method that will run before every test
    """
    self.random_quote=Quote(id=1,author="joykirii",quote="Quote")

  
  def test_instance(self):
    self.assertTrue(isinstance(self.random_quote, Quote))

  def test_init(self):
    self.assertEqual(self.random_quote.author, "joykirii")
    self.assertEqual(self.random_quote.quote, "Quote")

