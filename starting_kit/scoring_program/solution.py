import os
import pandas as pd


# ================ Small auxiliary functions =================

def read_solutions(data_dir):
    ''' Function to read the Labels from CSV files'''


    #----------------------------------------------------------------
    # Settings
    #----------------------------------------------------------------
    TRAIN_CSV_PATH = os.path.join(data_dir,"train.csv")
    TEST_CSV_PATH = os.path.join(data_dir,"test.csv")
    
    
    #----------------------------------------------------------------
    # Errors
    #----------------------------------------------------------------

    # Check TRAIN file
    if not os.path.isfile(TRAIN_CSV_PATH):
        print('[-] Train csv file not found!')
        return

    # Check TEST file
    if not os.path.isfile(TEST_CSV_PATH):
        print('[-] Test csv file not found!')
        return
    



    
    #----------------------------------------------------------------
    # Read CSVs
    #----------------------------------------------------------------
    train_df = pd.read_csv(TRAIN_CSV_PATH)
    test_df = pd.read_csv(TEST_CSV_PATH)
         
   
    
    
    
    
    
    print("###-------------------------------------###")
    print("### Train solutions : ", train_df.shape[0])
    print("### Test solutions : ", test_df.shape[0])
    print("###-------------------------------------###\n\n")
    

    #----------------------------------------------------------------
    # Separate labels and features
    #----------------------------------------------------------------
    
    y_train = train_df['label']
    y_test = test_df['label']
    
    
    solutions = [y_train, y_test]
    solution_names = ['train', 'test']
    
    
    return (solution_names,solutions)


