from enum import Enum
from functools import partial, partialmethod


class CalcOperators(Enum):
    ADD = '+'
    SUBTRACT = '-'
    MULTIPLY = '*'
    DIVIDE = '/'


class CalcController:
    def __init__(self, model, view) -> None:
        self._model = model
        self._view = view
        self._connect()
        self.current_operator = None
        self._buildExpression("+221+10")
        self._calculateResult()

    def _calculateResult(self) -> None:
        result = self._model.evaluateExpression(expression=self._view.display.text())
        self._view.display.setText(result)

    def _buildExpression(self, subExpression) -> None:
        if self._view.display.text() == "ERROR":
            self._view.display.clear()
        if self._view.display.text() == "0":
            expression = subExpression
        else:
            expression = self._view.display.text() + subExpression
        self._view.display.setText(expression)

    def _connect(self) -> None:
        for keySymbol, button in self._view.buttonsLayout.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                        partial(self._buildExpression, keySymbol)
                )
        self._view.buttonsLayout.buttonMap["C"].clicked.connect(self._view.display.clear)
        self._view.buttonsLayout.buttonMap["="].clicked.connect(self._calculateResult)
        self._view.display.returnPressed.connect(self._calculateResult)
            

    def equals(self, operator, x, y=None):
        match operator:
            case CalcOperators.ADD:
                return self._model.add(x, y)
            case CalcOperators.SUBTRACT:
                return self._model.subtract(x, y)
            case CalcOperators.MULTIPLY:
                return self._model.multiply(x, y)
            case CalcOperators.DIVIDE:
                return self._model.divide(x, y)
