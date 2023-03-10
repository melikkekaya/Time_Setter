# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/melike/Desktop/set_time/about.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_info_window(object):
    def setupUi(self, info_window):
        info_window.setObjectName("info_window")
        info_window.resize(400, 500)
        info_window.setMinimumSize(QtCore.QSize(400, 500))
        info_window.setMaximumSize(QtCore.QSize(400, 500))
        info_window.setStyleSheet("\n"
"background-color: rgb(251, 246, 195);")
        self.info_text = QtWidgets.QTextBrowser(info_window)
        self.info_text.setGeometry(QtCore.QRect(60, 70, 281, 201))
        self.info_text.setStyleSheet("color: rgb(223, 195, 245);\n"
"background-color: rgb(212, 239, 220);\n"
"border-color: rgb(180, 221, 246);")
        self.info_text.setFrameShape(QtWidgets.QFrame.Box)
        self.info_text.setObjectName("info_text")
        self.infowdw_btn_exit = QtWidgets.QPushButton(info_window)
        self.infowdw_btn_exit.setGeometry(QtCore.QRect(200, 320, 71, 61))
        self.infowdw_btn_exit.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infowdw_btn_exit.setIcon(icon)
        self.infowdw_btn_exit.setIconSize(QtCore.QSize(40, 40))
        self.infowdw_btn_exit.setObjectName("infowdw_btn_exit")
        self.infowdw_btn_return = QtWidgets.QPushButton(info_window)
        self.infowdw_btn_return.setGeometry(QtCore.QRect(110, 320, 71, 61))
        self.infowdw_btn_return.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.infowdw_btn_return.setIcon(icon1)
        self.infowdw_btn_return.setIconSize(QtCore.QSize(40, 40))
        self.infowdw_btn_return.setObjectName("infowdw_btn_return")

        self.retranslateUi(info_window)
        QtCore.QMetaObject.connectSlotsByName(info_window)

    def retranslateUi(self, info_window):
        _translate = QtCore.QCoreApplication.translate
        info_window.setWindowTitle(_translate("info_window", "About"))
        self.info_text.setHtml(_translate("info_window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#3f87ae;\">Melike KAYA</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#3f87ae;\">22.01.2023</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:36pt; color:#3f87ae;\">Brussels</span></p></body></html>"))
