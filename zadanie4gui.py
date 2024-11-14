from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import QApplication, QDialog


class Ui_zad4(object):
    def setupUi(self, zad4):
        zad4.setObjectName("zad4")
        zad4.setEnabled(True)
        zad4.resize(1313, 1180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(zad4.sizePolicy().hasHeightForWidth())
        zad4.setSizePolicy(sizePolicy)
        zad4.setMinimumSize(QtCore.QSize(0, 100))
        zad4.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        zad4.setMouseTracking(False)
        zad4.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.NoContextMenu)
        self.textEdit_2 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_2.setGeometry(QtCore.QRect(400, 350, 51, 51))
        self.textEdit_2.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_2.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_2.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_2.setLineWidth(3)
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_3.setGeometry(QtCore.QRect(400, 400, 51, 51))
        self.textEdit_3.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_3.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_3.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_3.setLineWidth(3)
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_4.setGeometry(QtCore.QRect(400, 450, 51, 51))
        self.textEdit_4.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_4.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_4.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_4.setLineWidth(3)
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_5.setGeometry(QtCore.QRect(400, 500, 51, 51))
        self.textEdit_5.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_5.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_5.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_5.setLineWidth(3)
        self.textEdit_5.setObjectName("textEdit_5")
        self.textEdit_6 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_6.setGeometry(QtCore.QRect(400, 550, 51, 51))
        self.textEdit_6.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_6.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_6.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_6.setLineWidth(3)
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_7.setGeometry(QtCore.QRect(400, 600, 51, 51))
        self.textEdit_7.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_7.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_7.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_7.setLineWidth(3)
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_8 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_8.setGeometry(QtCore.QRect(400, 650, 51, 51))
        self.textEdit_8.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_8.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_8.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_8.setLineWidth(3)
        self.textEdit_8.setObjectName("textEdit_8")
        self.textEdit_9 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_9.setGeometry(QtCore.QRect(450, 500, 51, 51))
        self.textEdit_9.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_9.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_9.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_9.setLineWidth(3)
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_10 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_10.setGeometry(QtCore.QRect(500, 500, 51, 51))
        self.textEdit_10.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_10.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_10.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_10.setLineWidth(3)
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_11 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_11.setGeometry(QtCore.QRect(550, 500, 51, 51))
        self.textEdit_11.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_11.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_11.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_11.setLineWidth(3)
        self.textEdit_11.setObjectName("textEdit_11")
        self.textEdit_12 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_12.setGeometry(QtCore.QRect(600, 500, 51, 51))
        self.textEdit_12.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_12.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_12.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_12.setLineWidth(3)
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_13.setGeometry(QtCore.QRect(650, 500, 51, 51))
        self.textEdit_13.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_13.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_13.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_13.setLineWidth(3)
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_14.setGeometry(QtCore.QRect(650, 450, 51, 51))
        self.textEdit_14.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_14.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_14.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_14.setLineWidth(3)
        self.textEdit_14.setObjectName("textEdit_14")
        self.textEdit_15 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_15.setGeometry(QtCore.QRect(650, 400, 51, 51))
        self.textEdit_15.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_15.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_15.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_15.setLineWidth(3)
        self.textEdit_15.setObjectName("textEdit_15")
        self.textEdit_16 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_16.setGeometry(QtCore.QRect(650, 350, 51, 51))
        self.textEdit_16.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_16.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_16.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_16.setLineWidth(3)
        self.textEdit_16.setObjectName("textEdit_16")
        self.textEdit_17 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_17.setGeometry(QtCore.QRect(650, 150, 51, 51))
        self.textEdit_17.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_17.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_17.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_17.setLineWidth(3)
        self.textEdit_17.setObjectName("textEdit_17")
        self.textEdit_18 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_18.setGeometry(QtCore.QRect(650, 300, 51, 51))
        self.textEdit_18.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_18.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_18.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_18.setLineWidth(3)
        self.textEdit_18.setObjectName("textEdit_18")
        self.textEdit_19 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_19.setGeometry(QtCore.QRect(650, 200, 51, 51))
        self.textEdit_19.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_19.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_19.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_19.setLineWidth(3)
        self.textEdit_19.setObjectName("textEdit_19")
        self.textEdit_20 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_20.setGeometry(QtCore.QRect(650, 250, 51, 51))
        self.textEdit_20.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_20.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_20.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_20.setLineWidth(3)
        self.textEdit_20.setObjectName("textEdit_20")
        self.textEdit_21 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_21.setGeometry(QtCore.QRect(650, 100, 51, 51))
        self.textEdit_21.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_21.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_21.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_21.setLineWidth(3)
        self.textEdit_21.setObjectName("textEdit_21")
        self.textEdit_22 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_22.setGeometry(QtCore.QRect(800, 950, 51, 51))
        self.textEdit_22.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_22.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_22.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_22.setLineWidth(3)
        self.textEdit_22.setObjectName("textEdit_22")
        self.textEdit_23 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_23.setGeometry(QtCore.QRect(700, 600, 51, 51))
        self.textEdit_23.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_23.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_23.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_23.setLineWidth(3)
        self.textEdit_23.setObjectName("textEdit_23")
        self.textEdit_24 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_24.setGeometry(QtCore.QRect(600, 600, 51, 51))
        self.textEdit_24.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_24.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_24.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_24.setLineWidth(3)
        self.textEdit_24.setObjectName("textEdit_24")
        self.textEdit_25 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_25.setGeometry(QtCore.QRect(550, 600, 51, 51))
        self.textEdit_25.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_25.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_25.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_25.setLineWidth(3)
        self.textEdit_25.setObjectName("textEdit_25")
        self.textEdit_26 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_26.setGeometry(QtCore.QRect(500, 600, 51, 51))
        self.textEdit_26.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_26.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_26.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_26.setLineWidth(3)
        self.textEdit_26.setObjectName("textEdit_26")
        self.textEdit_27 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_27.setGeometry(QtCore.QRect(450, 600, 51, 51))
        self.textEdit_27.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_27.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_27.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_27.setLineWidth(3)
        self.textEdit_27.setObjectName("textEdit_27")
        self.textEdit_28 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_28.setGeometry(QtCore.QRect(650, 600, 51, 51))
        self.textEdit_28.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_28.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_28.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_28.setLineWidth(3)
        self.textEdit_28.setObjectName("textEdit_28")
        self.textEdit_30 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_30.setGeometry(QtCore.QRect(800, 600, 51, 51))
        self.textEdit_30.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_30.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_30.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_30.setLineWidth(3)
        self.textEdit_30.setObjectName("textEdit_30")
        self.textEdit_31 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_31.setGeometry(QtCore.QRect(750, 600, 51, 51))
        self.textEdit_31.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_31.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_31.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_31.setLineWidth(3)
        self.textEdit_31.setObjectName("textEdit_31")
        self.textEdit_32 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_32.setGeometry(QtCore.QRect(850, 650, 51, 51))
        self.textEdit_32.setMinimumSize(QtCore.QSize(51, 51))
        self.textEdit_32.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_32.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_32.setLineWidth(3)
        self.textEdit_32.setObjectName("textEdit_32")
        self.textEdit_33 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_33.setGeometry(QtCore.QRect(850, 600, 51, 51))
        self.textEdit_33.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_33.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_33.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_33.setLineWidth(3)
        self.textEdit_33.setObjectName("textEdit_33")
        self.textEdit_34 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_34.setGeometry(QtCore.QRect(850, 550, 51, 51))
        self.textEdit_34.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_34.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_34.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_34.setLineWidth(3)
        self.textEdit_34.setObjectName("textEdit_34")
        self.textEdit_35 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_35.setGeometry(QtCore.QRect(850, 800, 51, 51))
        self.textEdit_35.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_35.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_35.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_35.setLineWidth(3)
        self.textEdit_35.setObjectName("textEdit_35")
        self.textEdit_36 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_36.setGeometry(QtCore.QRect(850, 700, 51, 51))
        self.textEdit_36.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_36.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_36.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_36.setLineWidth(3)
        self.textEdit_36.setObjectName("textEdit_36")
        self.textEdit_37 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_37.setGeometry(QtCore.QRect(850, 750, 51, 51))
        self.textEdit_37.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_37.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_37.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_37.setLineWidth(3)
        self.textEdit_37.setObjectName("textEdit_37")
        self.textEdit_29 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_29.setGeometry(QtCore.QRect(750, 700, 51, 51))
        self.textEdit_29.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_29.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_29.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_29.setLineWidth(3)
        self.textEdit_29.setObjectName("textEdit_29")
        self.textEdit_38 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_38.setGeometry(QtCore.QRect(650, 700, 51, 51))
        self.textEdit_38.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_38.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_38.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_38.setLineWidth(3)
        self.textEdit_38.setObjectName("textEdit_38")
        self.textEdit_39 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_39.setGeometry(QtCore.QRect(600, 700, 51, 51))
        self.textEdit_39.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_39.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_39.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_39.setLineWidth(3)
        self.textEdit_39.setObjectName("textEdit_39")
        self.textEdit_41 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_41.setGeometry(QtCore.QRect(800, 700, 51, 51))
        self.textEdit_41.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_41.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_41.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_41.setLineWidth(3)
        self.textEdit_41.setObjectName("textEdit_41")
        self.textEdit_42 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_42.setGeometry(QtCore.QRect(700, 700, 51, 51))
        self.textEdit_42.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_42.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_42.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_42.setLineWidth(3)
        self.textEdit_42.setObjectName("textEdit_42")
        self.textEdit_44 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_44.setGeometry(QtCore.QRect(550, 700, 51, 51))
        self.textEdit_44.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_44.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_44.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_44.setLineWidth(3)
        self.textEdit_44.setObjectName("textEdit_44")
        self.textEdit_40 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_40.setGeometry(QtCore.QRect(900, 700, 51, 51))
        self.textEdit_40.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_40.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_40.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_40.setLineWidth(3)
        self.textEdit_40.setObjectName("textEdit_40")
        self.textEdit_43 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_43.setGeometry(QtCore.QRect(950, 700, 51, 51))
        self.textEdit_43.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_43.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_43.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_43.setLineWidth(3)
        self.textEdit_43.setObjectName("textEdit_43")
        self.textEdit_45 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_45.setGeometry(QtCore.QRect(1000, 700, 51, 51))
        self.textEdit_45.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_45.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_45.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_45.setLineWidth(3)
        self.textEdit_45.setObjectName("textEdit_45")
        self.textEdit_47 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_47.setGeometry(QtCore.QRect(750, 800, 51, 51))
        self.textEdit_47.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_47.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_47.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_47.setLineWidth(3)
        self.textEdit_47.setObjectName("textEdit_47")
        self.textEdit_48 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_48.setGeometry(QtCore.QRect(650, 800, 51, 51))
        self.textEdit_48.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_48.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_48.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_48.setLineWidth(3)
        self.textEdit_48.setObjectName("textEdit_48")
        self.textEdit_49 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_49.setGeometry(QtCore.QRect(800, 800, 51, 51))
        self.textEdit_49.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_49.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_49.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_49.setLineWidth(3)
        self.textEdit_49.setObjectName("textEdit_49")
        self.textEdit_51 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_51.setGeometry(QtCore.QRect(600, 800, 51, 51))
        self.textEdit_51.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_51.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_51.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_51.setLineWidth(3)
        self.textEdit_51.setObjectName("textEdit_51")
        self.textEdit_52 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_52.setGeometry(QtCore.QRect(550, 800, 51, 51))
        self.textEdit_52.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_52.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_52.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_52.setLineWidth(3)
        self.textEdit_52.setObjectName("textEdit_52")
        self.textEdit_53 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_53.setGeometry(QtCore.QRect(450, 800, 51, 51))
        self.textEdit_53.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_53.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_53.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_53.setLineWidth(3)
        self.textEdit_53.setObjectName("textEdit_53")
        self.textEdit_54 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_54.setGeometry(QtCore.QRect(700, 800, 51, 51))
        self.textEdit_54.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_54.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_54.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_54.setLineWidth(3)
        self.textEdit_54.setObjectName("textEdit_54")
        self.textEdit_55 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_55.setGeometry(QtCore.QRect(500, 800, 51, 51))
        self.textEdit_55.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_55.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_55.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_55.setLineWidth(3)
        self.textEdit_55.setObjectName("textEdit_55")
        self.textEdit_46 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_46.setGeometry(QtCore.QRect(1100, 950, 51, 51))
        self.textEdit_46.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_46.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_46.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_46.setLineWidth(3)
        self.textEdit_46.setObjectName("textEdit_46")
        self.textEdit_50 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_50.setGeometry(QtCore.QRect(1000, 950, 51, 51))
        self.textEdit_50.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_50.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_50.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_50.setLineWidth(3)
        self.textEdit_50.setObjectName("textEdit_50")
        self.textEdit_56 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_56.setGeometry(QtCore.QRect(950, 950, 51, 51))
        self.textEdit_56.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_56.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_56.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_56.setLineWidth(3)
        self.textEdit_56.setObjectName("textEdit_56")
        self.textEdit_57 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_57.setGeometry(QtCore.QRect(900, 950, 51, 51))
        self.textEdit_57.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_57.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_57.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_57.setLineWidth(3)
        self.textEdit_57.setObjectName("textEdit_57")
        self.textEdit_58 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_58.setGeometry(QtCore.QRect(850, 950, 51, 51))
        self.textEdit_58.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_58.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_58.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_58.setLineWidth(3)
        self.textEdit_58.setObjectName("textEdit_58")
        self.textEdit_59 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_59.setGeometry(QtCore.QRect(1050, 950, 51, 51))
        self.textEdit_59.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_59.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_59.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_59.setLineWidth(3)
        self.textEdit_59.setObjectName("textEdit_59")
        self.textEdit_60 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_60.setGeometry(QtCore.QRect(1200, 950, 51, 51))
        self.textEdit_60.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_60.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_60.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_60.setLineWidth(3)
        self.textEdit_60.setObjectName("textEdit_60")
        self.textEdit_61 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_61.setGeometry(QtCore.QRect(1150, 950, 51, 51))
        self.textEdit_61.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_61.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_61.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_61.setLineWidth(3)
        self.textEdit_61.setObjectName("textEdit_61")
        self.textEdit_62 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_62.setGeometry(QtCore.QRect(1250, 950, 51, 51))
        self.textEdit_62.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_62.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_62.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_62.setLineWidth(3)
        self.textEdit_62.setObjectName("textEdit_62")
        self.textEdit_63 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_63.setGeometry(QtCore.QRect(450, 1050, 51, 51))
        self.textEdit_63.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_63.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_63.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_63.setLineWidth(3)
        self.textEdit_63.setObjectName("textEdit_63")
        self.textEdit_64 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_64.setGeometry(QtCore.QRect(450, 1000, 51, 51))
        self.textEdit_64.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_64.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_64.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_64.setLineWidth(3)
        self.textEdit_64.setObjectName("textEdit_64")
        self.textEdit_65 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_65.setGeometry(QtCore.QRect(450, 950, 51, 51))
        self.textEdit_65.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_65.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_65.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_65.setLineWidth(3)
        self.textEdit_65.setObjectName("textEdit_65")
        self.textEdit_66 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_66.setGeometry(QtCore.QRect(450, 850, 51, 51))
        self.textEdit_66.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_66.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_66.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_66.setLineWidth(3)
        self.textEdit_66.setObjectName("textEdit_66")
        self.textEdit_67 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_67.setGeometry(QtCore.QRect(450, 900, 51, 51))
        self.textEdit_67.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_67.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_67.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_67.setLineWidth(3)
        self.textEdit_67.setObjectName("textEdit_67")
        self.textEdit_68 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_68.setGeometry(QtCore.QRect(450, 1100, 51, 51))
        self.textEdit_68.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_68.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_68.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_68.setLineWidth(3)
        self.textEdit_68.setObjectName("textEdit_68")
        self.textEdit_69 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_69.setGeometry(QtCore.QRect(800, 850, 51, 51))
        self.textEdit_69.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_69.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_69.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_69.setLineWidth(3)
        self.textEdit_69.setObjectName("textEdit_69")
        self.textEdit_70 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_70.setGeometry(QtCore.QRect(800, 900, 51, 51))
        self.textEdit_70.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_70.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_70.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_70.setLineWidth(3)
        self.textEdit_70.setObjectName("textEdit_70")
        self.textBrowser_3 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_3.setGeometry(QtCore.QRect(400, 290, 71, 51))
        self.textBrowser_3.setMinimumSize(QtCore.QSize(71, 0))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_4.setGeometry(QtCore.QRect(360, 500, 41, 51))
        self.textBrowser_4.setMinimumSize(QtCore.QSize(41, 0))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.textBrowser_5 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_5.setGeometry(QtCore.QRect(660, 0, 41, 51))
        self.textBrowser_5.setMinimumSize(QtCore.QSize(41, 0))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.textBrowser_6 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_6.setGeometry(QtCore.QRect(360, 600, 41, 51))
        self.textBrowser_6.setMinimumSize(QtCore.QSize(41, 0))
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_7 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_7.setGeometry(QtCore.QRect(850, 500, 41, 51))
        self.textBrowser_7.setMinimumSize(QtCore.QSize(41, 0))
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_8.setGeometry(QtCore.QRect(510, 700, 41, 51))
        self.textBrowser_8.setMinimumSize(QtCore.QSize(41, 0))
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_9.setGeometry(QtCore.QRect(410, 800, 41, 51))
        self.textBrowser_9.setMinimumSize(QtCore.QSize(41, 0))
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_10.setGeometry(QtCore.QRect(760, 950, 41, 51))
        self.textBrowser_10.setMinimumSize(QtCore.QSize(41, 0))
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_11.setGeometry(QtCore.QRect(460, 750, 41, 51))
        self.textBrowser_11.setMinimumSize(QtCore.QSize(41, 0))
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(parent=zad4)
        self.textBrowser_12.setGeometry(QtCore.QRect(800, 1010, 71, 31))
        self.textBrowser_12.setMinimumSize(QtCore.QSize(71, 0))
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textEdit_71 = QtWidgets.QTextEdit(parent=zad4)
        self.textEdit_71.setGeometry(QtCore.QRect(650, 50, 51, 51))
        self.textEdit_71.setMinimumSize(QtCore.QSize(51, 0))
        self.textEdit_71.setFrameShape(QtWidgets.QFrame.Shape.Box)
        self.textEdit_71.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.textEdit_71.setLineWidth(3)
        self.textEdit_71.setObjectName("textEdit_71")

        self.retranslateUi(zad4)
        QtCore.QMetaObject.connectSlotsByName(zad4)

    def retranslateUi(self, zad4):
        _translate = QtCore.QCoreApplication.translate
        zad4.setWindowTitle(_translate("zad4", "Dialog"))
        self.textEdit_2.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_3.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_4.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_5.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_6.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_7.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_8.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_9.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_10.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_11.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_12.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_13.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_14.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_15.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_16.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_17.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_18.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_19.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_20.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_21.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_22.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_23.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_24.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_25.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_26.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_27.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_28.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_30.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_31.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_32.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_33.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_34.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_35.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_36.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_37.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_29.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_38.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_39.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_41.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_42.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_44.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_40.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_43.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_45.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_47.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_48.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_49.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_51.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_52.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_53.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_54.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_55.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_46.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_50.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_56.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_57.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_58.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_59.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_60.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_61.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_62.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_63.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_64.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_65.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_66.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_67.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_68.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_69.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_70.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textBrowser_3.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.textBrowser_4.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">2</span></p></body></html>"))
        self.textBrowser_5.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">3</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">4</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">5</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">6</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">7</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">8</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">9</span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt;\">10</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:18pt;\"><br /></p></body></html>"))
        self.textEdit_71.setHtml(_translate("zad4", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
app = QApplication(sys.argv)
window = QDialog()
ui = Ui_zad4()
ui.setupUi(window)

window.show()
sys.exit(app.exec())