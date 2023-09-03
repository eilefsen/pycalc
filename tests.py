import sys
from PyQt6.QtWidgets import QApplication
import calc
import gui_ctrl
import gui




def test_controller():
    test_y = 10.0
    test_x = 10.0

    print("-- TESTING CONTROLLER --")

    # Addition
    model.reset_hist()
    test_expected_result = 0.0

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.ADD, test_x)
    test_expected_result += test_x
    assert test_function == test_expected_result,\
            f"add_() wont add\n\
            X: {test_x} with empty Calculator.hist[-1] (0.0).\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.ADD, test_x, test_y)
    test_expected_result = test_x + test_y
    assert test_function == test_expected_result,\
            f"add_() doesn't correctly add\n\
            X: {test_x} with Y: {test_y}.\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.ADD, test_x)
    test_expected_result += test_x
    assert test_function == test_expected_result,\
            f"add_() doesn't correctly add\n\
            X: {test_x} with Calculator.hist[-1]: {test_expected_result - test_x}.\n\
            Result: {test_function}, Expected result: {test_expected_result}"
            
    print("✅ add_()")

    # Subtraction
    model.reset_hist()
    test_expected_result = 0.0

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.SUBTRACT, test_x)
    test_expected_result -= test_x
    assert test_function == test_expected_result,\
            f"subtract_() wont subtract\n\
            empty Calculator.hist[-1]: 0.0, with X: {test_x}.\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.SUBTRACT, test_x, test_y)
    test_expected_result = test_x - test_y
    assert test_function == test_expected_result,\
            f"add_() doesn't correctly subtract\n\
            X: {test_x} with Y: {test_y}.\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.SUBTRACT, test_x)
    test_expected_result -= test_x
    assert test_function == test_expected_result,\
            f"add_() doesn't correctly subtract\n\
            Calculator.hist[-1]: {test_expected_result + test_x} with X: {test_x}.\n\
            Result: {test_function}, Expected result: {test_expected_result}"
    print("✅ subtract_()")

    # Multiplication
    model.reset_hist()
    test_expected_result = 0.0

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.MULTIPLY, test_x)
    test_expected_result *= test_x
    assert test_function == test_expected_result,\
            f"multiply_() wont multiply\n\
            X: {test_x} with empty Calculator.hist[-1] (0.0).\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.MULTIPLY, test_x, test_y)
    test_expected_result = test_x * test_y
    assert test_function == test_expected_result,\
            f"multiply_() doesn't correctly multiply\n\
            X: {test_x} with Y: {test_y}.\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.MULTIPLY, test_x)
    test_expected_result *= test_x
    assert test_function == test_expected_result,\
            f"multiply_() doesn't correctly multiply\n\
            X: {test_x} with Calculator.hist[-1]: {test_expected_result / test_x}.\n\
            Result: {test_function}, Expected result: {test_expected_result}"
            
    print("✅ multiply_()")

    # Division
    model.reset_hist()
    test_expected_result = 0.0

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.DIVIDE, test_x, test_y)
    test_expected_result = test_x / test_y
    assert test_function == test_expected_result,\
            f"divide_() doesn't correctly divide\n\
            X: {test_x} with Y: {test_y}.\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = ctrl.equals_(gui_ctrl.CalcOperators.DIVIDE, test_x)
    test_expected_result /= test_x
    assert test_function == test_expected_result,\
            f"divide_() doesn't correctly divide\n\
            X: {test_x} with Calculator.hist[-1]: {test_expected_result * test_x}.\n\
            Result: {test_function}, Expected result: {test_expected_result}"
    print("✅ divide_()")
    return True


def test_model():
    # calc.py

    test_y = 10.0
    test_x = 10.0

    print("-- TESTING MODEL --")

    # Addition
    assert model.reset_hist(), "reset_hist() returned false"

    test_function = model.add(test_x)
    test_expected_result = test_x
    assert test_function == test_expected_result,\
            f"add() doesn't add\n\
            X: {test_x} with empty Canculator.hist[-1]: 0.0\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = model.add(test_x, test_y)
    test_expected_result = test_x + test_y
    assert test_function == test_expected_result,\
            f"add() doesn't correctly add\n\
            X: {test_x} with Y: {test_y}\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = model.add(test_x)
    test_expected_result += test_x
    assert test_function == test_expected_result,\
            f"add() doesn't add\n\
            X: {test_x} with Canculator.hist[-1]\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    print("✅ add()")

    # Subtraction
    assert model.reset_hist(), "reset_hist() returned false"

    test_function = model.subtract(test_x)
    test_expected_result = 0 - test_x
    assert test_function == test_expected_result,\
            f"subtract() doesn't subtract\n\
            X: {test_x} with empty Canculator.hist[-1]: 0.0\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = model.subtract(test_x, test_y)
    test_expected_result = test_x - test_y
    assert test_function == test_expected_result,\
            f"subtract() doesn't correctly subtract\n\
            X: {test_x} with Y: {test_y}\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = model.subtract(test_x)
    test_expected_result -= test_x
    assert test_function == test_expected_result,\
            f"subtract() doesn't subtract\n\
            X: {test_x} with Canculator.hist[-1]\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    print("✅ subtract()")

    # Multiplication
    assert model.reset_hist(), "reset_hist() returned false"

    test_function = model.multiply(test_x)
    test_expected_result = 0 * test_x
    assert test_function == test_expected_result,\
            f"multiply() doesn't multiply\n\
            X: {test_x} with empty Canculator.hist[-1]: 0.0\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = model.multiply(test_x, test_y)
    test_expected_result = test_x * test_y
    assert test_function == test_expected_result,\
            f"multiply() doesn't correctly multiply\n\
            X: {test_x} with Y: {test_y}\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = model.multiply(test_x)
    test_expected_result *= test_x
    assert test_function == test_expected_result,\
            f"multiply() doesn't multiply\n\
            X: {test_x} with Canculator.hist[-1]\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    print("✅ multiply()")
        
    # Division
    assert model.reset_hist(), "reset_hist() returned false"

    test_function = model.divide(test_x)
    test_expected_result = 0
    assert test_function == test_expected_result,\
            f"divide() doesn't correctly handle ZeroDivisionError\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = model.divide(test_x, test_y)
    test_expected_result = test_x / test_y
    assert test_function == test_expected_result,\
            f"divide() doesn't correctly divide\n\
            X: {test_x} with Y: {test_y}\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    test_function = model.divide(test_x)
    test_expected_result /= test_x
    assert test_function == test_expected_result,\
            f"divide() doesn't divide\n\
            X: {test_x} with Canculator.hist[-1]\n\
            Result: {test_function}, Expected result: {test_expected_result}"

    print("✅ divide()")

def main():
    test_controller()
    test_model()


if __name__ == "__main__":
    # instantiate all
    app = QApplication(sys.argv)
    model = calc.Calculator()
    ctrl = gui_ctrl.CalcController(model)
    window = gui.CalcWindow(ctrl)

    main()
