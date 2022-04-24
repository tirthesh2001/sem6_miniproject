import random as r
import pandas as pd
import streamlit as st
import csv

def app(sub): 
    s = st.container()
    df = pd.read_csv(sub+".csv")

    q2 = df.index[df['Difficulty'] == 2].tolist()
    l_q2 = r.sample(q2,5)
    s.title("Question Paper : "+sub.upper())
    s.header("(1) Attempt any four of the following: ")
    s.write('(10 marks each)')
    c1=1
    for i in l_q2:
        s.write('Q'+str(c1)+'. '+df.loc[i,'Questions'])
        c1+=1

    q3 = df.index[df['Difficulty'] == 3].tolist()
    l_q3 = r.sample(q3,4)
    s.header("(2) Attempt any three of the following: ")
    s.write('(20 marks each)')
    c2=1
    for i in l_q3:
        s.write('Q'+str(c2)+'. '+df.loc[i,'Questions'])
        c2+=1
