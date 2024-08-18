import unittest
from nerif.nerif_core import *


class MyTestCase(unittest.TestCase):
    def test_judge(self):
        judge = nerif("the sky is blue")
        self.assertEqual(True, judge)  # add assertion here
        judge = nerif("Do you know who I am?")
        self.assertEqual(False, judge)

    def test_match(self):
        test_selection = {
            "1": "the sky is blue",
            "2": "the sky is green",
            "3": "the sky is red",
        }
        match_result = nerif_match("the truth", test_selection)

        self.assertEqual("1", match_result)
        test_selection = {
            "reboot": "restart the server, it may takes a few minutes",
            "adduser": "add a new user on my server",
            "reservation": "make a reservation for the server",
        }
        match_result = nerif_match("I wanna use the server for AI training tonight", test_selection)

        self.assertEqual("reservation", match_result)


if __name__ == '__main__':
    unittest.main()