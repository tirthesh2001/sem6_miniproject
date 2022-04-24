import requests
from bs4 import BeautifulSoup
import csv 
import re
import random as r
def app():
    trry = "interview-questions/"
    page = requests.get(
        "https://intellipaat.com/blog/"+trry)
    soup = BeautifulSoup(page.content, 'html.parser')

    all_p_tags = []
    questions = []
    for element in soup.select('ul li a'):
      all_p_tags.append(element.get('href'))

    for i in all_p_tags:
      page = requests.get(i)
      soup = BeautifulSoup(page.content, 'html.parser')
      for ql in soup.select('h3 strong'):
        x = ql.text
        x = x.lstrip(".1234567890")
        x = x.lstrip(" ")
        if x not in questions and x != '':
          questions.append(x)

    fields = ['Questions','Difficulty']
    rows = []
    for i in questions:
      rows.append([i,r.randint(1,3)])

    filename = "question_set.csv"
    with open(filename, 'w') as csvfile:
      csvwriter = csv.writer(csvfile) 
            
        # writing the fields 
      csvwriter.writerow(fields) 
            
        # writing the data rows 
      csvwriter.writerows(rows)
