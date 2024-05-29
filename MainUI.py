# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(972, 681)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setMinimumSize(QtCore.QSize(50, 0))
        self.frame.setMaximumSize(QtCore.QSize(50, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 18, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.pushButton_OpenFile = QtWidgets.QPushButton(self.frame)
        self.pushButton_OpenFile.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_OpenFile.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Off/line/file.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_OpenFile.setIcon(icon)
        self.pushButton_OpenFile.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_OpenFile.setObjectName("pushButton_OpenFile")
        self.verticalLayout.addWidget(self.pushButton_OpenFile)
        spacerItem1 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.pushButton_Draw = QtWidgets.QPushButton(self.frame)
        self.pushButton_Draw.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_Draw.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Off/line/pencil.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Draw.setIcon(icon1)
        self.pushButton_Draw.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Draw.setObjectName("pushButton_Draw")
        self.verticalLayout.addWidget(self.pushButton_Draw)
        spacerItem2 = QtWidgets.QSpacerItem(20, 13, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.pushButton_Redraw = QtWidgets.QPushButton(self.frame)
        self.pushButton_Redraw.setMinimumSize(QtCore.QSize(40, 40))
        self.pushButton_Redraw.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Off/line/sync.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Redraw.setIcon(icon2)
        self.pushButton_Redraw.setIconSize(QtCore.QSize(20, 20))
        self.pushButton_Redraw.setObjectName("pushButton_Redraw")
        self.verticalLayout.addWidget(self.pushButton_Redraw)
        spacerItem3 = QtWidgets.QSpacerItem(20, 353, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout.addWidget(self.frame)
        self.MplWidget = MplWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MplWidget.sizePolicy().hasHeightForWidth())
        self.MplWidget.setSizePolicy(sizePolicy)
        self.MplWidget.setObjectName("MplWidget")
        self.horizontalLayout.addWidget(self.MplWidget)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setMinimumSize(QtCore.QSize(250, 0))
        self.frame_3.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 6, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.toolBox = QtWidgets.QToolBox(self.frame_3)
        self.toolBox.setObjectName("toolBox")
        self.Page_InputData = QtWidgets.QWidget()
        self.Page_InputData.setGeometry(QtCore.QRect(0, 0, 242, 558))
        self.Page_InputData.setObjectName("Page_InputData")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.Page_InputData)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.Page_InputData)
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem4 = QtWidgets.QSpacerItem(56, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)
        self.nonlabel_FileInput = QtWidgets.QLabel(self.frame_2)
        self.nonlabel_FileInput.setObjectName("nonlabel_FileInput")
        self.horizontalLayout_2.addWidget(self.nonlabel_FileInput)
        spacerItem5 = QtWidgets.QSpacerItem(56, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem5)
        self.verticalLayout_3.addWidget(self.frame_2)
        self.frame_4 = QtWidgets.QFrame(self.Page_InputData)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 30))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.Label_Location = QtWidgets.QLabel(self.frame_4)
        self.Label_Location.setObjectName("Label_Location")
        self.verticalLayout_4.addWidget(self.Label_Location)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.Page_InputData)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem6 = QtWidgets.QSpacerItem(64, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.label_2 = QtWidgets.QLabel(self.frame_5)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem7 = QtWidgets.QSpacerItem(64, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_3.addWidget(self.frame_5)
        self.frame_6 = QtWidgets.QFrame(self.Page_InputData)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tableWidget_Coordinates = QtWidgets.QTableWidget(self.frame_6)
        self.tableWidget_Coordinates.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_Coordinates.setObjectName("tableWidget_Coordinates")
        self.tableWidget_Coordinates.setColumnCount(2)
        self.tableWidget_Coordinates.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Coordinates.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_Coordinates.setHorizontalHeaderItem(1, item)
        self.tableWidget_Coordinates.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget_Coordinates.horizontalHeader().setSortIndicatorShown(False)
        self.tableWidget_Coordinates.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_Coordinates.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_5.addWidget(self.tableWidget_Coordinates)
        self.verticalLayout_3.addWidget(self.frame_6)
        self.frame_7 = QtWidgets.QFrame(self.Page_InputData)
        self.frame_7.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_7.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.verticalLayout_3.addWidget(self.frame_7)
        self.toolBox.addItem(self.Page_InputData, "")
        self.Page_None = QtWidgets.QWidget()
        self.Page_None.setGeometry(QtCore.QRect(0, 0, 242, 558))
        self.Page_None.setObjectName("Page_None")
        self.toolBox.addItem(self.Page_None, "")
        self.verticalLayout_2.addWidget(self.toolBox)
        self.horizontalLayout.addWidget(self.frame_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 972, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen_File)
        self.menuFile.addAction(self.actionSave)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.nonlabel_FileInput.setText(_translate("MainWindow", "File Input Location"))
        self.Label_Location.setText(_translate("MainWindow", "Location"))
        self.label_2.setText(_translate("MainWindow", "Coordinates"))
        item = self.tableWidget_Coordinates.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "X"))
        item = self.tableWidget_Coordinates.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Y"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Page_InputData), _translate("MainWindow", "Input Data Information"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Page_None), _translate("MainWindow", "Page_None"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
from mplwidget import MplWidget
import Icons_rc