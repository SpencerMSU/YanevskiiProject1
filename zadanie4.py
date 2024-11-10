import sys
from PyQt6.QtWidgets import QApplication, QDialog
from zadanie4gui import Ui_zad4

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_zad4()
ui.setupUi(window)

window.show()
sys.exit(app.exec())