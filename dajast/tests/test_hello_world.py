
import unittest

from dajast import build_ast, PythonPrint



class HelloWorldTestCase(unittest.TestCase):

    def test_working(self):
        tokens = ["print", "(", '"hello world"', ")"]

        tokens_ast = list(build_ast(tokens))

        assert len(tokens_ast) == 1
        assert isinstance(tokens_ast[0], PythonPrint)
        assert tokens_ast[0].print_arg ==  '"hello world"'


