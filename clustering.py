import matplotlib.pyplot as plt
import numpy as np
from sklearn.cluster import KMeans
from sympy import centroid
from sklearn.cluster import AffinityPropagation
from sklearn.cluster import MeanShift
from sklearn.cluster import SpectralClustering
from sklearn.cluster import AgglomerativeClustering
from sklearn.cluster import DBSCAN

from plot import Plot
class Clusters:
    def __init__(self,file_source,open_mode = "r"):
        self.source = file_source
        self.mode = open_mode
        self.xc = []
        self.yc = []
        self.count = []
        count = 0
        with open(self.source,mode=self.mode) as f:
            for line in f:                
                x_c, y_c = line.split()
                self.xc.append(x_c)
                self.yc.append(y_c)
                self.count.append(count)
                count+=1
        self.x = np.array(self.xc)
        self.y = np.array(self.yc)
        self.x = self.x.astype(np.float32)
        self.y = self.y.astype(np.float32)
        self.pairs = np.vstack((self.x,self.y)).T
        
    def get_points(self):
        return self.pairs
    
    def get_initial_solution_source(self):
        plt.clf()
        plt.scatter(self.x , self.y , c="black")
        for i, txt in enumerate(self.count):
            plt.annotate(i, (self.x[i], self.y[i]))
            
        self.filename_initial_solution = "initial_solution.png"
        plt.savefig(self.filename_initial_solution)
        return self.filename_initial_solution
    
    def k_means(self,cluster_n=8 ,init = 'k-means++',max_iter = 300 ,algorithm = 'lloyd'):
        plt.clf()
        clustering = KMeans(n_clusters=int(cluster_n),init=init,max_iter=int(max_iter), algorithm=algorithm)
        source = Plot(self.pairs,clustering)
        source.plot_centroids(clustering.cluster_centers_)
        return source.plot_source()
    def affinity_propagation(self,damping=0.5,max_iter=200,affinity= "euclidean",random_state=0):
        plt.clf()
        clustering = AffinityPropagation(damping=float(damping),max_iter=int(max_iter),affinity=affinity,random_state=int(random_state)).fit(self.pairs)
        source = Plot(self.pairs,clustering)
        source.plot_centroids(clustering.cluster_centers_)
        return source.plot_source()

    def mean_shift(self,bandwidth,bin_seeding,max_iter):
        plt.clf()
        clustering = MeanShift(bandwidth=int(bandwidth),bin_seeding=bin_seeding,max_iter=int(max_iter)).fit(self.pairs)
        source = Plot(self.pairs,clustering)
        centers = source.plot_mean_centers()
        return source.plot_source()
    
    def spectral_clustering(self,n_clusters=8,eigen_solver="None",n_init=10,n_neighbors=10,assign_labels="kmeans"):
        plt.clf()
        clustering = SpectralClustering(n_clusters=int(n_clusters),eigen_solver=eigen_solver,n_init=int(n_init),n_neighbors=int(n_neighbors),assign_labels=assign_labels).fit(self.pairs)
        source = Plot(self.pairs,clustering)
        centers = source.plot_mean_centers()
        return source.plot_source()
        
    def hierarcical_clustering(self,cluster_number=2,linkage = "ward"):
        plt.clf()
        clustering = AgglomerativeClustering(n_clusters=int(cluster_number), affinity='euclidean', linkage=str(linkage)).fit(self.pairs)
        source = Plot(self.pairs,clustering)
        source.plot_mean_centers()
        return source.plot_source()
        
    def dbscan(self,eps=0.5,min_sample=5,algorithm="auto"):
        plt.clf()
        clustering = DBSCAN(eps=float(eps), min_samples=int(min_sample),algorithm=str(algorithm)).fit(self.pairs)
        source = Plot(self.pairs,clustering)
        centers = source.plot_mean_centers()
        return source.plot_source()