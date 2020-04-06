import pandas as pd
import numpy as np


#Step 1: Read the input data. This should have been from the database
data = pd.read_csv('input_data.csv')

#Step 2: Check the output data stored in the database 
#and only take reponse ids that do not have a response assigned.  
data = data[data['response'].isnull()]
print(f"We have {data.shape[0]} respondants without \
                  an assigned probability")

#Step 3: Assign a response
data['response'] = np.random.rand(len(data)) #Toy example

# STep4: Store the data into the database
data[['Respondent ID', 'response']].to_csv('output_data.csv', index = False)
# STep 5: Send the email