import sklearn
import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('D:/Ml Project/trained_model.sav','rb'))

def diabetes_prediction(input_data):
    input_data = ( 4,110,92,0,0,37.6,0.191,30)
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)
    if (prediction[0]==0):
      return'the person is not diabetic'
    else:
     return'the person is diabetic'
     
def main():
    
    #giving a title
    st.title('diabetes prediction web app')
    
    
    #getting input data from user
    
    
    pregnancies = st.text_input('number of pregnancies')
    Glucose = st.text_input('glucose level ')
    BloodPressure= st.text_input('level of BloodPressure')
    SkinThickness= st.text_input('number of SkinThickness') 
    Insulin = st.text_input('number of Insulin ')
    BMI= st.text_input('number of BMI ')
    DiabetesPedigreeFunction = st.text_input('number of DiabetesPedigreeFunction ')
    Age = st.text_input('age of person ')
    
    #code for prediction
    diagnosis=''
    # cretaing the button
    if st.button('diabetes test result'):
        diagnosis = diabetes_prediction([pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age])
        
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
        
        