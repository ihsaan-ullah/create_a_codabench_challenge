#------------------------------------------
# Imports
#------------------------------------------
import argparse
import os
import sys
import numpy as np
import pandas as pd 


#------------------------------------------
# Import Model
#------------------------------------------
from model import Model



#------------------------------------------
# Directories
#------------------------------------------
input_dir = '/app/input_data/'
output_dir = '/app/output/'
program_dir = '/app/program'
submission_dir = '/app/ingestion_program'

sys.path.append(program_dir)
sys.path.append(submission_dir)


#------------------------------------------
# Directories
#------------------------------------------

#------------------------------------------
# Read Train Data
#------------------------------------------
def get_training_data(input_dir):


    # set train data and solution file
    train_data_file = os.path.join(input_dir, 'train.csv')
    train_solution_file = os.path.join(input_dir, 'train.labels')
    
    # Read Train data
    X_train = pd.read_csv(train_data_file)

    # Read Train solution
    f = open(train_solution_file, "r")
    y_train = f.read().splitlines()
    y_train = np.array(y_train,dtype=float)


    return X_train, y_train

#------------------------------------------
# Read Test Data
#------------------------------------------
def get_prediction_data(input_dir):

    # set test data and solution file
    test_data_file = os.path.join(input_dir, 'test.csv')

    # Read Test data
    X_test = pd.read_csv(test_data_file)

    return X_test

#------------------------------------------
# Save Predictions
#------------------------------------------
def save_prediction(output_dir, prediction_prob):

    prediction_file = os.path.join(output_dir, 'test.predictions')

    predictions = prediction_prob[:,1]

    with open(prediction_file, 'w') as f:
        for ind, lbl in enumerate(predictions):
            str_label = str(int(lbl))
            if ind < len(predictions)-1:
                f.write(str_label + "\n")
            else:
                f.write(str_label)

    

#------------------------------------------
# Run the pipeline 
# > Load 
# > Trein 
# > Predict 
# > Save
#------------------------------------------
def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("input_dir")
    parser.add_argument("output_dir")
    args = parser.parse_args()

    input_dir = args.input_dir
    output_dir = args.output_dir

    print('#--- Reading Data ---#')
    X_train, y_train = get_training_data(input_dir)
    X_test = get_prediction_data(input_dir)


    print('#--- Starting Learning ---#')
    m = Model()

    print('#--- Training Model ---#')
    m.fit(X_train, y_train)

    print('#--- Running Prediction ---#')
    prediction_prob = m.predict_score(X_test)

    print('#--- Saving Prediction ---#')
    save_prediction(output_dir, prediction_prob)


if __name__ == '__main__':
    main()