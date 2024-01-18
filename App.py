import streamlit as st
import pandas as pd
import pickle

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

st.title('Iris Flower Prediction App')

sepal_length = st.slider('Sepal Length (cm)', 4.0, 8.0, 5.0)
sepal_width = st.slider('Sepal Width (cm)', 2.0, 4.5, 3.5)
petal_length = st.slider('Petal Length (cm)', 1.0, 7.0, 4.0)
petal_width = st.slider('Petal Width (cm)', 0.1, 2.5, 1.3)

if st.button('Predict Iris Flower Type'):
    input_data = pd.DataFrame({
        'sepal_length': [sepal_length],
        'sepal_width': [sepal_width],
        'petal_length': [petal_length],
        'petal_width': [petal_width]
    })

    prediction = model.predict(input_data)

    st.success(f'The predicted Iris flower type is: {prediction[0]}')

st.markdown("NIM: 20202230095")
st.markdown("Name: Ghina Ayu AUdreina")