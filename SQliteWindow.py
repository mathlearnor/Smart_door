# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SQliteWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(839, 626)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 110, 551, 501))
        self.tableView.setObjectName("tableView")
        self.pushButton_add = QtWidgets.QPushButton(Dialog)
        self.pushButton_add.setGeometry(QtCore.QRect(650, 380, 93, 28))
        self.pushButton_add.setObjectName("pushButton_add")
        self.pushButton_delete = QtWidgets.QPushButton(Dialog)
        self.pushButton_delete.setGeometry(QtCore.QRect(650, 450, 93, 28))
        self.pushButton_delete.setObjectName("pushButton_delete")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(160, 50, 261, 51))
        font = QtGui.QFont()
        font.setFamily("华光行书_CNKI")
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton_add.setText(_translate("Dialog", "增加一行"))
        self.pushButton_delete.setText(_translate("Dialog", "删除一行"))
        self.label.setText(_translate("Dialog", "已录人脸名单"))
