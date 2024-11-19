import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QFileDialog,
    QVBoxLayout,
    QHBoxLayout,
    QLineEdit,
    QGridLayout,
)
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt, QTimer

class ImageSearchApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Поиск предметов на картинке")


        self.search_button = QPushButton("Показать фото", clicked=self.show_photo)
        self.photo_label = QLabel()

        grid_layout = QGridLayout()

        self.line_edits = []

        for i in range(7):
            line_edit = QLineEdit()
            self.line_edits.append(line_edit)
            button = QPushButton(f"Проверить {i + 1}")
            button.clicked.connect(lambda _, idx=i+1: self.on_check(idx))
            grid_layout.addWidget(button, i, 0)
            grid_layout.addWidget(line_edit, i, 1)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.search_button)
        main_layout.addWidget(self.photo_label)
        main_layout.addLayout(grid_layout)


        self.message_label = QLabel("")
        main_layout.addWidget(self.message_label)


        self.setLayout(main_layout)
        self.resize(800, 600)
        self.show()

    def on_check(self, index):
        line_edit = self.line_edits[index - 1]
        if index == 1:
            if str(line_edit.text()).lower() == "рамные рельсы" or str(line_edit.text()).lower() == "рельсы" or str(line_edit.text()).lower() == "рельса":  # Правильное сравнение строк
                self.message_label.setText("Вы правы")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
            else:
                self.message_label.setText("Вы ошиблись")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
        elif index == 2:
            if str(line_edit.text()).lower() == "остряк":
                self.message_label.setText("Вы правы")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
            else:
                self.message_label.setText("Вы ошиблись")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
        elif index == 3:
            if str(line_edit.text()).lower() == "переводной механизм" or str(line_edit.text()).lower() == "механизм переводной":
                self.message_label.setText("Вы правы")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
            else:
                self.message_label.setText("Вы ошиблись")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
        elif index == 4:
            if str(line_edit.text()).lower() == "брусья" or str(line_edit.text()).lower() == "переводные брусья" or str(line_edit.text()).lower() == "брусья переводные":
                self.message_label.setText("Вы правы")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
            else:
                self.message_label.setText("Вы ошиблись")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
        elif index == 5:
            if str(line_edit.text()).lower() == "контррельсы" or str(line_edit.text()).lower() == "контр рельсы":
                self.message_label.setText("Вы правы")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
            else:
                self.message_label.setText("Вы ошиблись")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
        elif index == 6:
            if str(line_edit.text()).lower() == "усовик":
                self.message_label.setText("Вы правы")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
            else:
                self.message_label.setText("Вы ошиблись")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
        elif index == 7:
            if str(line_edit.text()).lower() == "сердечник" or str(line_edit.text()).lower() == "сердечник крестовины":
                self.message_label.setText("Вы правы")
                QTimer.singleShot(1000, lambda: self.message_label.clear())
            else:
                self.message_label.setText("Вы ошиблись")
                QTimer.singleShot(1000, lambda: self.message_label.clear())

    def show_photo(self):
        photo = "strelocnyj_perevod.jpg"
        pixmap = QPixmap(photo)
        scaled_pixmap = pixmap.scaledToWidth(self.width())
        self.photo_label.setPixmap(scaled_pixmap)

app = QApplication(sys.argv)
ex = ImageSearchApp()
sys.exit(app.exec())
