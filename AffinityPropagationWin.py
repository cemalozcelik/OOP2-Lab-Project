# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AffinityPropagation.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AffinityPropagationWindow(object):
    def setupUi(self, AffinityPropagationWindow):
        AffinityPropagationWindow.setObjectName("AffinityPropagationWindow")
        AffinityPropagationWindow.resize(600, 220)
        AffinityPropagationWindow.setMaximumSize(QtCore.QSize(600, 220))
        self.centralwidget = QtWidgets.QWidget(AffinityPropagationWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Base = QtWidgets.QGridLayout()
        self.Base.setObjectName("Base")
        self.label_random_state = QtWidgets.QLabel(self.centralwidget)
        self.label_random_state.setObjectName("label_random_state")
        self.Base.addWidget(self.label_random_state, 1, 0, 1, 1)
        self.lineEdit_damping = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_damping.setObjectName("lineEdit_damping")
        self.Base.addWidget(self.lineEdit_damping, 0, 1, 1, 1)
        self.combobox_affinity = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_affinity.setObjectName("combobox_affinity")
        self.combobox_affinity.addItem("")
        self.combobox_affinity.addItem("")
        self.Base.addWidget(self.combobox_affinity, 3, 1, 1, 1)
        self.lineEdit_iteration = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_iteration.setObjectName("lineEdit_iteration")
        self.Base.addWidget(self.lineEdit_iteration, 2, 1, 1, 1)
        self.label_iteration = QtWidgets.QLabel(self.centralwidget)
        self.label_iteration.setObjectName("label_iteration")
        self.Base.addWidget(self.label_iteration, 2, 0, 1, 1)
        self.label_damping = QtWidgets.QLabel(self.centralwidget)
        self.label_damping.setObjectName("label_damping")
        self.Base.addWidget(self.label_damping, 0, 0, 1, 1)
        self.label_affinity = QtWidgets.QLabel(self.centralwidget)
        self.label_affinity.setObjectName("label_affinity")
        self.Base.addWidget(self.label_affinity, 3, 0, 1, 1)
        self.lineEdit_random_state = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_random_state.setObjectName("lineEdit_random_state")
        self.Base.addWidget(self.lineEdit_random_state, 1, 1, 1, 1)
        self.gridLayout.addLayout(self.Base, 0, 0, 1, 1)
        AffinityPropagationWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(AffinityPropagationWindow)
        QtCore.QMetaObject.connectSlotsByName(AffinityPropagationWindow)

    def retranslateUi(self, AffinityPropagationWindow):
        _translate = QtCore.QCoreApplication.translate
        AffinityPropagationWindow.setWindowTitle(_translate("AffinityPropagationWindow", "MainWindow"))
        self.label_random_state.setText(_translate("AffinityPropagationWindow", "random_state : int, default=None"))
        self.lineEdit_damping.setStatusTip(_translate("AffinityPropagationWindow", "Damping factor in the range [0.5, 1.0) is the extent to which the current value is maintained relative to incoming values (weighted 1 - damping). "))
        self.combobox_affinity.setStatusTip(_translate("AffinityPropagationWindow", "Which affinity to use."))
        self.combobox_affinity.setItemText(0, _translate("AffinityPropagationWindow", "euclidean"))
        self.combobox_affinity.setItemText(1, _translate("AffinityPropagationWindow", "precomputed"))
        self.lineEdit_iteration.setStatusTip(_translate("AffinityPropagationWindow", "Maximum number of iterations."))
        self.label_iteration.setText(_translate("AffinityPropagationWindow", "max_iter: int, default=200"))
        self.label_damping.setText(_translate("AffinityPropagationWindow", "damping: float, default=0.5"))
        self.label_affinity.setText(_translate("AffinityPropagationWindow", "affinity , default=’euclidean’"))
        self.lineEdit_random_state.setStatusTip(_translate("AffinityPropagationWindow", "Pseudo-random number generator to control the starting state."))
