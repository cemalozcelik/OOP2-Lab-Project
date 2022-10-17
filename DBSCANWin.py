# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DBSCAN.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DBSCANWindow(object):
    def setupUi(self, DBSCANWindow):
        DBSCANWindow.setObjectName("DBSCANWindow")
        DBSCANWindow.resize(584, 129)
        DBSCANWindow.setMaximumSize(QtCore.QSize(590, 200))
        self.centralwidget = QtWidgets.QWidget(DBSCANWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Base = QtWidgets.QGridLayout()
        self.Base.setObjectName("Base")
        self.label_eps = QtWidgets.QLabel(self.centralwidget)
        self.label_eps.setObjectName("label_eps")
        self.Base.addWidget(self.label_eps, 0, 0, 1, 1)
        self.label_min_samples = QtWidgets.QLabel(self.centralwidget)
        self.label_min_samples.setObjectName("label_min_samples")
        self.Base.addWidget(self.label_min_samples, 1, 0, 1, 1)
        self.combobox_algorithm_d = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_algorithm_d.setObjectName("combobox_algorithm_d")
        self.combobox_algorithm_d.addItem("")
        self.combobox_algorithm_d.addItem("")
        self.combobox_algorithm_d.addItem("")
        self.combobox_algorithm_d.addItem("")
        self.Base.addWidget(self.combobox_algorithm_d, 2, 1, 1, 1)
        self.lineEdit_eps = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_eps.setObjectName("lineEdit_eps")
        self.Base.addWidget(self.lineEdit_eps, 0, 1, 1, 1)
        self.lineEdit_min_samples = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_min_samples.setObjectName("lineEdit_min_samples")
        self.Base.addWidget(self.lineEdit_min_samples, 1, 1, 1, 1)
        self.label_algorithm = QtWidgets.QLabel(self.centralwidget)
        self.label_algorithm.setObjectName("label_algorithm")
        self.Base.addWidget(self.label_algorithm, 2, 0, 1, 1)
        self.gridLayout.addLayout(self.Base, 0, 0, 1, 1)
        DBSCANWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(DBSCANWindow)
        QtCore.QMetaObject.connectSlotsByName(DBSCANWindow)

    def retranslateUi(self, DBSCANWindow):
        _translate = QtCore.QCoreApplication.translate
        DBSCANWindow.setWindowTitle(_translate("DBSCANWindow", "MainWindow"))
        self.label_eps.setText(_translate("DBSCANWindow", "eps : float, default=0.5"))
        self.label_min_samples.setText(_translate("DBSCANWindow", "min_samples : int, default=5"))
        self.combobox_algorithm_d.setStatusTip(_translate("DBSCANWindow", "Which affinity to use."))
        self.combobox_algorithm_d.setItemText(0, _translate("DBSCANWindow", "auto"))
        self.combobox_algorithm_d.setItemText(1, _translate("DBSCANWindow", "ball_tree"))
        self.combobox_algorithm_d.setItemText(2, _translate("DBSCANWindow", "kd_tree"))
        self.combobox_algorithm_d.setItemText(3, _translate("DBSCANWindow", "brute"))
        self.lineEdit_eps.setStatusTip(_translate("DBSCANWindow", "Damping factor in the range [0.5, 1.0) is the extent to which the current value is maintained relative to incoming values (weighted 1 - damping). "))
        self.lineEdit_min_samples.setStatusTip(_translate("DBSCANWindow", "Pseudo-random number generator to control the starting state."))
        self.label_algorithm.setText(_translate("DBSCANWindow", "algorithm, default=’auto’"))
