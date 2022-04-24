import random as r
import pandas as pd
import streamlit as st
import csv
def app(sub):
    s = st.container()
    df = pd.read_csv(sub+'.csv')

    q1 = df.index[df['Difficulty'] == 3].tolist()
    l_q1 = r.sample(q1,6)
    s.title("Question Paper : "+sub.upper())
    s.header("(1) Attempt any five of the following: ")
    s.write("(20 marks each)")
    c = 1
    for i in l_q1:
        s.text('Q'+str(c)+'. '+df.loc[i,'Questions'])
        c+=1
