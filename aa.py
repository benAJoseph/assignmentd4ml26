import matplotlib.pyplot as plt 
import pandas as pd
import streamlit as st
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
#matplotlib.use('Agg')
import seaborn as sns 

st.set_option('deprecation.showPyplotGlobalUse', False)

df = pd.read_csv('test.csv')

st.title("Air Travel Customer Satisfaction")

st.header("Using NumPy, Pandas, Seaborn with Streamlit and deplying with Heroku")

st.subheader("Flight Distance VS Seat Class")
sns.catplot(x="Class", y="Flight Distance", hue="satisfaction",
            kind="violin", split=True, data=df)
st.pyplot()

st.subheader("OverAll Satisfaction VS Age of customer")
sns.catplot(x = "satisfaction" , y= "Age", hue = "Customer Type", kind="box", data = df)
st.pyplot()

st.subheader("Seat Comfort VS Age of customer")
sns.catplot(x="Seat comfort", y="Age", hue="Type of Travel",
            kind="violin", split=True, data=df)
st.pyplot()

st.subheader("Summary Plot")
sns.pairplot(df, hue="Customer Type")
st.pyplot()