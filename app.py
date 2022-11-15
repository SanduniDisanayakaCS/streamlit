# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 01:37:21 2022

@author: HP
"""

import numpy as np
import pickle
import streamlit as st

loaded_model = pickle.load(open('C:/Users/HP/Desktop/satisfaction_research/satisfaction_model.sav', 'rb'))

#Creating a function for Prediction

def satisfaction_prediction(input_data):
    
   
    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return'Low Satisfaction'
      

      from gtts import gTTS
      import os
      myText ="Low Satisfaction"
      language ='en'
      output =gTTS(text=myText, lang=language,slow=False)
      output.save("output.mp3")
      os.system("start output.mp3")
    if (prediction[0] == 1):
      return'Medium Satisfaction'
      
      from gtts import gTTS
      import os
      myText ="Medium Satisfaction"
      language ='en'
      output =gTTS(text=myText, lang=language,slow=False)
      output.save("output.mp3")
      os.system("start output.mp3")
    if(prediction[0])==2:
      return'High Satisfaction'
      
      from gtts import gTTS
      import os
      myText ="High Satisfaction"
      language ='en'
      output =gTTS(text=myText, lang=language,slow=False)
      output.save("output.mp3")
      os.system("start output.mp3")


def main():
    
    # giving a Title 
    st.title('Satisfaction Prediction web App')
    
    #getting input data from the user
    
    #Amplitude,Variance,Kurtosis,RMS,F.score,Mean,Skew ,Phase,
    
    Amplitude=st.text_input('Amplitude range')
    Variance=st.text_input('Variance range')
    Kurtosis=st.text_input('Kurtosis range')
    RMS=st.text_input('RMS range')
    FScore=st.text_input('Fscore range')
    Mean=st.text_input('Mean range')
    Skew=st.text_input('Skew range')
    Phase=st.text_input('Phase range')
    
    #code for Prediction
    
    satisfaction =''
    
    # Creating a button for Prediction
    
    if st.button('Satisfaction Test Result'):
        satisfaction =satisfaction_prediction([ Amplitude,Variance,Kurtosis,RMS,FScore,Mean, Skew,Phase])
    st.success(satisfaction)
    
if __name__=='__main__':
    main()
  
    
    
    
    