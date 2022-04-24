import random as r
import pandas as pd
import streamlit as st
import csv
def app(sub):
    s = st.container()
    df = pd.read_csv(sub+'.csv')

    q1 = df.index[df['Difficulty'] == 1].tolist()
    l_q1 = r.sample(q1,22)
    s.title("Question Paper: "+sub.upper())
    s.header("(1) Attempt any 20 of the following: ")
    s.write("(5 marks each)")
    c=1
    for i in l_q1:
        s.write('Q'+str(c)+'. '+df.loc[i,'Questions'])
        c+=1
