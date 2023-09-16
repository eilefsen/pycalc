from PyQt6.QtWidgets import QApplication
import PyQt6.sip
import sys
import calc
import gui_ctrl
import gui


def main():
    # INSTANTIATE ALL
    calcApp = QApplication(sys.argv)
    calcModel = calc.Calculator()
    calcWindow = gui.CalcWindow()
    calcControl = gui_ctrl.CalcController(calcModel, calcWindow)
    calcWindow.show()
    sys.exit(calcApp.exec())


if __name__ == "__main__":
    main()
