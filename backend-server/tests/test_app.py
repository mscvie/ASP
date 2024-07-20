import unittest

class PseudoTests(unittest.TestCase):

    def test_true_equals_true(self):
        """Test that True equals True."""
        self.assertEqual(True, True, "True should be equal to True")

    def test_another_true_equals_true(self):
        """Another test that True equals True."""
        self.assertEqual(True, True, "True should be equal to True")

if __name__ == '__main__':
    unittest.main()
