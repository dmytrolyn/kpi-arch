import unittest
from main import Context, Constant, Value, Add


class TestInterpreter(unittest.TestCase):
    def test_interpret_add_expression(self):
        context = Context()
        context.set_value('a', 5)

        expression = Add(Value('a'), Constant(7))

        result = expression.interpret(context)

        self.assertEqual(result, 12)

    def test_interpret_value_expression(self):
        context = Context()
        context.set_value('a', 5)

        expression = Value('a')

        result = expression.interpret(context)

        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()