import unittest

from utils import clean_name
from utils import is_valid_email
from utils import create_user_record


class TestUtils(unittest.TestCase):

    def test_clean_name(self):
        result = clean_name("  anusha  ")
        self.assertEqual(result, "Anusha")

    def test_valid_email(self):
        result = is_valid_email("anusha@example.com")
        self.assertTrue(result)

    def test_invalid_email(self):
        result = is_valid_email("anusha")
        self.assertFalse(result)

    def test_create_user_record(self):
        result = create_user_record(
            "anusha",
            "anusha@example.com",
            "Hyderabad"
        )

        self.assertEqual(result["name"], "Anusha")
        self.assertEqual(result["email"], "anusha@example.com")
        self.assertEqual(result["city"], "Hyderabad")


if __name__ == "__main__":
    unittest.main()