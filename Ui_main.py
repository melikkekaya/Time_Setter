# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/Users/melike/Desktop/set_time/main.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_main_window(object):
    def setupUi(self, main_window):
        main_window.setObjectName("main_window")
        main_window.resize(400, 500)
        main_window.setMinimumSize(QtCore.QSize(400, 500))
        main_window.setMaximumSize(QtCore.QSize(400, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/../../Downloads/stopwatch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        main_window.setWindowIcon(icon)
        main_window.setStyleSheet("background-color: rgb(212, 239, 220);")
        self.centralwidget = QtWidgets.QWidget(main_window)
        self.centralwidget.setObjectName("centralwidget")
        self.mainwdw_lbl_showtime = QtWidgets.QLabel(self.centralwidget)
        self.mainwdw_lbl_showtime.setGeometry(QtCore.QRect(70, 60, 250, 250))
        self.mainwdw_lbl_showtime.setStyleSheet("font: 75 28pt \"Comic Sans MS\";\n"
"background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));")
        self.mainwdw_lbl_showtime.setAlignment(QtCore.Qt.AlignCenter)
        self.mainwdw_lbl_showtime.setObjectName("mainwdw_lbl_showtime")
        self.mainwdw_btn_exit = QtWidgets.QPushButton(self.centralwidget)
        self.mainwdw_btn_exit.setGeometry(QtCore.QRect(160, 400, 71, 61))
        self.mainwdw_btn_exit.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/exit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainwdw_btn_exit.setIcon(icon1)
        self.mainwdw_btn_exit.setIconSize(QtCore.QSize(40, 40))
        self.mainwdw_btn_exit.setObjectName("mainwdw_btn_exit")
        self.mainwdw_btn_settime = QtWidgets.QPushButton(self.centralwidget)
        self.mainwdw_btn_settime.setGeometry(QtCore.QRect(120, 30, 151, 51))
        self.mainwdw_btn_settime.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.mainwdw_btn_settime.setStyleSheet("font: 75 16pt \"Comic Sans MS\";\n"
"background-color: rgb(180, 221, 246);\n"
"")
        self.mainwdw_btn_settime.setIcon(icon)
        self.mainwdw_btn_settime.setIconSize(QtCore.QSize(40, 40))
        self.mainwdw_btn_settime.setObjectName("mainwdw_btn_settime")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(40, 270, 321, 121))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.mainwdw_btn_play = QtWidgets.QPushButton(self.layoutWidget)
        self.mainwdw_btn_play.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.mainwdw_btn_play.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/play-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainwdw_btn_play.setIcon(icon2)
        self.mainwdw_btn_play.setIconSize(QtCore.QSize(60, 60))
        self.mainwdw_btn_play.setObjectName("mainwdw_btn_play")
        self.horizontalLayout.addWidget(self.mainwdw_btn_play)
        self.mainwdw_btn_pause = QtWidgets.QPushButton(self.layoutWidget)
        self.mainwdw_btn_pause.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/pause-button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainwdw_btn_pause.setIcon(icon3)
        self.mainwdw_btn_pause.setIconSize(QtCore.QSize(60, 60))
        self.mainwdw_btn_pause.setObjectName("mainwdw_btn_pause")
        self.horizontalLayout.addWidget(self.mainwdw_btn_pause)
        self.mainwdw_btn_reset = QtWidgets.QPushButton(self.layoutWidget)
        self.mainwdw_btn_reset.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/reset.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainwdw_btn_reset.setIcon(icon4)
        self.mainwdw_btn_reset.setIconSize(QtCore.QSize(60, 60))
        self.mainwdw_btn_reset.setObjectName("mainwdw_btn_reset")
        self.horizontalLayout.addWidget(self.mainwdw_btn_reset)
        self.mainwdw_btn_pause.raise_()
        self.mainwdw_btn_reset.raise_()
        self.mainwdw_btn_play.raise_()
        self.layoutWidget.raise_()
        self.mainwdw_btn_exit.raise_()
        self.mainwdw_lbl_showtime.raise_()
        self.mainwdw_btn_settime.raise_()
        main_window.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(main_window)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(self.menubar)
        self.menuMenu.setObjectName("menuMenu")
        main_window.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(main_window)
        self.statusbar.setObjectName("statusbar")
        main_window.setStatusBar(self.statusbar)
        self.mainwdw_action_about = QtWidgets.QAction(main_window)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/information.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainwdw_action_about.setIcon(icon5)
        self.mainwdw_action_about.setObjectName("mainwdw_action_about")
        self.mainwdw_action_exit = QtWidgets.QAction(main_window)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/exit-2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainwdw_action_exit.setIcon(icon6)
        self.mainwdw_action_exit.setObjectName("mainwdw_action_exit")
        self.mainwdw_action_main = QtWidgets.QAction(main_window)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("/Users/melike/Desktop/set_time/stopwatch.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.mainwdw_action_main.setIcon(icon7)
        self.mainwdw_action_main.setObjectName("mainwdw_action_main")
        self.menuMenu.addAction(self.mainwdw_action_about)
        self.menuMenu.addAction(self.mainwdw_action_main)
        self.menuMenu.addSeparator()
        self.menuMenu.addAction(self.mainwdw_action_exit)
        self.menubar.addAction(self.menuMenu.menuAction())

        self.retranslateUi(main_window)
        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslateUi(self, main_window):
        _translate = QtCore.QCoreApplication.translate
        main_window.setWindowTitle(_translate("main_window", "Set Timer App"))
        self.mainwdw_lbl_showtime.setText(_translate("main_window", "0"))
        self.mainwdw_btn_settime.setText(_translate("main_window", "  SET TIME"))
        self.menuMenu.setTitle(_translate("main_window", "Menu"))
        self.mainwdw_action_about.setText(_translate("main_window", "About"))
        self.mainwdw_action_exit.setText(_translate("main_window", "Exit"))
        self.mainwdw_action_main.setText(_translate("main_window", "Timer"))
