import pandas as pd
import numpy as np
import streamlit as st
from summarizer import Summarizer
from summarizer import Summarizer
model=Summarizer()
#loaded_model = load(open('Summarizer.sav', 'rb')
  
def ATTORNEY_prediction(input_data):
                    
#       input_data_as_numpy_array = np.asarray(input_data) 
   
#       input_data_reshaped = input_data_as_numpy_array.reshape(1-1)
                    
#       prediction = loaded_model.predict(input_data_reshaped
#       print(prediction)

        summary=model(input_data)
        print(summary)
        return summary

def main():
                                        
         #giving a title
    st.title('Model Deployment: Bert Model')
                                       
    input_text=st.text_input('Insert Text')                                    
        #code for prediction
    diagnosis = ''
        
     #Creating a button for prediction
    if st.button('ATTORNEY Test Result'):
        diagnosis = ATTORNEY_prediction(input_text)
                                        
    st.success(diagnosis)
                                        
if __name__ == '__main__':
   main()                                     