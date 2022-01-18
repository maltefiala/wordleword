
import pickle
import nltk
import streamlit as st

st.write("""
#Wordle starting word
The default settings will show you the best starting word based on
occurence frequency of letters in 5 letter words.
""")

with open('fivel.pkl', 'rb') as f:
    fivel = pickle.load(f)

fives = ''.join(fivel)

myFD = nltk.FreqDist(fives)

mostletters=''
for x in myFD.most_common(6):
  mostletters += x[0]

#myFD.plot()

bestl = nltk.FreqDist(mostletters)

yourwords=[w for w in fivel if nltk.FreqDist(w) <= bestl]

yourwords
