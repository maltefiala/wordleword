
import pickle
import nltk
import pandas as pd
import streamlit as st

st.write("""
# Wordle word finder
The default settings will show you the best starting word based on
occurence frequency of letters in 5 letter words.
""")

with open('fivel.pkl', 'rb') as f:
    fivel = pickle.load(f)

fives = ''.join(fivel)

myFD = nltk.FreqDist(fives)

df_myFD = pd.DataFrame.from_dict(myFD, orient='index')


st.write("## General Letter Distribution")

st.bar_chart(df_myFD)


st.write("## Chosen letter distribution (ranked)")

mostcommon_count = st.slider('Chose how many letters you want to graph (ranked)', 0, 26, 6)
mostcommon_list = myFD.most_common(mostcommon_count)
mostcommon_dict = {}
for item in mostcommon_list:
    mostcommon_dict[item[0]]=item[1]

df_mostcommon_dict = pd.DataFrame.from_dict(mostcommon_dict, orient='index')
st.bar_chart(df_mostcommon_dict)

mostcommon_letters=''
for x in mostcommon_list:
    mostcommon_letters += x[0]


st.write("## Chose letters for word creation")
myletters = st.text_input('Letters shown per default are your chosen  common letters', value=mostcommon_letters)

bestl = nltk.FreqDist(myletters)

yourwords=[w for w in fivel if nltk.FreqDist(w) <= bestl]


st.write("## Words created")

yourwords
