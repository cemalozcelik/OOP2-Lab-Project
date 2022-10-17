# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SpectralClustering.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SpectralClusteringWindow(object):
    def setupUi(self, SpectralClusteringWindow):
        SpectralClusteringWindow.setObjectName("SpectralClusteringWindow")
        SpectralClusteringWindow.resize(588, 189)
        SpectralClusteringWindow.setMaximumSize(QtCore.QSize(600, 200))
        self.centralwidget = QtWidgets.QWidget(SpectralClusteringWindow)
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
        self.label_eigen_solver = QtWidgets.QLabel(self.centralwidget)
        self.label_eigen_solver.setObjectName("label_eigen_solver")
        self.verticalLayout_label.addWidget(self.label_eigen_solver)
        self.label_n_init = QtWidgets.QLabel(self.centralwidget)
        self.label_n_init.setObjectName("label_n_init")
        self.verticalLayout_label.addWidget(self.label_n_init)
        self.label_n_neighbors = QtWidgets.QLabel(self.centralwidget)
        self.label_n_neighbors.setObjectName("label_n_neighbors")
        self.verticalLayout_label.addWidget(self.label_n_neighbors)
        self.label_assign_labels = QtWidgets.QLabel(self.centralwidget)
        self.label_assign_labels.setObjectName("label_assign_labels")
        self.verticalLayout_label.addWidget(self.label_assign_labels)
        self.horizontalLayout.addLayout(self.verticalLayout_label)
        self.verticalLayout_input = QtWidgets.QVBoxLayout()
        self.verticalLayout_input.setObjectName("verticalLayout_input")
        self.lineEdit_n_clusters = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_n_clusters.setObjectName("lineEdit_n_clusters")
        self.verticalLayout_input.addWidget(self.lineEdit_n_clusters)
        self.comboBox_eigen_solver = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_eigen_solver.setObjectName("comboBox_eigen_solver")
        self.comboBox_eigen_solver.addItem("")
        self.comboBox_eigen_solver.addItem("")
        self.comboBox_eigen_solver.addItem("")
        self.comboBox_eigen_solver.addItem("")
        self.comboBox_eigen_solver.addItem("")
        self.comboBox_eigen_solver.setItemText(4, "")
        self.verticalLayout_input.addWidget(self.comboBox_eigen_solver)
        self.lineEdit_n_init = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_n_init.setObjectName("lineEdit_n_init")
        self.verticalLayout_input.addWidget(self.lineEdit_n_init)
        self.lineEdit_n_neighbors = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_n_neighbors.setObjectName("lineEdit_n_neighbors")
        self.verticalLayout_input.addWidget(self.lineEdit_n_neighbors)
        self.comboBox_assign_labels = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_assign_labels.setObjectName("comboBox_assign_labels")
        self.comboBox_assign_labels.addItem("")
        self.comboBox_assign_labels.addItem("")
        self.comboBox_assign_labels.addItem("")
        self.verticalLayout_input.addWidget(self.comboBox_assign_labels)
        self.horizontalLayout.addLayout(self.verticalLayout_input)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        SpectralClusteringWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SpectralClusteringWindow)
        QtCore.QMetaObject.connectSlotsByName(SpectralClusteringWindow)

    def retranslateUi(self, SpectralClusteringWindow):
        _translate = QtCore.QCoreApplication.translate
        SpectralClusteringWindow.setWindowTitle(_translate("SpectralClusteringWindow", "MainWindow"))
        self.label_n_clusters.setStatusTip(_translate("SpectralClusteringWindow", "Bandwidth used in the RBF kernel."))
        self.label_n_clusters.setText(_translate("SpectralClusteringWindow", "n_clusters : int, default=8"))
        self.label_eigen_solver.setText(_translate("SpectralClusteringWindow", "eigen_solver, default=None"))
        self.label_n_init.setText(_translate("SpectralClusteringWindow", "n_init: int, default=10"))
        self.label_n_neighbors.setText(_translate("SpectralClusteringWindow", "n_neighbors: int, default=10"))
        self.label_assign_labels.setText(_translate("SpectralClusteringWindow", "assign_labels, default=’kmeans’"))
        self.lineEdit_n_clusters.setStatusTip(_translate("SpectralClusteringWindow", "Bandwidth used in the RBF kernel."))
        self.comboBox_eigen_solver.setItemText(0, _translate("SpectralClusteringWindow", "None"))
        self.comboBox_eigen_solver.setItemText(1, _translate("SpectralClusteringWindow", "arpack"))
        self.comboBox_eigen_solver.setItemText(2, _translate("SpectralClusteringWindow", "lobpcg"))
        self.comboBox_eigen_solver.setItemText(3, _translate("SpectralClusteringWindow", "amg"))
        self.lineEdit_n_init.setStatusTip(_translate("SpectralClusteringWindow", "Maximum number of iterations, per seed point before the clustering operation terminates (for that seed point)"))
        self.comboBox_assign_labels.setItemText(0, _translate("SpectralClusteringWindow", "kmeans"))
        self.comboBox_assign_labels.setItemText(1, _translate("SpectralClusteringWindow", "discretize"))
        self.comboBox_assign_labels.setItemText(2, _translate("SpectralClusteringWindow", "cluster_qr"))
