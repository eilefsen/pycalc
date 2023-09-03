from PyQt6.QtCore import (
        Qt,
        QRegularExpression
)
from PyQt6.QtGui import QRegularExpressionValidator
from PyQt6.QtWidgets import (
        QMainWindow,
        QWidget,
        QPushButton,
        QVBoxLayout,
        QGridLayout,
        QLineEdit,
        QSizePolicy
)


WINDOW_SIZE_WIDTH = 350
WINDOW_SIZE_HEIGHT = 370
DISPLAY_HEIGHT = 80


class CalcWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("Calculator")
        self.setFixedSize(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
        font = self.font()
        font.setPointSize(36)
        self.setFont(font)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

        self._createDisplay()
        self._createButtons()

    def _createDisplay(self) -> None:
        self.display = CalcDisplay()
        self.generalLayout.addWidget(self.display)

    def _createButtons(self) -> None:
        self.buttonsLayout = CalcKeypad()
        self.generalLayout.addLayout(self.buttonsLayout)
        pass


class CalcDisplay(QLineEdit):
    def __init__(self) -> None:
        super().__init__()
        self.setFixedHeight(DISPLAY_HEIGHT)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setContentsMargins(0,5,0,5)
        self.setFocus()
        self.setReadOnly(True)
        

    def clear(self):
        self.setText("0")


class CalcButton(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.setSizePolicy(
                QSizePolicy.Policy.Expanding,
                QSizePolicy.Policy.Expanding,)


class CalcKeypad(QGridLayout):
    def __init__(self) -> None:
        super().__init__()
        self.createButtons()

    def createButtons(self) -> None:
        self.buttonMap = {}
        keyBoard = [
            ["7", "8", "9", "/", "C",],
            ["4", "5", "6", "*", "("],
            ["1", "2", "3", "-", ")"],
            ["0", ".", "+", "="],
        ]

        for row, keys in enumerate(keyBoard):
            for col, key in enumerate(keys):
                self.buttonMap[key] = CalcButton(key)
                if col == 0 and row == 3:
                    self.addWidget(self.buttonMap[key], row, col, 1, 2)
                elif col > 0 and row == 3:
                    self.addWidget(self.buttonMap[key], row, col + 1)
                else:
                    self.addWidget(self.buttonMap[key], row, col)
