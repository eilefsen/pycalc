class Calculator:
    def evaluateExpression(self, expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = "ERROR"
        return result
