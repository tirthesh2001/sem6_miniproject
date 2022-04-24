import random as r
import pandas as pd
import streamlit as st
import csv
from PIL import Image

import medium
import hard_qb
import easy_qb
import bhai_fail
import isme_full

def space(ele,num):
    for i in range(num):
        ele.text(" ")

st.set_page_config(page_title='QPM-IT-A-18',page_icon="qmaker.png", menu_items={
         'Get Help' : 'https://www.extremelycoolapp.com/help',
         'About': '''Implementation of semester 6 mini project\n
                     Project Guide : Prof. Rohit Barve\n
                     Team :
                     Sameep Sawant : 20101A2001
                     Atharva Panvalkar : 20101A2005
                     Tirthesh Patil : 20101A2009
                     Sanchit Jadhav : 20101A2010'''}
                   )
                   
read_ai = pd.read_csv('ai.csv')
read_ai.sort_values(["Difficulty"])

read_os = pd.read_csv('os.csv')
read_os.sort_values(["Difficulty"])

read_sql = pd.read_csv('sql.csv')
read_sql.sort_values(["Difficulty"])

read_ds = pd.read_csv('ds.csv')
read_ds.sort_values(["Difficulty"])

read_other = pd.read_csv('other.csv')
read_other.sort_values(["Difficulty"])

cont_title = st.container()
col1, col2 = st.columns([1,20])
logo = Image.open('qmaker.png')
with cont_title:
    with col1:
        st.image(logo, width=120)
    with col2:
        st.markdown('<h1 style="color:#a5f5ff; float: right;"><u>Question Paper Maker</u></h1>',unsafe_allow_html=True)

cont1 = st.container()
cont2 = st.container()
cont3 = st.container()
cont1.subheader("Make your selections:-")

sel_sub = cont1.selectbox('Select the subject for the paper: ',('AI', 'OS', 'SQL', 'DS', 'Other'))
space(cont1,2)

marks = cont1.number_input('Enter your previous marks: ', max_value = 100)
cont1.caption('Marks out of 100')
space(cont1,4)

show = cont1.button("Display Question Bank")
if show:
    if sel_sub == 'AI':
        cont2.write(read_ai.sort_values(["Difficulty"]))
    elif sel_sub == 'OS':
        cont2.write(read_os.sort_values(["Difficulty"]))
    elif sel_sub == 'SQL':
        cont2.write(read_sql.sort_values(["Difficulty"]))
    elif sel_sub == 'DS':
        cont2.write(read_ds.sort_values(["Difficulty"]))
    elif sel_sub == 'Other':
        cont2.write(read_other.sort_values(["Difficulty"]))
space(cont2,1)
gen = cont3.button("Generate Paper")
if gen:
    f1 = open("record.txt","r")
    rec = [float(i) for i in f1.read().split("\n")]
    prev_marks = rec[0]
    diff = rec[1]
    f1.close()
    if (prev_marks < marks):
        if diff !=5:
            diff+=1
        else:
            diff = 5
    elif (prev_marks > marks):
        if diff != 1:
            diff-=1
        else:
            diff = 1
    elif (prev_marks == marks):
        diff = diff
    else:
        cont3.write("Invalid Entry")

    f2 = open("record.txt","w+")
    f2.write(str(marks)+'\n')
    f2.write(str(diff))

    if (diff == 1):
        isme_full.app(sel_sub.lower())
    elif (diff == 2):
        easy_qb.app(sel_sub.lower())
    elif (diff == 3):
        medium.app(sel_sub.lower())
    elif (diff == 4):
        hard_qb.app(sel_sub.lower())
    elif (diff == 5):
        bhai_fail.app(sel_sub.lower())
    

