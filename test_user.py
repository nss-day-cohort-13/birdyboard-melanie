import unittest
import birdyboard
import user

class TestUser(unittest.TestCase):

  @classmethod
  def setUpClass(self):
    pass

  def test_new_user(self):
    new_user = User("Melanie Baker", "magpiemels")
    self.assertEqual("Melanie Baker", new_user.full_name)
    self.assertqual("magpiemels", new_user.screen_name)
    self.assertIsNotNone(new_user.user_id)

  def test_select_user(self):
    user = User("Aaron Hutcheson", "ahutcheson")
    self.assertEqual("Aaron Hutcheson", user.full_name)
    self.assertqual("ahutcheson", user.screen_name)
    self.assertIsNotNone(user.user_id)








if __name__ == '__main__':
  unittest.main()
