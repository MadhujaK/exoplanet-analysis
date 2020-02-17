import unittest

from app import app

class BasicTest(unittest.TestCase):
  def setUp(self):
    self.app = app.test_client()

  def test_mainpage(self):
    response = self.app.get('/', follow_redirects=True)
    self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
  unittest.main()
