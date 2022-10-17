# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MeanShift.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MeanShiftWindow(object):
    def setupUi(self, MeanShiftWindow):
        MeanShiftWindow.setObjectName("MeanShiftWindow")
        MeanShiftWindow.resize(378, 160)
        MeanShiftWindow.setMaximumSize(QtCore.QSize(380, 160))
        self.centralwidget = QtWidgets.QWidget(MeanShiftWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Base = QtWidgets.QGridLayout()
        self.Base.setObjectName("Base")
        self.lineEdit_bandwidth = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_bandwidth.setObjectName("lineEdit_bandwidth")
        self.Base.addWidget(self.lineEdit_bandwidth, 0, 1, 1, 1)
        self.lineEdit_max_iter = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_max_iter.setObjectName("lineEdit_max_iter")
        self.Base.addWidget(self.lineEdit_max_iter, 1, 1, 1, 1)
        self.label_max_iter = QtWidgets.QLabel(self.centralwidget)
        self.label_max_iter.setObjectName("label_max_iter")
        self.Base.addWidget(self.label_max_iter, 1, 0, 1, 1)
        self.label_bin_seeding = QtWidgets.QLabel(self.centralwidget)
        self.label_bin_seeding.setObjectName("label_bin_seeding")
        self.Base.addWidget(self.label_bin_seeding, 2, 0, 1, 1)
        self.combobox_bin_seeding = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_bin_seeding.setObjectName("combobox_bin_seeding")
        self.combobox_bin_seeding.addItem("")
        self.combobox_bin_seeding.addItem("")
        self.Base.addWidget(self.combobox_bin_seeding, 2, 1, 1, 1)
        self.label_bandwidth = QtWidgets.QLabel(self.centralwidget)
        self.label_bandwidth.setObjectName("label_bandwidth")
        self.Base.addWidget(self.label_bandwidth, 0, 0, 1, 1)
        self.gridLayout.addLayout(self.Base, 0, 0, 1, 1)
        MeanShiftWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MeanShiftWindow)
        QtCore.QMetaObject.connectSlotsByName(MeanShiftWindow)

    def retranslateUi(self, MeanShiftWindow):
        _translate = QtCore.QCoreApplication.translate
        MeanShiftWindow.setWindowTitle(_translate("MeanShiftWindow", "MainWindow"))
        self.lineEdit_bandwidth.setStatusTip(_translate("MeanShiftWindow", "Bandwidth used in the RBF kernel."))
        self.lineEdit_max_iter.setStatusTip(_translate("MeanShiftWindow", "Maximum number of iterations, per seed point before the clustering operation terminates (for that seed point)"))
        self.label_max_iter.setText(_translate("MeanShiftWindow", "max_iter : int, default=300"))
        self.label_bin_seeding.setText(_translate("MeanShiftWindow", "bin_seeding : bool, default=False"))
        self.combobox_bin_seeding.setStatusTip(_translate("MeanShiftWindow", "Setting this option to True will speed up the algorithm "))
        self.combobox_bin_seeding.setItemText(0, _translate("MeanShiftWindow", "False"))
        self.combobox_bin_seeding.setItemText(1, _translate("MeanShiftWindow", "True"))
        self.label_bandwidth.setStatusTip(_translate("MeanShiftWindow", "Bandwidth used in the RBF kernel."))
        self.label_bandwidth.setText(_translate("MeanShiftWindow", "bandwidth : float, default=None"))
