import nltk
nltk.download('words')
nltk.download('names')

from nltk.corpus import words, names

word_list = words.words()
name_list = names.words()

fivel = []
for word in word_list:
    if (len(word)==5):
      fivel.append(word.lower())

for name in name_list:
    for word in fivel:
      if (name.lower() == word):
          fivel.remove(word)

import pickle

with open('fivel.pkl', 'wb') as f:
    pickle.dump(fivel, f)

print (len(fivel))
