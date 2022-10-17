# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Kmeans.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_KmeansWindow(object):
    def setupUi(self, KmeansWindow):
        KmeansWindow.setObjectName("KmeansWindow")
        KmeansWindow.resize(400, 140)
        KmeansWindow.setMaximumSize(QtCore.QSize(400, 140))
        self.centralwidget = QtWidgets.QWidget(KmeansWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.Base = QtWidgets.QGridLayout()
        self.Base.setObjectName("Base")
        self.label_n_clusters = QtWidgets.QLabel(self.centralwidget)
        self.label_n_clusters.setObjectName("label_n_clusters")
        self.Base.addWidget(self.label_n_clusters, 0, 0, 1, 1)
        self.lineEdit_cluster_number = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_cluster_number.setObjectName("lineEdit_cluster_number")
        self.Base.addWidget(self.lineEdit_cluster_number, 0, 1, 1, 1)
        self.label_init = QtWidgets.QLabel(self.centralwidget)
        self.label_init.setObjectName("label_init")
        self.Base.addWidget(self.label_init, 1, 0, 1, 1)
        self.combobox_init = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_init.setObjectName("combobox_init")
        self.combobox_init.addItem("")
        self.combobox_init.addItem("")
        self.Base.addWidget(self.combobox_init, 1, 1, 1, 1)
        self.label_iteration = QtWidgets.QLabel(self.centralwidget)
        self.label_iteration.setObjectName("label_iteration")
        self.Base.addWidget(self.label_iteration, 2, 0, 1, 1)
        self.lineEdit_iteration = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_iteration.setObjectName("lineEdit_iteration")
        self.Base.addWidget(self.lineEdit_iteration, 2, 1, 1, 1)
        self.label_algorithm = QtWidgets.QLabel(self.centralwidget)
        self.label_algorithm.setObjectName("label_algorithm")
        self.Base.addWidget(self.label_algorithm, 3, 0, 1, 1)
        self.combobox_algorithm_k = QtWidgets.QComboBox(self.centralwidget)
        self.combobox_algorithm_k.setObjectName("combobox_algorithm_k")
        self.combobox_algorithm_k.addItem("")
        self.combobox_algorithm_k.addItem("")
        self.combobox_algorithm_k.addItem("")
        self.combobox_algorithm_k.addItem("")
        self.Base.addWidget(self.combobox_algorithm_k, 3, 1, 1, 1)
        self.gridLayout.addLayout(self.Base, 0, 0, 1, 1)
        KmeansWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(KmeansWindow)
        QtCore.QMetaObject.connectSlotsByName(KmeansWindow)

    def retranslateUi(self, KmeansWindow):
        _translate = QtCore.QCoreApplication.translate
        KmeansWindow.setWindowTitle(_translate("KmeansWindow", "MainWindow"))
        self.label_n_clusters.setText(_translate("KmeansWindow", "n_clusters, int, default=8"))
        self.lineEdit_cluster_number.setStatusTip(_translate("KmeansWindow", "Enter number of clusters"))
        self.label_init.setText(_translate("KmeansWindow", "int, default=k-means++"))
        self.combobox_init.setStatusTip(_translate("KmeansWindow", "Choice the init"))
        self.combobox_init.setItemText(0, _translate("KmeansWindow", "k-means++"))
        self.combobox_init.setItemText(1, _translate("KmeansWindow", "random"))
        self.label_iteration.setText(_translate("KmeansWindow", "max_iter, int, default = 300"))
        self.lineEdit_iteration.setStatusTip(_translate("KmeansWindow", "Enter the iteration"))
        self.label_algorithm.setText(_translate("KmeansWindow", "algorithm, default = lloyd"))
        self.combobox_algorithm_k.setStatusTip(_translate("KmeansWindow", "Choice the algorithm"))
        self.combobox_algorithm_k.setItemText(0, _translate("KmeansWindow", "lloyd"))
        self.combobox_algorithm_k.setItemText(1, _translate("KmeansWindow", "elkan"))
        self.combobox_algorithm_k.setItemText(2, _translate("KmeansWindow", "auto"))
        self.combobox_algorithm_k.setItemText(3, _translate("KmeansWindow", "full"))
