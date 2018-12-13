import csv
import re
import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from collections import OrderedDict
from nltk.tokenize import PunktSentenceTokenizer
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

factori = StemmerFactory()
stemmer = factori.create_stemmer()
 
factory = StopWordRemoverFactory()
stopword = factory.create_stop_word_remover()

punctuations = '''‘!()–—[]{};:''’+""”“\\,<>./``?@#$%^&*|_~''' #-
df = pd.read_csv('./data_gemastik/data-all.csv')
arr_data = []
for i in range(len(df)):
    arr_kalimat = [df['judul'][i], df['konten'][i]]
    row = ""
    for indeks, j in enumerate(arr_kalimat):
        kalimat = ""
        lowcase_word = j.lower()                    #lowcase data perbaris
        stopw = stopword.remove(lowcase_word)
        # stemming = stemmer.stem(stopw)
        tokens = word_tokenize(stopw)          #Tokenisasi Kalimat
        for k, kata in enumerate(tokens):
            string = ""
            for huruf in kata:
                if huruf not in punctuations:
                    if huruf == '-':
                        string += ' '
                    else:
                        string += huruf
            if k == len(tokens)-1:
                kalimat += string
            else:
                kalimat += string + ' '
        # if indeks != len(arr_kalimat)-1:
        #     kalimat += ', '
        row += kalimat
    # cleans = re.sub('\\+',' ',row)
    clean = re.sub(' +',' ',row)
    arr_data.append(clean)
df2 = pd.DataFrame(arr_data)
df2.to_csv('./input/data-bersih.csv', index=False)
print(df2)
            

'''
arr_praproses =[]

with open ('./data_gemastik/data-all.csv', 'r') as input :
    reader = input.read().split("\n")               #Akses data per baris
    for indeks in range(len(reader)):
        lowcase_word = reader[indeks].lower()       #lowcase data perbaris
        stopw = stopword.remove(lowcase_word)
        stemming = stemmer.stem(stopw)
        tokenizer = RegexpTokenizer(r'\w+')         #remove punctuatuion
        tokens = tokenizer.tokenize(stemming)   #Tokenisasi Kalimat
        # filtered_words = [w for w in tokens if not w in stopwords.words('english')]     #remove Stopwords
        output = []       
        print(tokens)                          #nampung hasil stemming dulu
        for kata in tokens:
            output.append(kata) #proses stemming per-kata dalam 1 kalimat
        arr_praproses.append(output)                #tampung kalimat hasil stemm ke arr_praproses


out = open('./input/data-all-clean.csv', 'w')                        #Open file .csv buat nampung data
for j in range(len(arr_praproses)):
    print (" ".join(arr_praproses[j]))
    out.write(" ".join(arr_praproses[j]) + '\n')
out.close()

'''
# print (len(arr_praproses))