from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QDialog

class Ui_guishka(object):
    def setupUi(self, guishka):
        guishka.setObjectName("guishka")
        guishka.resize(828, 801)
        self.pushButton = QtWidgets.QPushButton(parent=guishka)
        self.pushButton.setGeometry(QtCore.QRect(310, 510, 171, 28))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(parent=guishka)
        self.textBrowser.setGeometry(QtCore.QRect(20, 190, 261, 51))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=guishka)
        self.textBrowser_2.setGeometry(QtCore.QRect(280, 190, 261, 51))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=guishka)
        self.textBrowser_3.setGeometry(QtCore.QRect(540, 190, 261, 51))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.listView_2 = QtWidgets.QListView(parent=guishka)
        self.listView_2.setGeometry(QtCore.QRect(280, 240, 256, 192))
        self.listView_2.setObjectName("listView_2")
        self.listView_3 = QtWidgets.QListView(parent=guishka)
        self.listView_3.setGeometry(QtCore.QRect(540, 240, 256, 192))
        self.listView_3.setMaximumSize(QtCore.QSize(256, 16777215))
        self.listView_3.setObjectName("listView_3")
        self.listView = QtWidgets.QListView(parent=guishka)
        self.listView.setGeometry(QtCore.QRect(20, 240, 256, 192))
        self.listView.setObjectName("listView")
        self.checkBox = QtWidgets.QCheckBox(parent=guishka)
        self.checkBox.setGeometry(QtCore.QRect(320, 80, 191, 21))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=guishka)
        self.checkBox_2.setGeometry(QtCore.QRect(320, 140, 251, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=guishka)
        self.checkBox_3.setGeometry(QtCore.QRect(320, 120, 221, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=guishka)
        self.checkBox_4.setGeometry(QtCore.QRect(320, 100, 231, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=guishka)
        self.textBrowser_4.setGeometry(QtCore.QRect(180, 10, 471, 51))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_2 = QtWidgets.QPushButton(parent=guishka)
        self.pushButton_2.setGeometry(QtCore.QRect(170, 470, 171, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(parent=guishka)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 470, 171, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(parent=guishka)
        self.pushButton_4.setGeometry(QtCore.QRect(510, 470, 171, 28))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=guishka)
        self.textBrowser_5.setGeometry(QtCore.QRect(90, 560, 291, 51))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.retranslateUi(guishka)
        QtCore.QMetaObject.connectSlotsByName(guishka)

    def retranslateUi(self, guishka):
        _translate = QtCore.QCoreApplication.translate
        guishka.setWindowTitle(_translate("guishka", "Dialog"))
        self.pushButton.setText(_translate("guishka", "Закрыт приложение"))
        self.textBrowser.setHtml(_translate("guishka", "Груз"))
        self.textBrowser_2.setHtml(_translate("guishka", "Вагон"))
        self.textBrowser_3.setHtml(_translate("guishka", "Габариты"))
        self.checkBox.setText(_translate("guishka", "Лёгкий(3 вагона,0 ошибок)"))
        self.checkBox_2.setText(_translate("guishka", "Богоподобный(20 вагонов,0 ошибок)"))
        self.checkBox_3.setText(_translate("guishka", "Трудный(10 вагонов ,1 ошибка)"))
        self.checkBox_4.setText(_translate("guishka", "Нормальный(5 вагонов,0 ошибок)"))
        self.textBrowser_4.setHtml(_translate("guishka", "Уровень сложности"))
        self.pushButton_2.setText(_translate("guishka", "Сброс выбора"))
        self.pushButton_3.setText(_translate("guishka", "Проверить"))
        self.pushButton_4.setText(_translate("guishka", "Сохранить результат"))
        self.textBrowser_5.setHtml(_translate("guishka", "Результат"))

    def button_start(self,click1, click2, click3, count, count_of_construction, count_of_sostav, count_of_weigh):
        """1)Вообще нихуя не понял из этого кода, какой нахуй 'клик' что это??
        2)Все эти данные про вагон(кол-во состава, вес и тд) будем брать из базы данных (sqlite3). Соответственно нужно создать саму БД и придумать ее архитектуру.
        3)Кнопки поменять на Qpushbutton и добавить clicked.connect для связки функций,ну и соответственно сами функции
        4)Добавить html формат на кнопки, но текста в 'context' сделать поменьше
        5)Я думаю, что можно не разделять логирование с самой программой тк код небольшой все равно. Но это на усмотрение Егора Заболотного
        6)С 3 заданием тоже самое.Все данные нужно брать из БД.Сделать нормальные кнопки."""


        # if click1 == -1 or click2 == -1 or click3 == -1:
        #     print("Нехватает элементов для кейса")
        # elif click1 == 0 and click2 == 0 and click3 == 0:
        #     count_of_construction.remove(count_of_construction[click1])
        #     count_of_sostav.remove(count_of_sostav[click2])
        #     count_of_weigh.remove(count_of_weigh[click3])
        # else:
        #     count -= 1
        # return (count, count_of_construction, count_of_sostav, count_of_weigh)
        pass

    def button_part(self):
        # count_of_construction = [1, 2, 1]
        # count_of_sostav = [1, 1, 1]
        # count_of_weigh = [1, 1, 1]
        # construction_name = ["1 модель", "и тд"]
        # sostav_name = ["1 картина состава", "и тд"]
        # weigh_name = ["мясо", "и тд"]
        #
        # count = 10
        # cnt = len(construction_name) + len(sostav_name) + len(weigh_name)
        # while cnt > 0:
        #     rand = randint(0, cnt)
        #     click1 = -1
        #     click2 = -1
        #     click3 = -1
        #
        #     count, count_of_construction, count_of_sostav, count_of_weigh = button_start(click1, click2, click3, count,
        #                                                                                  count_of_construction,
        #                                                                                  count_of_sostav,
        #                                                                                  count_of_weigh)
        #     if type == True:
        #         print("10/" + count)
        #
        # if count > 8:
        #     print("Ваша оценка 5")
        # elif count > 6:
        #     print("Ваша оценка 4")
        # elif count > 4:
        #     print("Ваша оценка 3")
        # elif count > 2:
        #     print("Ваша оценка 2")
        # else:
        #     print("Ваша оценка 0")
        pass

    def button_type(self,type):
        # return not type
        pass

    def button_start(self):
        # print("кликните на режим игры: ")
        # if click == True:
        #     button_part()
        # if click == True:
        #     type = button_type(type)
        pass

###Logging
app = QApplication(sys.argv)
window = QDialog()
ui = Ui_guishka()
ui.setupUi(window)

window.show()
sys.exit(app.exec())
