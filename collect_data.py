import glob
import errno
import os
import csv
from xml.etree import ElementTree
import operator
import pandas as pd

path = './data_gemastik/data-all.csv'      #Cara akses semua data yang ada di file /data/train
files = glob.glob(path)
out = open('./data_gemastik/data-all2.csv', 'w')
# out.write('att1' +'\t'+ 'att2' + '\n')
for name in files:      #Looping file .xml yang ada di file /data/train
    # print(name)
    try:      
        # hasil =[] #Wadah buat write csvnya dikosongin lagi biar biasa beda baris
        # dom = ElementTree.parse(name) #ngeparser datanya jadi tree
        # isi = dom.findall('text/p') #akses text yang didalam tag <p> ... </p>

        # for i in isi:
        #     hasil.append(i.text)

        with open (name, 'r') as inputan :
            reader = inputan.read().split("\n")               #Akses data per baris
            for indeks in range(len(reader)):
                out.write(name[30:-4] + '\t' + reader[indeks] + '\n')
                # print(reader[indeks])
        # out.write('\n') #buat misahin setiap data dibeda baris
        
    except IOError as exc:
        if exc.errno != errno.EISDIR:
            raise
out.close()
# print (len(files))

#================= SORTING DATA BERDASARKAN KOLOM KE-1 =====================#
'''
sample = open('data-awal-test.csv','r')

csv1 = csv.reader(sample, delimiter='\t')

sort = sorted(csv1, key=operator.itemgetter(0))

out = open('data_sorted_test.csv', 'w')
for count in range(len(sort)):
    del (sort[count][0]) # Hapus Colom Ke-1
    out.write(" ".join(sort[count]) + '\n') #buat misahin setiap data dibeda baris
out.close()
'''