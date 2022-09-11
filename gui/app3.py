import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

@st.cache
def load_data():
    url='https://github.com/digipodium/Datasets/blob/main/regression/dataB.csv'
    df=pd.read_csv(url)
    return df
df=load_data()
st.header("Data science app")
if(st.checkbox("see raw data")):
    st.dataframe(df)
vis_ops=['2D vis','3 D Vis']
columns=df.columns.tolist()
choice=st.sidebar.radio("slect an option",vis_ops)
if choice==vis_ops[0]:
  x=st.sidebar.selectbox('Selct column for x',columns)
  y=st.sidebar.selectbox('Selct column for x',columns)
  fig=px.scatter(df,x,y,color=x)
  st.plotly_chart(fig,use_container_width=True)
