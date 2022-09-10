
import unittest

from lex import tokenize



class HelloWorldTestCase(unittest.TestCase):

    def test_working(self):
        code = """print("hello world")"""
        expected_tokens = ["print", "(", '"hello world"', ")"]

        assert tokenize(code) == expected_tokens

