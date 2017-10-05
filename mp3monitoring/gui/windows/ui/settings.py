# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SettingsWindow(object):
    def setupUi(self, SettingsWindow):
        SettingsWindow.setObjectName("SettingsWindow")
        SettingsWindow.resize(500, 250)
        font = QtGui.QFont()
        font.setFamily("Noto Sans UI")
        SettingsWindow.setFont(font)
        SettingsWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        SettingsWindow.setDockNestingEnabled(False)
        self.centralwidget = QtWidgets.QWidget(SettingsWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(9, 9, 9, 9)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setUsesScrollButtons(True)
        self.tabWidget.setObjectName("tabWidget")
        self.General = QtWidgets.QWidget()
        self.General.setObjectName("General")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.General)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.view = QtWidgets.QGroupBox(self.General)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.view.setFont(font)
        self.view.setObjectName("view")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.view)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.guiUpdateTimeSpinBox = QtWidgets.QDoubleSpinBox(self.view)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.guiUpdateTimeSpinBox.setFont(font)
        self.guiUpdateTimeSpinBox.setMaximum(10.0)
        self.guiUpdateTimeSpinBox.setSingleStep(0.01)
        self.guiUpdateTimeSpinBox.setObjectName("guiUpdateTimeSpinBox")
        self.gridLayout_3.addWidget(self.guiUpdateTimeSpinBox, 0, 1, 1, 1)
        self.guiUpdateTimeLabel = QtWidgets.QLabel(self.view)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.guiUpdateTimeLabel.setFont(font)
        self.guiUpdateTimeLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.guiUpdateTimeLabel.setObjectName("guiUpdateTimeLabel")
        self.gridLayout_3.addWidget(self.guiUpdateTimeLabel, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        self.gridLayout_2.addWidget(self.view, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 2, 0, 1, 1)
        self.updater = QtWidgets.QGroupBox(self.General)
        self.updater.setEnabled(False)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.updater.setFont(font)
        self.updater.setObjectName("updater")
        self.gridLayout = QtWidgets.QGridLayout(self.updater)
        self.gridLayout.setObjectName("gridLayout")
        self.checkForUpdatesBox = QtWidgets.QCheckBox(self.updater)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.checkForUpdatesBox.setFont(font)
        self.checkForUpdatesBox.setObjectName("checkForUpdatesBox")
        self.gridLayout.addWidget(self.checkForUpdatesBox, 0, 0, 1, 1)
        self.gridLayout_2.addWidget(self.updater, 1, 0, 1, 1)
        self.tabWidget.addTab(self.General, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.dialogButtonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.dialogButtonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Cancel)
        self.dialogButtonBox.setObjectName("dialogButtonBox")
        self.verticalLayout.addWidget(self.dialogButtonBox)
        SettingsWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettingsWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(SettingsWindow)

    def retranslateUi(self, SettingsWindow):
        _translate = QtCore.QCoreApplication.translate
        SettingsWindow.setWindowTitle(_translate("SettingsWindow", "Settings"))
        self.view.setTitle(_translate("SettingsWindow", "View"))
        self.guiUpdateTimeSpinBox.setSuffix(_translate("SettingsWindow", "s"))
        self.guiUpdateTimeLabel.setToolTip(_translate("SettingsWindow", "Pause between the scans."))
        self.guiUpdateTimeLabel.setText(_translate("SettingsWindow", "Update gui intervall"))
        self.updater.setTitle(_translate("SettingsWindow", "Updater"))
        self.checkForUpdatesBox.setText(_translate("SettingsWindow", "Check updates at startup"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.General), _translate("SettingsWindow", "General"))
