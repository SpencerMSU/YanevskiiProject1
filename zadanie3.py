import sys
from PyQt6.QtWidgets import QApplication, QDialog
from zadanie3gui import Ui_zad3

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_zad3()
ui.setupUi(window)

window.show()
sys.exit(app.exec())