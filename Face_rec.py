# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Face_rec.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1025, 667)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 20, 641, 81))
        font = QtGui.QFont()
        font.setFamily("华光行书_CNKI")
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.label.setObjectName("label")
        self.label_face = QtWidgets.QLabel(Dialog)
        self.label_face.setGeometry(QtCore.QRect(20, 140, 640, 480))
        self.label_face.setFrameShape(QtWidgets.QFrame.Box)
        self.label_face.setText("")
        self.label_face.setObjectName("label_face")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(690, 143, 51, 16))
        font = QtGui.QFont()
        font.setFamily("华光行书_CNKI")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(690, 183, 61, 16))
        font = QtGui.QFont()
        font.setFamily("华光行书_CNKI")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit_ID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ID.setGeometry(QtCore.QRect(760, 140, 231, 21))
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.lineEdit_name = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_name.setGeometry(QtCore.QRect(760, 179, 231, 21))
        self.lineEdit_name.setObjectName("lineEdit_name")
        self.pushButton_begin_rec = QtWidgets.QPushButton(Dialog)
        self.pushButton_begin_rec.setGeometry(QtCore.QRect(790, 283, 131, 28))
        self.pushButton_begin_rec.setObjectName("pushButton_begin_rec")
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setGeometry(QtCore.QRect(750, 323, 231, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.pushButton_back = QtWidgets.QPushButton(Dialog)
        self.pushButton_back.setGeometry(QtCore.QRect(910, 630, 93, 28))
        self.pushButton_back.setObjectName("pushButton_back")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(690, 219, 61, 20))
        font = QtGui.QFont()
        font.setFamily("华光行书_CNKI")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_xuehao = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_xuehao.setGeometry(QtCore.QRect(760, 220, 231, 21))
        self.lineEdit_xuehao.setObjectName("lineEdit_xuehao")
        self.pushButton_show_sqlite = QtWidgets.QPushButton(Dialog)
        self.pushButton_show_sqlite.setGeometry(QtCore.QRect(20, 630, 181, 28))
        self.pushButton_show_sqlite.setObjectName("pushButton_show_sqlite")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "欢迎使用人脸录入功能"))
        self.label_3.setText(_translate("Dialog", "ID:"))
        self.label_4.setText(_translate("Dialog", "姓名："))
        self.pushButton_begin_rec.setText(_translate("Dialog", "开始人脸录入"))
        self.pushButton_back.setText(_translate("Dialog", "返回"))
        self.label_2.setText(_translate("Dialog", "学号："))
        self.pushButton_show_sqlite.setText(_translate("Dialog", "已录人脸名单"))