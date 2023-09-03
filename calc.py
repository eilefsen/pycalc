class Calculator:
    def __init__(self) -> None:
        self.reset_hist()

    def reset_hist(self) -> None:
        self.hist = [0.0]

    def add(self, x, y=None) -> float:
        if y is None:
            out = self.hist[-1] + x     # add last element of hist with x
        else:
            out = x + y
        self.hist.append(out)           # append to history list
        return out

    def subtract(self, x, y=None) -> float:
        if y is None:
            out = self.hist[-1] - x     # subtract last element of hist with x
        else:
            out = x - y
        self.hist.append(out)           # append to history list
        return out

    def multiply(self, x, y=None) -> float:
        if y is None:
            out = self.hist[-1] * x     # multiply last element of hist with x
        else:
            out = x * y
        self.hist.append(out)           # append to history list
        return out

    def divide(self, x, y=None) -> float:
        try:
            if y is None:
                out = self.hist[-1] / x     # divide last element of hist with x
            else:
                out = x / y
            self.hist.append(out)           # append to history list
            return out
        except ZeroDivisionError as e:
            print(e, end=": ")
            self.hist.append(0.0)
            return 0.0

    def evaluateExpression(self, expression):
        try:
            result = str(eval(expression, {}, {}))
        except Exception:
            result = "ERROR"
        return result


def main() -> None:
    calc = Calculator()
    print(calc.add(2))
    print(calc.add(10))
    calc.reset_hist()
    print(calc.add(13004, 430))
    print(calc.add(10))
    print(calc.divide(0))


if __name__ == "__main__":
    main()
