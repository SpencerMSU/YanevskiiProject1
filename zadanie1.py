import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QLabel, QVBoxLayout
from PyQt6.QtGui import QPixmap
import os

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Главное окно")
        self.setGeometry(100, 100, 800, 600)
        layout = QGridLayout()
        self.setLayout(layout)

        start_button = QPushButton("Начать")
        start_button.clicked.connect(self.open_second_window)
        layout.addWidget(start_button, 1, 0, 1, 4)

        close_button = QPushButton("Закрыть")
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button, 2, 0, 1, 4)

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Второе окно")
        self.setGeometry(100, 100, 800, 600)

        layout = QGridLayout()
        self.setLayout(layout)

        folder_dir = "Gabarits"
        row = 0
        col = 0
        for image_file in os.listdir(folder_dir):
            if not (image_file.endswith('.PNG') or image_file.endswith('.jpg') or image_file.endswith('.jpeg')):
                continue
            photo_label = QLabel()
            pixmap = QPixmap(os.path.join(folder_dir, image_file))
            scaled_pixmap = pixmap.scaledToWidth(250)
            photo_label.setPixmap(scaled_pixmap)
            layout.addWidget(photo_label, row, col)
            col += 1
            if col >= 4:
                col = 0
                row += 1

        k = 0
        for i in range(2):
            for j in range(4):
                index = i * 4 + j + 1
                label = QLabel()
                pixmap = QPixmap(f'gaborit{index}.png').scaled(150, 150)
                label.setPixmap(pixmap)
                layout.addWidget(label, i, j)
                wagon_button = QPushButton(f"Вагон {k+1}")
                k += 1
                wagon_button.clicked.connect(lambda _, number_gabarits=k: self.open_third_window(number_gabarits))
                layout.addWidget(wagon_button, i + 2, j)

        check_button = QPushButton("ПРОВЕРИТЬ РЕЗУЛЬТАТ")
        check_button.clicked.connect(self.open_result_window)
        layout.addWidget(check_button, 4, 0, 1, 4)

    def open_third_window(self, number_gabarits):
        """Добавить работу с БД"""
        self.third_window = ThirdWindow()
        self.third_window.show()
        self.close()

    def open_result_window(self):
        self.result_window = ResultWindow()
        self.result_window.show()

class ThirdWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Третье окно")
        self.setGeometry(100, 100, 800, 600)

        layout = QGridLayout()
        folder_dir = "Cargo"
        row = 0
        col = 0

        for image_file in os.listdir(folder_dir):
            if not (image_file.endswith('.png') or image_file.endswith('.jpg') or image_file.endswith('.jpeg')):
                continue
            photo_label = QLabel()
            pixmap = QPixmap(os.path.join(folder_dir, image_file))
            scaled_pixmap = pixmap.scaledToWidth(250)
            photo_label.setPixmap(scaled_pixmap)


            layout.addWidget(photo_label, row, col)


            col += 1
            if col >= 4:
                col = 0
                row += 1
        k = 1
        for i in range(2):
            for j in range(4):
                index = i * 4 + j + 1
                label = QLabel()
                pixmap = QPixmap(f'vagon{index}.png').scaled(150, 150)
                label.setPixmap(pixmap)
                layout.addWidget(label, i, j)
                load_button = QPushButton(f"Груз {k}")
                k+=1
                load_button.clicked.connect(lambda _, number_cargo=k: self.open_fourth_window(number_cargo))
                layout.addWidget(load_button, i + 2, j)

        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.back_to_second_window)
        layout.addWidget(back_button, 4, 0, 1, 4)

        self.setLayout(layout)

    def open_fourth_window(self,number_cargo):
        """Добавить работу с БД"""
        self.fourth_window = FourthWindow()
        self.fourth_window.show()
        self.close()

    def back_to_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()

class FourthWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Четвертое окно")
        self.setGeometry(100, 100, 800, 600)

        layout = QGridLayout()

        folder_dir = "type_vagon"
        row = 0
        col = 0
        for image_file in os.listdir(folder_dir):
            if not (image_file.endswith('.png') or image_file.endswith('.jpg') or image_file.endswith('.jpeg')):
                continue
            photo_label = QLabel()
            pixmap = QPixmap(os.path.join(folder_dir, image_file))
            scaled_pixmap = pixmap.scaledToWidth(250)
            photo_label.setPixmap(scaled_pixmap)
            layout.addWidget(photo_label, row, col)
            col += 1
            if col >= 4:
                col = 0
                row += 1
        k = 1
        for i in range(2):
            for j in range(4):
                index = i * 4 + j + 1
                label = QLabel()
                pixmap = QPixmap(f'gruz{index}.png').scaled(150, 150)
                label.setPixmap(pixmap)
                layout.addWidget(label, i, j)
                save_button = QPushButton(f"Сохранить {k}")
                k+=1
                save_button.clicked.connect(lambda _, type_vagon=k: self.back_to_second_window(type_vagon))
                layout.addWidget(save_button, i + 2, j)

        back_button = QPushButton("Назад")
        back_button.clicked.connect(self.back_to_third_window)
        layout.addWidget(back_button, 4, 0, 1, 4)
        self.setLayout(layout)

    def back_to_second_window(self,type_vagon):
        """Добавить работу с БД"""
        self.second_window = SecondWindow()
        self.second_window.show()
        self.close()

    def back_to_third_window(self):
        self.third_window = ThirdWindow()
        self.third_window.show()
        self.close()


class ResultWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Результат")
        self.setGeometry(100, 100, 400, 200)
        layout = QVBoxLayout()
        result_label = QLabel("Ваш процент верности выполнения: 100%")  # Здесь надо добавить логику для вычисления процента
        layout.addWidget(result_label)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())