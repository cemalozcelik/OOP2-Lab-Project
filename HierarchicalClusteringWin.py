# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'HiearchicalClustering.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HiearchicalClusteringWindow(object):
    def setupUi(self, HiearchicalClusteringWindow):
        HiearchicalClusteringWindow.setObjectName("HiearchicalClusteringWindow")
        HiearchicalClusteringWindow.resize(555, 130)
        HiearchicalClusteringWindow.setMaximumSize(QtCore.QSize(560, 130))
        self.centralwidget = QtWidgets.QWidget(HiearchicalClusteringWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_label = QtWidgets.QVBoxLayout()
        self.verticalLayout_label.setObjectName("verticalLayout_label")
        self.label_n_clusters = QtWidgets.QLabel(self.centralwidget)
        self.label_n_clusters.setObjectName("label_n_clusters")
        self.verticalLayout_label.addWidget(self.label_n_clusters)
        self.label_linkage = QtWidgets.QLabel(self.centralwidget)
        self.label_linkage.setObjectName("label_linkage")
        self.verticalLayout_label.addWidget(self.label_linkage)
        self.horizontalLayout.addLayout(self.verticalLayout_label)
        self.verticalLayout_input = QtWidgets.QVBoxLayout()
        self.verticalLayout_input.setObjectName("verticalLayout_input")
        self.lineEdit_num_clusters = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_num_clusters.setObjectName("lineEdit_num_clusters")
        self.verticalLayout_input.addWidget(self.lineEdit_num_clusters)
        self.comboBox_linkage = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_linkage.setObjectName("comboBox_linkage")
        self.comboBox_linkage.addItem("")
        self.comboBox_linkage.addItem("")
        self.comboBox_linkage.addItem("")
        self.comboBox_linkage.addItem("")
        self.verticalLayout_input.addWidget(self.comboBox_linkage)
        self.horizontalLayout.addLayout(self.verticalLayout_input)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        HiearchicalClusteringWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HiearchicalClusteringWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 555, 22))
        self.menubar.setObjectName("menubar")
        HiearchicalClusteringWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HiearchicalClusteringWindow)
        self.statusbar.setObjectName("statusbar")
        HiearchicalClusteringWindow.setStatusBar(self.statusbar)

        self.retranslateUi(HiearchicalClusteringWindow)
        QtCore.QMetaObject.connectSlotsByName(HiearchicalClusteringWindow)

    def retranslateUi(self, HiearchicalClusteringWindow):
        _translate = QtCore.QCoreApplication.translate
        HiearchicalClusteringWindow.setWindowTitle(_translate("HiearchicalClusteringWindow", "MainWindow"))
        self.label_n_clusters.setStatusTip(_translate("HiearchicalClusteringWindow", "Bandwidth used in the RBF kernel."))
        self.label_n_clusters.setText(_translate("HiearchicalClusteringWindow", "n_clusters : int or None, default=2"))
        self.label_linkage.setText(_translate("HiearchicalClusteringWindow", "linkage, default=’ward’"))
        self.lineEdit_num_clusters.setStatusTip(_translate("HiearchicalClusteringWindow", "Bandwidth used in the RBF kernel."))
        self.comboBox_linkage.setItemText(0, _translate("HiearchicalClusteringWindow", "ward"))
        self.comboBox_linkage.setItemText(1, _translate("HiearchicalClusteringWindow", "complete"))
        self.comboBox_linkage.setItemText(2, _translate("HiearchicalClusteringWindow", "average"))
        self.comboBox_linkage.setItemText(3, _translate("HiearchicalClusteringWindow", "single"))
