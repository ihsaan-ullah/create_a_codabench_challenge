#------------------------------------------
# Imports
#------------------------------------------

import sys
from sys import argv
import os
import os.path
import json
import numpy as np
import pandas as pd




#------------------------------------------
# Import Metric
#------------------------------------------
from metric import auc_metric


#------------------------------------------
# constants
#------------------------------------------
data_name = "fair_universe"



#------------------------------------------
# Read Predictions
#------------------------------------------
def read_prediction(prediction_dir):
    prediction_file = os.path.join(prediction_dir,'test.predictions')


    # Check if file exists
    if not os.path.isfile(prediction_file):
        print('[-] Test prediction file not found!')
        return


    f = open(prediction_file, "r")
    
    predicted_scores = f.read().splitlines()
    predicted_scores = np.array(predicted_scores,dtype=float)
    
    return predicted_scores

#------------------------------------------
# Read Solutions
#------------------------------------------
def read_solution(reference_dir):

    solution_file = os.path.join(reference_dir, 'test.labels')

    # Check if file exists
    if not os.path.isfile(solution_file):
        print('[-] Test solution file not found!')
        return

    f = open(solution_file, "r")
    
    test_labels = f.read().splitlines()
    test_labels = np.array(test_labels,dtype=float)

    return test_labels

def save_score(score_dir, score):

    score_file = os.path.join(score_dir, 'scores.json')

    scores = {
        'auc': score,
    }
    with open(score_file, 'w') as f_score:
        f_score.write(json.dumps(scores))
        f_score.close()
    
def main():


    #------------------------------------------
    # Read Args
    #------------------------------------------
    input_dir = argv[1]
    output_dir = argv[2]

    reference_dir = os.path.join(input_dir, 'ref')
    prediction_dir = os.path.join(input_dir, 'res')


    #------------------------------------------
    # Read prediction and solution
    #------------------------------------------
    prediction = read_prediction(prediction_dir)
    solution = read_solution(reference_dir)


    #------------------------------------------
    # Compute Score
    #------------------------------------------
    auc_score = auc_metric(solution, prediction)
    print("AUC Score :", auc_score)

    #------------------------------------------
    # Write Score
    #------------------------------------------
    save_score(output_dir, auc_score)



if __name__ == '__main__':
    main()