import sys
from PyQt6.QtWidgets import QApplication, QDialog
from zadanie1gui import Ui_guishka

app = QApplication(sys.argv)
window = QDialog()
ui = Ui_guishka()
ui.setupUi(window)

window.show()
sys.exit(app.exec())