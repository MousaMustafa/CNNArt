# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'framework1.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1621, 923)
        MainWindow.setAcceptDrops(False)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(30, 30, 191, 151))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayoutWidget = QtWidgets.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(4, 0, 171, 71))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.combo_layline = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_layline.setObjectName("combo_layline")
        self.combo_layline.addItem("")
        self.combo_layline.addItem("")
        self.combo_layline.addItem("")
        self.gridLayout.addWidget(self.combo_layline, 0, 1, 1, 1)
        self.combo_laycolumn = QtWidgets.QComboBox(self.gridLayoutWidget)
        self.combo_laycolumn.setObjectName("combo_laycolumn")
        self.combo_laycolumn.addItem("")
        self.combo_laycolumn.addItem("")
        self.combo_laycolumn.addItem("")
        self.gridLayout.addWidget(self.combo_laycolumn, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.grids1 = QtWidgets.QPushButton(self.tab)
        self.grids1.setGeometry(QtCore.QRect(50, 80, 81, 31))
        self.grids1.setObjectName("grids1")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 171, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.combo_3D = QtWidgets.QComboBox(self.horizontalLayoutWidget)
        self.combo_3D.setObjectName("combo_3D")
        self.combo_3D.addItem("")
        self.combo_3D.addItem("")
        self.combo_3D.addItem("")
        self.combo_3D.addItem("")
        self.combo_3D.addItem("")
        self.combo_3D.addItem("")
        self.combo_3D.addItem("")
        self.combo_3D.addItem("")
        self.horizontalLayout.addWidget(self.combo_3D)
        self.grids2 = QtWidgets.QPushButton(self.tab_2)
        self.grids2.setGeometry(QtCore.QRect(50, 80, 81, 31))
        self.grids2.setObjectName("grids2")
        self.tabWidget.addTab(self.tab_2, "")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(250, 10, 1341, 771))
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1339, 769))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(30, 190, 191, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.openfile = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.openfile.setObjectName("openfile")
        self.horizontalLayout_2.addWidget(self.openfile)
        self.resetdicom = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.resetdicom.setObjectName("resetdicom")
        self.horizontalLayout_2.addWidget(self.resetdicom)
        self.clearimage = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.clearimage.setObjectName("clearimage")
        self.horizontalLayout_2.addWidget(self.clearimage)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(30, 390, 189, 379))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Datapre = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Datapre.setFont(font)
        self.Datapre.setObjectName("Datapre")
        self.verticalLayout.addWidget(self.Datapre)
        self.setting_CNN = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.setting_CNN.setFont(font)
        self.setting_CNN.setObjectName("setting_CNN")
        self.verticalLayout.addWidget(self.setting_CNN)
        self.deep_visualization = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.deep_visualization.setFont(font)
        self.deep_visualization.setObjectName("deep_visualization")
        self.verticalLayout.addWidget(self.deep_visualization)
        self.exit = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.exit.setFont(font)
        self.exit.setObjectName("exit")
        self.verticalLayout.addWidget(self.exit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1621, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.combo_layline.setItemText(0, _translate("MainWindow", "1"))
        self.combo_layline.setItemText(1, _translate("MainWindow", "2"))
        self.combo_layline.setItemText(2, _translate("MainWindow", "3"))
        self.combo_laycolumn.setItemText(0, _translate("MainWindow", "1"))
        self.combo_laycolumn.setItemText(1, _translate("MainWindow", "2"))
        self.combo_laycolumn.setItemText(2, _translate("MainWindow", "3"))
        self.label_2.setText(_translate("MainWindow", "columns"))
        self.label.setText(_translate("MainWindow", "lines"))
        self.grids1.setText(_translate("MainWindow", "make grids"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "2D"))
        self.label_3.setText(_translate("MainWindow", "lines"))
        self.combo_3D.setItemText(0, _translate("MainWindow", "1"))
        self.combo_3D.setItemText(1, _translate("MainWindow", "2"))
        self.combo_3D.setItemText(2, _translate("MainWindow", "3"))
        self.combo_3D.setItemText(3, _translate("MainWindow", "4"))
        self.combo_3D.setItemText(4, _translate("MainWindow", "5"))
        self.combo_3D.setItemText(5, _translate("MainWindow", "6"))
        self.combo_3D.setItemText(6, _translate("MainWindow", "7"))
        self.combo_3D.setItemText(7, _translate("MainWindow", "8"))
        self.grids2.setText(_translate("MainWindow", "make grids"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "3D"))
        self.openfile.setText(_translate("MainWindow", "load"))
        self.resetdicom.setText(_translate("MainWindow", "reset"))
        self.clearimage.setText(_translate("MainWindow", "clear"))
        self.Datapre.setText(_translate("MainWindow", "Data Preprocess"))
        self.setting_CNN.setText(_translate("MainWindow", "Set CNN"))
        self.deep_visualization.setText(_translate("MainWindow", "Deep Visualization"))
        self.exit.setText(_translate("MainWindow", "Exit"))

