class Context:
    def __init__(self):
        self.values = {}

    def set_value(self, name, value):
        self.values[name] = value

    def get_value(self, name):
        return self.values.get(name)


class Expression:
    def interpret(self, context):
        pass


class Constant(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self, context):
        return self.value


class Value(Expression):
    def __init__(self, name):
        self.name = name

    def interpret(self, context):
        return context.get_value(self.name)


class Add(Expression):
    def __init__(self, left_expression, right_expression):
        self.left_expression = left_expression
        self.right_expression = right_expression

    def interpret(self, context):
        left_value = self.left_expression.interpret(context)
        right_value = self.right_expression.interpret(context)
        return left_value + right_value


if __name__ == "__main__":
    context = Context()
    context.set_value('a', 5)

    expression = Add(Value('a'), Constant(7))
    result = expression.interpret(context)

    expression = Add(Value('a'), Constant(result))
    result = expression.interpret(context)

    print(f"Result: {result}")