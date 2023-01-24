# Model file which contains a model class in scikit-learn style
# Model class must have these 4 methods
# - fit: trains the model.
# - predict: uses the model to perform predictions.
# - save: saves the model.
# - load: reloads the model.

# Created by: Ihsan Ullah
# Created on: 01 Dec, 2022

#----------------------------------------
# Imports
#----------------------------------------
import pickle
import numpy as np
from os.path import isfile
from sklearn.base import BaseEstimator
from sklearn import tree

#----------------------------------------
# Model Class
#----------------------------------------
class model (BaseEstimator):
    
    def __init__(self):
        """
        This is a constructor for initializing class variables

        Parameters
        ----------
        None

        Returns
        -------
        None
        """
        self.num_train_samples=0
        self.num_feat=1
        self.num_labels=1
        self.is_trained=False
        self.clf = tree.DecisionTreeClassifier()

    def fit(self, X, y):
        """
        This function trains the model provided training data

        Parameters
        ----------
        X: 2D numpy array
            training data matrix of dimension num_train_examples * num_features
            each column is a feature and each row a datapoint
        y: 1D numpy array
            training label matrix of dimension num_train_samples
        
        Returns
        -------
        None
        """


        self.num_train_samples = X.shape[0]
        if X.ndim > 1: 
            self.num_feat = X.shape[1]

        print("FIT: dim(X)= [{:d}, {:d}]".format(self.num_train_samples, self.num_feat))
        
        num_train_labels = y.shape[0]
        if y.ndim > 1: 
            self.num_labels = y.shape[1]
        else:
            self.num_labels = len(np.unique(y))
        
        if (self.num_train_samples != num_train_labels):
            print("[-] ARRGH: number of samples in X and y do not match!")
            return

        self.clf.fit(X,y)

        self.is_trained=True

    def predict(self, X):

        """
        This function predicts labels on test data.

        Make sure that the predicted values are in the correct format for the scoring
        metric. For example, binary classification problems often expect predictions
        in the form of a discriminant value (if the area under the ROC curve it the 
        metric) rather that predictions of the class labels themselves. For multi-class
        or multi-labels problems, class probabilities are often expected if the metric
        is cross-entropy.
        Scikit-learn also has a function predict-proba, we do not require it.
        The function predict eventually can return probabilities.

        Parameters
        ----------
        X: 2D numpy array
            test data matrix of dimension num_test_examples * num_features
            each column is a feature and each row a datapoint
        
        
        Returns
        -------
        y: 1D numpy array
            predicted labels
        """

        num_test_samples = X.shape[0]

        if X.ndim > 1: 
            num_feat = X.shape[1]
        print("PREDICT: dim(X)= [{:d}, {:d}]".format(num_test_samples, num_feat))
        
        if (self.num_feat != num_feat):
            print("[-] ARRGH: number of features in X does not match training data!")
            return 
        
        
        y = self.clf.predict(X)
        
        return y

    def save(self, path="./"):
        pickle.dump(self, open(path + '_model.pickle', "wb"))

    def load(self, path="./"):
        modelfile = path + '_model.pickle'
        if isfile(modelfile):
            with open(modelfile, 'rb') as f:
                self = pickle.load(f)
            print("Model reloaded from: " + modelfile)
        return self
