import streamlit as st
import joblib
model = joblib.load('Diabetes Prediction')
st.title('Diabetes Prediction')
ip1 = st.number_input('Enter Number of pregnancies')
ip2 = st.number_input('Enter Glucose level in blood')
ip3 = st.number_input('Enter the Blood pressure measurement')
ip4 = st.number_input(' Enter thickness of the skin')
ip5 = st.number_input('Enter Insulin level in blood')
ip6 = st.number_input('Enter Body mass index')
ip7 = st.number_input('Enter Diabetes percentage(DiabetesPedigreeFunction)')
ip8 = st.number_input('Enter Age')
#It creates a text box in the webapp
op = model.predict([[ip1,ip2,ip3,ip4,ip5,ip6,ip7,ip8]])
if st.button('Predict'):
  if (op==1):
     st.title('Patient is diagonsed to have symtoms of Diabetes')
  if (op==0):
     st.title('NO WORRIES!there are no such symtoms diagonsed by Patient')
