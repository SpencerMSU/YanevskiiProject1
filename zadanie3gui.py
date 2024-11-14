from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QDialog

class Ui_zad3(object):
    def setupUi(self, zad3):
        zad3.setObjectName("zad3")
        zad3.resize(871, 754)
        zad3.setWindowTitle("Dialog")
        self.frame = QtWidgets.QFrame(parent=zad3)
        self.frame.setGeometry(QtCore.QRect(200, 60, 401, 231))
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(parent=self.frame)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 0, 401, 231))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(parent=zad3)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(260, 340, 211, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(parent=zad3)
        self.plainTextEdit_4.setGeometry(QtCore.QRect(520, 340, 241, 31))
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.checkBox = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox.setGeometry(QtCore.QRect(50, 380, 81, 20))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_2.setGeometry(QtCore.QRect(50, 400, 81, 20))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_3.setGeometry(QtCore.QRect(50, 420, 81, 20))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_4.setGeometry(QtCore.QRect(50, 490, 81, 20))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_5.setGeometry(QtCore.QRect(50, 450, 81, 20))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_6.setGeometry(QtCore.QRect(50, 470, 81, 20))
        self.checkBox_6.setObjectName("checkBox_6")
        self.checkBox_10 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_10.setGeometry(QtCore.QRect(300, 400, 81, 20))
        self.checkBox_10.setObjectName("checkBox_10")
        self.checkBox_11 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_11.setGeometry(QtCore.QRect(300, 380, 81, 20))
        self.checkBox_11.setObjectName("checkBox_11")
        self.checkBox_12 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_12.setGeometry(QtCore.QRect(300, 420, 81, 20))
        self.checkBox_12.setObjectName("checkBox_12")
        self.checkBox_13 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_13.setGeometry(QtCore.QRect(300, 470, 81, 20))
        self.checkBox_13.setObjectName("checkBox_13")
        self.checkBox_14 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_14.setGeometry(QtCore.QRect(300, 450, 81, 20))
        self.checkBox_14.setObjectName("checkBox_14")
        self.checkBox_15 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_15.setGeometry(QtCore.QRect(300, 490, 81, 20))
        self.checkBox_15.setObjectName("checkBox_15")
        self.checkBox_16 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_16.setGeometry(QtCore.QRect(300, 550, 81, 20))
        self.checkBox_16.setObjectName("checkBox_16")
        self.checkBox_17 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_17.setGeometry(QtCore.QRect(300, 530, 81, 20))
        self.checkBox_17.setObjectName("checkBox_17")
        self.checkBox_18 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_18.setGeometry(QtCore.QRect(300, 570, 81, 20))
        self.checkBox_18.setObjectName("checkBox_18")
        self.checkBox_19 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_19.setGeometry(QtCore.QRect(560, 400, 81, 20))
        self.checkBox_19.setObjectName("checkBox_19")
        self.checkBox_20 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_20.setGeometry(QtCore.QRect(560, 380, 81, 20))
        self.checkBox_20.setObjectName("checkBox_20")
        self.checkBox_21 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_21.setGeometry(QtCore.QRect(560, 420, 81, 20))
        self.checkBox_21.setObjectName("checkBox_21")
        self.checkBox_22 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_22.setGeometry(QtCore.QRect(560, 470, 81, 20))
        self.checkBox_22.setObjectName("checkBox_22")
        self.checkBox_23 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_23.setGeometry(QtCore.QRect(560, 450, 81, 20))
        self.checkBox_23.setObjectName("checkBox_23")
        self.checkBox_24 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_24.setGeometry(QtCore.QRect(560, 490, 81, 20))
        self.checkBox_24.setObjectName("checkBox_24")
        self.checkBox_25 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_25.setGeometry(QtCore.QRect(560, 550, 81, 20))
        self.checkBox_25.setObjectName("checkBox_25")
        self.checkBox_26 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_26.setGeometry(QtCore.QRect(560, 530, 81, 20))
        self.checkBox_26.setObjectName("checkBox_26")
        self.checkBox_27 = QtWidgets.QCheckBox(parent=zad3)
        self.checkBox_27.setGeometry(QtCore.QRect(560, 570, 81, 20))
        self.checkBox_27.setObjectName("checkBox_27")
        self.pushButton = QtWidgets.QPushButton(parent=zad3)
        self.pushButton.setGeometry(QtCore.QRect(230, 610, 331, 51))
        self.pushButton.setObjectName("pushButton")
        self.textBrowser = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser.setGeometry(QtCore.QRect(10, 340, 211, 31))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_2 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 380, 31, 61))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 450, 31, 61))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_4.setGeometry(QtCore.QRect(10, 530, 31, 61))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_5.setGeometry(QtCore.QRect(260, 380, 31, 61))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_6.setGeometry(QtCore.QRect(260, 530, 31, 61))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_7.setGeometry(QtCore.QRect(260, 450, 31, 61))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_8.setGeometry(QtCore.QRect(520, 380, 31, 61))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_9.setGeometry(QtCore.QRect(520, 530, 31, 61))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_10.setGeometry(QtCore.QRect(520, 450, 31, 61))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(parent=zad3)
        self.textBrowser_11.setGeometry(QtCore.QRect(190, 680, 171, 51))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.splitter = QtWidgets.QSplitter(parent=zad3)
        self.splitter.setGeometry(QtCore.QRect(50, 530, 86, 60))
        self.splitter.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.splitter.setObjectName("splitter")
        self.checkBox_8 = QtWidgets.QCheckBox(parent=self.splitter)
        self.checkBox_8.setObjectName("checkBox_8")
        self.checkBox_9 = QtWidgets.QCheckBox(parent=self.splitter)
        self.checkBox_9.setObjectName("checkBox_9")
        self.checkBox_7 = QtWidgets.QCheckBox(parent=self.splitter)
        self.checkBox_7.setObjectName("checkBox_7")

        self.retranslateUi(zad3)
        QtCore.QMetaObject.connectSlotsByName(zad3)

    def retranslateUi(self, zad3):
        _translate = QtCore.QCoreApplication.translate
        self.plainTextEdit.setPlainText(_translate("zad3", "картинка под названием rels.png\n"
""))
        self.plainTextEdit_3.setPlainText(_translate("zad3", "Группа элементов II"))
        self.plainTextEdit_4.setPlainText(_translate("zad3", "Группа элементов III"))
        self.checkBox.setText(_translate("zad3", "Вариант 1"))
        self.checkBox_2.setText(_translate("zad3", "Вариант 2"))
        self.checkBox_3.setText(_translate("zad3", "Вариант 3"))
        self.checkBox_4.setText(_translate("zad3", "Вариант 3"))
        self.checkBox_5.setText(_translate("zad3", "Вариант 1"))
        self.checkBox_6.setText(_translate("zad3", "Вариант 2"))
        self.checkBox_10.setText(_translate("zad3", "Вариант 2"))
        self.checkBox_11.setText(_translate("zad3", "Вариант 1"))
        self.checkBox_12.setText(_translate("zad3", "Вариант 3"))
        self.checkBox_13.setText(_translate("zad3", "Вариант 2"))
        self.checkBox_14.setText(_translate("zad3", "Вариант 1"))
        self.checkBox_15.setText(_translate("zad3", "Вариант 3"))
        self.checkBox_16.setText(_translate("zad3", "Вариант 2"))
        self.checkBox_17.setText(_translate("zad3", "Вариант 1"))
        self.checkBox_18.setText(_translate("zad3", "Вариант 3"))
        self.checkBox_19.setText(_translate("zad3", "Вариант 2"))
        self.checkBox_20.setText(_translate("zad3", "Вариант 1"))
        self.checkBox_21.setText(_translate("zad3", "Вариант 3"))
        self.checkBox_22.setText(_translate("zad3", "Вариант 2"))
        self.checkBox_23.setText(_translate("zad3", "Вариант 1"))
        self.checkBox_24.setText(_translate("zad3", "Вариант 3"))
        self.checkBox_25.setText(_translate("zad3", "Вариант 2"))
        self.checkBox_26.setText(_translate("zad3", "Вариант 1"))
        self.checkBox_27.setText(_translate("zad3", "Вариант 3"))
        self.pushButton.setText(_translate("zad3", "Проверить ответы и показать оценку"))
        self.textBrowser.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Группа элементов I</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.textBrowser_2.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">1</span></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">2,4</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">3</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">5</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">10</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8pt;\"><br /></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">11</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">6,8</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">9</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">7</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("zad3", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Оценка и разбалловка</span></p></body></html>"))
        self.checkBox_8.setText(_translate("zad3", "Вариант 1"))
        self.checkBox_9.setText(_translate("zad3", "Вариант 2"))
        self.checkBox_7.setText(_translate("zad3", "Вариант 3"))

        def button_part(self):
            pass
        #     construction_name = ["рамные рельсы", "остряки", "сердечник крестовины", "контррельсы", "усовики",
        #                          "переводной механизм", "стрелка с переводным механизмом", "соединительные пути",
        #                          "крестовина с контррельсами"]
        #     count = 10
        #     cnt = 9
        #     while cnt > 0:
        #         rand = randint(0, cnt)
        #         print("Найдите " + construction_name[rand])
        #         cnt -= 1
        #         construction_name.remove(construction_name[rand])
        #         if click == True:
        #             continue
        #         elif click == False:
        #             count -= 1
        #         if type == True:
        #             print("10/" + count)
        #
        #     if count > 8:
        #         print("Ваша оценка 5")
        #     elif count > 6:
        #         print("Ваша оценка 4")
        #     elif count > 4:
        #         print("Ваша оценка 3")
        #     elif count > 2:
        #         print("Ваша оценка 2")
        #     else:
        #         print("Ваша оценка 0")
        #
        # def button_type(type):
        #     return not type
        #
        # def button_start():
        #     print("кликните на режим игры: ")
        #     if click == True:
        #         button_part()
        #     if click == True:
        #         type = button_type(type)
#Logging
app = QApplication(sys.argv)
window = QDialog()
ui = Ui_zad3()
ui.setupUi(window)

window.show()
sys.exit(app.exec())
