from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QLabel
from PyQt5 import QtCore, QtGui, QtWidgets
from app_ui_project import Ui_MainWindow
import sys
from PyQt5.QtGui import  QPixmap
from clustering import Clusters
from skimage import  img_as_ubyte,io
import matplotlib.pyplot as plt

from AffinityPropagationWin import Ui_AffinityPropagationWindow
from KMeansWin import Ui_KmeansWindow
from DBSCANWin import Ui_DBSCANWindow
from SpectralClusteringWin import Ui_SpectralClusteringWindow
from MeanShiftWin import Ui_MeanShiftWindow
from HierarchicalClusteringWin import Ui_HiearchicalClusteringWindow

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.width = self.label_initial_solution.geometry().width()
        self.height = self.label_initial_solution.geometry().height()
        
        #Menu : File
        #Open Data
        self.action_open_data.triggered.connect(self.open_data)
        self.pushButton_action_open_data.clicked.connect(self.open_data)
        #Save initial solution
        self.action_save_initial_solution.triggered.connect(self.save_initial_solution)
        self.pushButton_action_save_initial_solution.clicked.connect(self.save_initial_solution)
        #Save final solution
        self.action_save_final_solution.triggered.connect(self.save_final_solution)
        self.pushButton_action_save_final_solution.clicked.connect(self.save_final_solution)
        #Export initial solution
        self.action_export_as_initial_solution.triggered.connect(self.export_as_initial_solution)
        self.pushButton_action_export_as_initial_solution.clicked.connect(self.export_as_initial_solution)
        #Export final solution
        self.action_export_as_final_solution.triggered.connect(self.export_as_final_solution)
        self.pushButton_action_export_as_final_solution.clicked.connect(self.export_as_final_solution)
        #Exit
        self.action_exit.triggered.connect(self.exit)

        #Menu : Edit
        #Clear
        self.action_clear_initial_solution.triggered.connect(self.clear_initial_solution)
        self.pushButton_action_clear_initial_solution.clicked.connect(self.clear_initial_solution)
        self.action_clear_final_solution.triggered.connect(self.clear_final_solution)
        self.pushButton_action_clear_final_solution.clicked.connect(self.clear_final_solution)
        #Undo and Redo
        ##Polymorphizm

        #Menu : Clustering
        ##K means
        self.action_k_means.triggered.connect(self.k_means)
        self.pushButton_k_means.clicked.connect(self.k_means)
        ##Affinity Propagation
        self.action_affinity_propagation.triggered.connect(self.affinity_propagation)
        self.pushButton_action_affinity_propagation.clicked.connect(self.affinity_propagation)
        ##Mean-shift
        self.action_mean_shift.triggered.connect(self.mean_shift)
        self.pushButton_action_mean_shift.clicked.connect(self.mean_shift)
        ##Spectral Clustering
        self.action_spectral_clustering.triggered.connect(self.spectral_clustering)
        self.pushButton_action_spectral_clustering.clicked.connect(self.spectral_clustering)
        #Hierarchical Clustering
        self.action_hierarcical_clustering.triggered.connect(self.hierarcical_clustering)
        self.pushButton_action_hierarcical_clustering.clicked.connect(self.hierarcical_clustering)
        ##DBSCAN
        self.action_DBSCAN.triggered.connect(self.dbscan)
        self.pushButton_action_DBSCAN.clicked.connect(self.dbscan)
        
        #Menu : Heuristic
        ##Hill Climbing
        self.action_hill_climbing.triggered.connect(self.hill_climbing)
        self.pushButton_action_hill_climbing.clicked.connect(self.hill_climbing)
        ##Simulated Anneling
        self.action_simulated_anneling.triggered.connect(self.simulated_anneling)
        self.pushButton_action_simulated_anneling.clicked.connect(self.simulated_anneling)
        
        
        
    #Menu : File
    
    def open_data(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "", "Text (*.txt)", options=options)
        if fileName:
            print("Selected filename: ", fileName)
            self.source = fileName
            self.plot = Clusters(self.source)  
            self.plot_initial_solution(self.plot.get_initial_solution_source())
            
    
    def plot_initial_solution(self,source):
        self.source = source
        self.image  = io.imread(fname=self.source)
        arr = img_as_ubyte(self.image)
        img = QtGui.QImage(arr.data, arr.shape[1], arr.shape[0], arr.strides[0], QtGui.QImage.Format_ARGB32_Premultiplied)
        pixmap = QPixmap.fromImage(img)
        if(self.image.shape[1] >= self.width or self.image.shape[0] >= self.height):
            self.groupBox_initial_solution.setMinimumWidth(self.image.shape[1])
            self.groupBox_initial_solution.setMinimumHeight(self.image.shape[0])
        self.label_initial_solution.setPixmap(pixmap)
        self.enable_clustering_menu(True)
    
    def enable_clustering_menu(self,bool):
        self.action_k_means.setEnabled(bool)
        self.pushButton_k_means.setEnabled(bool)
        self.action_affinity_propagation.setEnabled(bool)
        self.pushButton_action_affinity_propagation.setEnabled(bool)
        self.action_mean_shift.setEnabled(bool)
        self.pushButton_action_mean_shift.setEnabled(bool)
        self.action_spectral_clustering.setEnabled(bool)
        self.pushButton_action_spectral_clustering.setEnabled(bool)
        self.action_hierarcical_clustering.setEnabled(bool)
        self.pushButton_action_hierarcical_clustering.setEnabled(bool)
        self.action_DBSCAN.setEnabled(bool)
        self.pushButton_action_DBSCAN.setEnabled(bool)
        self.action_clear_initial_solution.setEnabled(bool)
        self.pushButton_action_clear_initial_solution.setEnabled(bool)
        self.action_clear_initial_solution.setEnabled(bool)
        self.pushButton_action_clear_initial_solution.setEnabled(bool)
        self.action_undo_initial_solution.setEnabled(bool)
        self.pushButton_action_undo_initial_solution.setEnabled(bool)
    
    def enable_action_after_clustering(self,bool):
        self.action_export_as_initial_solution.setEnabled(bool)
        self.pushButton_action_export_as_initial_solution.setEnabled(bool)
        self.action_save_initial_solution.setEnabled(bool)
        self.pushButton_action_save_initial_solution.setEnabled(bool)
    def save_initial_solution(self):
        plt.savefig(self.plot.get_initial_solution_source())
    def save_final_solution(self):
        pass
    def export_as_initial_solution(self):
        plt.savefig("filename.jpg")
    def export_as_final_solution(self):
        pass
    def exit(self):
        sys.exit()
    
    #Menu : Edit
    
    def clear_initial_solution(self):
        self.label_initial_solution.clear()
        self.action_clear_initial_solution.setEnabled(False)
        self.pushButton_action_clear_initial_solution.setEnabled(False)
        self.enable_clustering_menu(False)
    def clear_final_solution(self):
        self.label_final_solution.clear()
        self.action_clear_initial_solution.setEnabled(False)
        self.pushButton_action_clear_final_solution.setEnabled(False)
    
    #Menu : Clustering
    #K-means
    def cluster_number_changed(self):
        cluster_n = ( self.ui.lineEdit_cluster_number.text())
        algorithm = (self.ui.combobox_algorithm_k.currentText())
        max_iter = (self.ui.lineEdit_iteration.text())
        init = self.ui.combobox_init.currentText()
        self.textEdit_info_panel.setText("cluster number ="+(cluster_n)+"\talgorithm: "+ (algorithm)+ "\tmax_iter : "+(max_iter)+"\tinit : "+ (init))
        self.label_result.setText("cluster number ="+(cluster_n)+"\nalgorithm: "+ (algorithm)+ "\nmax_iter : "+(max_iter)+"\ninit : "+ (init))
        self.plot_initial_solution(self.plot.k_means(cluster_n,init,max_iter,algorithm))
        
    def iter_changed(self):
        cluster_n = ( self.ui.lineEdit_cluster_number.text())
        algorithm = (self.ui.combobox_algorithm_k.currentText())
        max_iter = (self.ui.lineEdit_iteration.text())
        init = self.ui.combobox_init.currentText()
        self.textEdit_info_panel.setText("cluster number ="+(cluster_n)+"\talgorithm: "+ (algorithm)+ "\tmax_iter : "+(max_iter)+"\tinit : "+ (init))
        self.label_result.setText("cluster number ="+(cluster_n)+"\nalgorithm: "+ (algorithm)+ "\nmax_iter : "+(max_iter)+"\ninit : "+ (init))
        self.plot_initial_solution(self.plot.k_means(cluster_n,init,max_iter,algorithm))
        
    def algorithm_changed(self):
        cluster_n = ( self.ui.lineEdit_cluster_number.text())
        algorithm = (self.ui.combobox_algorithm_k.currentText())
        max_iter = (self.ui.lineEdit_iteration.text())
        init = self.ui.combobox_init.currentText()
        self.textEdit_info_panel.setText("cluster number ="+(cluster_n)+"\talgorithm: "+ (algorithm)+ "\tmax_iter : "+(max_iter)+"\tinit : "+ (init))
        self.label_result.setText("cluster number ="+(cluster_n)+"\nalgorithm: "+ (algorithm)+ "\nmax_iter : "+(max_iter)+"\ninit : "+ (init))
        self.plot_initial_solution(self.plot.k_means(cluster_n,init,max_iter,algorithm))
    
    def init_changes(self):
        cluster_n = ( self.ui.lineEdit_cluster_number.text())
        algorithm = (self.ui.combobox_algorithm_k.currentText())
        max_iter = (self.ui.lineEdit_iteration.text())
        init = self.ui.combobox_init.currentText()
        self.textEdit_info_panel.setText("cluster number ="+(cluster_n)+"\talgorithm: "+ (algorithm)+ "\tmax_iter : "+(max_iter)+"\tinit : "+ (init))
        self.label_result.setText("cluster number ="+(cluster_n)+"\nalgorithm: "+ (algorithm)+ "\nmax_iter : "+(max_iter)+"\ninit : "+ (init))
        self.plot_initial_solution(self.plot.k_means(cluster_n,init,max_iter,algorithm))
    def k_means(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_KmeansWindow()
        self.ui.setupUi(self.window)
        self.ui.lineEdit_cluster_number.returnPressed.connect(self.cluster_number_changed)
        self.ui.lineEdit_iteration.returnPressed.connect(self.iter_changed)
        self.ui.combobox_algorithm_k.currentTextChanged.connect(self.algorithm_changed)
        self.ui.combobox_init.currentTextChanged.connect(self.init_changes)
        
        self.window.show()

    #affinity_propagation
    def affinity_changed(self):
        affinity = self.ui.combobox_affinity.currentText()
        damping = self.ui.lineEdit_damping.text()
        iter = self.ui.lineEdit_iteration.text()
        random_state = self.ui.lineEdit_random_state.text()
        self.textEdit_info_panel.setText("affinity:"+affinity+"\tdamping:"+damping+"\titer:"+iter+"\trandom_state:"+random_state)
        self.label_result.setText("affinity:"+affinity+"\ndamping:"+damping+"\niter:"+iter+"\nrandom_state:"+random_state)
        self.plot_initial_solution(self.plot.affinity_propagation(damping,iter,affinity,random_state))
    def damping_changed(self):
        affinity = self.ui.combobox_affinity.currentText()
        damping = self.ui.lineEdit_damping.text()
        iter = self.ui.lineEdit_iteration.text()
        random_state = self.ui.lineEdit_random_state.text()
        self.textEdit_info_panel.setText("affinity:"+affinity+"\tdamping:"+damping+"\titer:"+iter+"\trandom_state:"+random_state)
        self.label_result.setText("affinity:"+affinity+"\ndamping:"+damping+"\niter:"+iter+"\nrandom_state:"+random_state)
        self.plot_initial_solution(self.plot.affinity_propagation(damping,iter,affinity,random_state))

    def iter_affinity_changed(self):
        affinity = self.ui.combobox_affinity.currentText()
        damping = self.ui.lineEdit_damping.text()
        iter = self.ui.lineEdit_iteration.text()
        random_state = self.ui.lineEdit_random_state.text()
        self.textEdit_info_panel.setText("affinity:"+affinity+"\tdamping:"+damping+"\titer:"+iter+"\trandom_state:"+random_state)
        self.label_result.setText("affinity:"+affinity+"\ndamping:"+damping+"\niter:"+iter+"\nrandom_state:"+random_state)
        self.plot_initial_solution(self.plot.affinity_propagation(damping,iter,affinity,random_state))

    def random_state_affinity_changed(self):
        affinity = self.ui.combobox_affinity.currentText()
        damping = self.ui.lineEdit_damping.text()
        iter = self.ui.lineEdit_iteration.text()
        random_state = self.ui.lineEdit_random_state.text()
        self.textEdit_info_panel.setText("affinity:"+affinity+"\tdamping:"+damping+"\titer:"+iter+"\trandom_state:"+random_state)
        self.label_result.setText("affinity:"+affinity+"\ndamping:"+damping+"\niter:"+iter+"\nrandom_state:"+random_state)
        self.plot_initial_solution(self.plot.affinity_propagation(damping,iter,affinity,random_state))

    def affinity_propagation(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AffinityPropagationWindow()
        self.ui.setupUi(self.window)
        self.ui.combobox_affinity.currentTextChanged.connect(self.affinity_changed)
        self.ui.lineEdit_damping.returnPressed.connect(self.damping_changed)
        self.ui.lineEdit_iteration.returnPressed.connect(self.iter_affinity_changed)
        self.ui.lineEdit_random_state.returnPressed.connect(self.random_state_affinity_changed)
        self.window.show()
    
    # mean_shift
    def bandwidth_mean_shift(self):
        bandwidth = self.ui.lineEdit_bandwidth.text()
        bin_seeding = self.ui.combobox_bin_seeding.currentText()
        max_iter = self.ui.lineEdit_max_iter.text()
        self.textEdit_info_panel.setText("bandwidth:"+bandwidth+"\tbin_seeding:"+bin_seeding+"\tmax_iter:"+max_iter)
        self.label_result.setText("bandwidth:"+bandwidth+"\nbin_seeding:"+bin_seeding+"\nmax_iter:"+max_iter)
        self.plot_initial_solution(self.plot.mean_shift(bandwidth,bin_seeding,max_iter))

    def bin_seeding_mean_shift(self):
        bandwidth = self.ui.lineEdit_bandwidth.text()
        bin_seeding = self.ui.combobox_bin_seeding.currentText()
        max_iter = self.ui.lineEdit_max_iter.text()
        self.textEdit_info_panel.setText("bandwidth:"+bandwidth+"\tbin_seeding:"+bin_seeding+"\tmax_iter:"+max_iter)
        self.label_result.setText("bandwidth:"+bandwidth+"\nbin_seeding:"+bin_seeding+"\nmax_iter:"+max_iter)
        self.plot_initial_solution(self.plot.mean_shift(bandwidth,bin_seeding,max_iter))
        
    def max_iter_mean_shift(self):
        bandwidth = self.ui.lineEdit_bandwidth.text()
        bin_seeding = self.ui.combobox_bin_seeding.currentText()
        max_iter = self.ui.lineEdit_max_iter.text()
        self.textEdit_info_panel.setText("bandwidth:"+bandwidth+"\tbin_seeding:"+bin_seeding+"\tmax_iter:"+max_iter)
        self.label_result.setText("bandwidth:"+bandwidth+"\nbin_seeding:"+bin_seeding+"\nmax_iter:"+max_iter)
        self.plot_initial_solution(self.plot.mean_shift(bandwidth,bin_seeding,max_iter))
        
    def mean_shift(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MeanShiftWindow()
        self.ui.setupUi(self.window)
        self.ui.lineEdit_bandwidth.returnPressed.connect(self.bandwidth_mean_shift)
        self.ui.combobox_bin_seeding.currentTextChanged.connect(self.bin_seeding_mean_shift)
        self.ui.lineEdit_max_iter.returnPressed.connect(self.max_iter_mean_shift)
        self.window.show()
    
    
    def cluster_number_spectral_clustering(self):
        cluster_number = self.ui.lineEdit_n_clusters.text()
        init = self.ui.lineEdit_n_init.text()
        neighbors = self.ui.lineEdit_n_neighbors.text()
        eigen_solver = self.ui.comboBox_eigen_solver.currentText()
        assign_labels = self.ui.comboBox_assign_labels.currentText()
        
        self.textEdit_info_panel.setText("cluster_number:"+cluster_number+"\tinit:"+init+"\tneighbors:"+neighbors+"\teigen_solver:"+eigen_solver+"\tassign_labels:"+assign_labels)
        self.label_result.setText("cluster_number:"+cluster_number+"\ninit:"+init+"\nneighbors:"+neighbors+"\neigen_solver:"+eigen_solver+"\nassign_labels:"+assign_labels)
        self.plot_initial_solution(self.plot.spectral_clustering(cluster_number,eigen_solver,init,neighbors,assign_labels))
    def init_number_spectral_clustering(self):
        cluster_number = self.ui.lineEdit_n_clusters.text()
        init = self.ui.lineEdit_n_init.text()
        neighbors = self.ui.lineEdit_n_neighbors.text()
        eigen_solver = self.ui.comboBox_eigen_solver.currentText()
        assign_labels = self.ui.comboBox_assign_labels.currentText()
        self.textEdit_info_panel.setText("cluster_number:"+cluster_number+"\tinit:"+init+"\tneighbors:"+neighbors+"\teigen_solver:"+eigen_solver+"\tassign_labels:"+assign_labels)
        self.label_result.setText("cluster_number:"+cluster_number+"\ninit:"+init+"\nneighbors:"+neighbors+"\neigen_solver:"+eigen_solver+"\nassign_labels:"+assign_labels)
        self.plot_initial_solution(self.plot.spectral_clustering(cluster_number,eigen_solver,init,neighbors,assign_labels))
    
    #spectral_clustering
    def neighbors_number_spectral_clustering(self):
        cluster_number = self.ui.lineEdit_n_clusters.text()
        init = self.ui.lineEdit_n_init.text()
        neighbors = self.ui.lineEdit_n_neighbors.text()
        eigen_solver = self.ui.comboBox_eigen_solver.currentText()
        assign_labels = self.ui.comboBox_assign_labels.currentText()
        self.textEdit_info_panel.setText("cluster_number:"+cluster_number+"\tinit:"+init+"\tneighbors:"+neighbors+"\teigen_solver:"+eigen_solver+"\tassign_labels:"+assign_labels)
        self.label_result.setText("cluster_number:"+cluster_number+"\ninit:"+init+"\nneighbors:"+neighbors+"\neigen_solver:"+eigen_solver+"\nassign_labels:"+assign_labels)
        self.plot_initial_solution(self.plot.spectral_clustering(cluster_number,eigen_solver,init,neighbors,assign_labels))
        
    def eigen_solver(self):
        cluster_number = self.ui.lineEdit_n_clusters.text()
        init = self.ui.lineEdit_n_init.text()
        neighbors = self.ui.lineEdit_n_neighbors.text()
        eigen_solver = self.ui.comboBox_eigen_solver.currentText()
        assign_labels = self.ui.comboBox_assign_labels.currentText()
        self.textEdit_info_panel.setText("cluster_number:"+cluster_number+"\tinit:"+init+"\tneighbors:"+neighbors+"\teigen_solver:"+eigen_solver+"\tassign_labels:"+assign_labels)
        self.label_result.setText("cluster_number:"+cluster_number+"\ninit:"+init+"\nneighbors:"+neighbors+"\neigen_solver:"+eigen_solver+"\nassign_labels:"+assign_labels)
        self.plot_initial_solution(self.plot.spectral_clustering(cluster_number,eigen_solver,init,neighbors,assign_labels))
    
    def assign_labels(self):
        cluster_number = self.ui.lineEdit_n_clusters.text()
        init = self.ui.lineEdit_n_init.text()
        neighbors = self.ui.lineEdit_n_neighbors.text()
        eigen_solver = self.ui.comboBox_eigen_solver.currentText()
        assign_labels = self.ui.comboBox_assign_labels.currentText()
        self.textEdit_info_panel.setText("cluster_number:"+cluster_number+"\tinit:"+init+"\tneighbors:"+neighbors+"\teigen_solver:"+eigen_solver+"\tassign_labels:"+assign_labels)
        self.label_result.setText("cluster_number:"+cluster_number+"\ninit:"+init+"\nneighbors:"+neighbors+"\neigen_solver:"+eigen_solver+"\nassign_labels:"+assign_labels)
        self.plot_initial_solution(self.plot.spectral_clustering(cluster_number,eigen_solver,init,neighbors,assign_labels))
    
    def spectral_clustering(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_SpectralClusteringWindow()
        self.ui.setupUi(self.window)
        self.ui.lineEdit_n_clusters.returnPressed.connect(self.cluster_number_spectral_clustering)
        self.ui.lineEdit_n_init.returnPressed.connect(self.init_number_spectral_clustering)
        self.ui.lineEdit_n_neighbors.returnPressed.connect(self.neighbors_number_spectral_clustering)
        self.ui.comboBox_eigen_solver.currentTextChanged.connect(self.eigen_solver)
        self.ui.comboBox_assign_labels.currentTextChanged.connect(self.assign_labels)
        self.window.show()
    
    # hierarcical_clustering
    def cluster_number_hierarcical_clustering(self):
        cluster_number = self.ui.lineEdit_num_clusters.text()
        linkage = self.ui.comboBox_linkage.currentText()
        self.plot_initial_solution(self.plot.hierarcical_clustering(cluster_number,linkage))
        self.textEdit_info_panel.setText("cluster_number:"+cluster_number+"\tlinkage:"+linkage)
        self.label_result.setText("cluster_number:"+cluster_number+"\nlinkage:"+linkage)
        
    def linkage__hierarcical_clustering(self):
        cluster_number = self.ui.lineEdit_num_clusters.text()
        linkage = self.ui.comboBox_linkage.currentText()
        self.plot_initial_solution(self.plot.hierarcical_clustering(cluster_number,linkage))
        self.textEdit_info_panel.setText("cluster_number:"+cluster_number+"\tlinkage:"+linkage)
        self.label_result.setText("cluster_number:"+cluster_number+"\nlinkage:"+linkage)
        
    def hierarcical_clustering(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_HiearchicalClusteringWindow()
        self.ui.setupUi(self.window)
        self.enable_action_after_clustering(True)
        self.ui.lineEdit_num_clusters.returnPressed.connect(self.cluster_number_hierarcical_clustering)
        self.ui.comboBox_linkage.currentTextChanged.connect(self.linkage__hierarcical_clustering)
        
        self.window.show()
    # dbscan
    def algorithm_dbscan(self):
        algorithm = self.ui.combobox_algorithm_d.currentText()
        eps = self.ui.lineEdit_eps.text()
        min_samples = self.ui.lineEdit_min_samples.text()
        self.textEdit_info_panel.setText("algorithm:"+algorithm+"\teps:"+eps+"\tmin_samples:"+min_samples)
        self.label_result.setText("algorithm:"+algorithm+"\neps:"+eps+"\nmin_samples:"+min_samples)
        self.plot_initial_solution(self.plot.dbscan(eps,min_samples,algorithm))
        
    def eps_dbscan(self):
        algorithm = self.ui.combobox_algorithm_d.currentText()
        eps = self.ui.lineEdit_eps.text()
        min_samples = self.ui.lineEdit_min_samples.text()
        self.textEdit_info_panel.setText("algorithm:"+algorithm+"\teps:"+eps+"\tmin_samples:"+min_samples)
        self.label_result.setText("algorithm:"+algorithm+"\neps:"+eps+"\nmin_samples:"+min_samples)
        self.plot_initial_solution(self.plot.dbscan(eps,min_samples,algorithm))
        
    def min_samples_dbscan(self):
        algorithm = self.ui.combobox_algorithm_d.currentText()
        eps = self.ui.lineEdit_eps.text()
        min_samples = self.ui.lineEdit_min_samples.text()
        self.textEdit_info_panel.setText("algorithm:"+algorithm+"\teps:"+eps+"\tmin_samples:"+min_samples)
        self.label_result.setText("algorithm:"+algorithm+"\neps:"+eps+"\nmin_samples:"+min_samples)
        self.plot_initial_solution(self.plot.dbscan(eps,min_samples,algorithm))
        
    def dbscan(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_DBSCANWindow()
        self.ui.setupUi(self.window)
        self.ui.combobox_algorithm_d.currentTextChanged.connect(self.algorithm_dbscan)
        self.ui.lineEdit_eps.returnPressed.connect(self.eps_dbscan)
        self.ui.lineEdit_min_samples.returnPressed.connect(self.min_samples_dbscan)
        
        self.window.show()
    
    #Menu : Heuristic
    
    def hill_climbing(self):
        pass
    def simulated_anneling(self):
        pass
    
if __name__ == "__main__":
    app = QApplication([])
    ex = MainWindow()
    
    ex.show()
    sys.exit(app.exec_())