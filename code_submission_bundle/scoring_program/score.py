#------------------------------------------
# Imports
#------------------------------------------
import sys
import os
import json
import numpy as np



#------------------------------------------
# Import Metric
#------------------------------------------
from metric import auc_metric


#------------------------------------------
# constants
#------------------------------------------
data_name = "fair_universe"

#------------------------------------------
# directories
#------------------------------------------
# Directory read predictions and solutions from
input_dir = '/app/input' 

# Directory to output computed score into
output_dir = '/app/output/'

# reference data (test labels)
reference_dir = os.path.join(input_dir, 'ref')  # Ground truth data

# submitted/predicted lables
prediction_dir = os.path.join(input_dir, 'res')

# score file to write score into
score_file = os.path.join(output_dir, 'scores.json') 



#------------------------------------------
# Read Predictions
#------------------------------------------
def read_prediction():
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
def read_solution():

    solution_file = os.path.join(reference_dir, 'test.labels')

    # Check if file exists
    if not os.path.isfile(solution_file):
        print('[-] Test solution file not found!')
        return

    f = open(solution_file, "r")
    
    test_labels = f.read().splitlines()
    test_labels = np.array(test_labels,dtype=float)

    return test_labels

def save_score(score):

    scores = {
        'auc': score,
    }
    with open(score_file, 'w') as f_score:
        f_score.write(json.dumps(scores))
        f_score.close()

def print_pretty(text):
    print("-------------------")
    print("#---",text)
    print("-------------------")


    
def main():


    #------------------------------------------
    # Read prediction and solution
    #------------------------------------------
    print_pretty('Reading prediction')
    prediction = read_prediction()
    solution = read_solution()


    #------------------------------------------
    # Compute Score
    #------------------------------------------
    print_pretty('Computing score')
    auc_score = auc_metric(solution, prediction)
    print("AUC Score :", auc_score)

    #------------------------------------------
    # Write Score
    #------------------------------------------
    print_pretty('Saving prediction')
    save_score(auc_score)



if __name__ == '__main__':
    main()