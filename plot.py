import matplotlib.pyplot as plt
import numpy as np

class Plot:
    def __init__(self,pairs,algorithm):
        self.pairs = pairs
        self.algorithm = algorithm
        self.label = self.algorithm.fit_predict(self.pairs)
        self.u_labels = np.unique(self.label)
        print(self.u_labels)
        self.plot_figure()
        
    def plot_figure(self):
        plt.clf()
        for i in self.u_labels:
            plt.scatter(self.pairs[self.label == i , 0] , self.pairs[self.label == i , 1] , label = i)
        self.count = np.shape(self.pairs)
        for i in range(self.count[0]):
            plt.annotate(i, (self.pairs[i,0], self.pairs[i,1]))
        plt.legend()
    
    def plot_source(self):
        self.filename_initial_solution = "initial_solution.png"
        plt.savefig(self.filename_initial_solution)
        return self.filename_initial_solution

    def plot_centroids(self,centers):
        self.centroids = centers
        plt.scatter(self.centroids[:,0] , self.centroids[:,1] , s = 80, color = 'k')
    
    def plot_mean_centers(self):

        for i in self.u_labels:
            center_x = sum(self.pairs[self.label == i , 0])/np.shape(self.pairs[self.label == i , 0])
            center_y = sum(self.pairs[self.label == i , 1])/np.shape(self.pairs[self.label == i , 1])
            plt.scatter(center_x , center_y, s = 80, color = 'k')
