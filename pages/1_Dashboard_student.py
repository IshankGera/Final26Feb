import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from matplotlib import image
import plotly.express as px
import seaborn as sns
df = pd.read_csv('student.csv')
st.title("Student Dashboard")
st.image("iris.jpg")
st.dataframe(df)

gender = st.selectbox("Select the gender:",df['Sex'].unique())


fig1 = px.histogram(df[df['Sex']==gender],x='Marks(out of 100)',y='Marks(out of 100)')
st.plotly_chart(fig1, use_container_width=True)

fig2 = px.scatter(df[df['Sex']==gender],x='Attendance(out of 100)')
st.plotly_chart(fig2, use_container_width=True)

fig3 = px.scatter(df[df['Sex']==gender],y='Attendance(out of 100)')
st.plotly_chart(fig3, use_container_width=True)

fig4 = px.line(df[df['Sex']==gender],x='Attendance(out of 100)' ,y='Marks(out of 100)')
st.plotly_chart(fig4, use_container_width=True)

fig5 = px.bar(df[df['Sex']==gender],x='Attendance(out of 100)' ,y='Marks(out of 100)')
st.plotly_chart(fig5, use_container_width=True)