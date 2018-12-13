import pandas as pd

def buat_dict(data):
    vocab = {}
    with open(data, 'r') as f:
        reader = f.read().split('\n')
        for kata in reader:
            vocab[kata] = 1
    return vocab

df = pd.read_csv('./input/data-bersih.csv')
positif = buat_dict('./sentimen/positive.csv')
negatif = buat_dict('./sentimen/negative.csv')
jokowi = buat_dict('./sentimen/jokowi.csv')
prabowo = buat_dict('./sentimen/prabowo.csv')
for i, row in enumerate(df['sentences']):
    neg, pos, jok, pra = 0, 0, 0, 0
    kalimat = row.split(' ')
    for j, kata in enumerate(kalimat):
        if j < len(kalimat)-1:
            dua_kata = kalimat[j]+' '+kalimat[j+1]
            if dua_kata in negatif:
                neg += 1
            if dua_kata in positif:
                pos += 1
            if dua_kata in jokowi:
                jok += 1
            if dua_kata in prabowo:
                pra += 1
        if j < len(kalimat)-2:
            tiga_kata = kalimat[j]+' '+kalimat[j+1]+' '+kalimat[j+2]
            if tiga_kata in negatif:
                neg += 1
            if tiga_kata in positif:
                pos += 1
            if tiga_kata in jokowi:
                jok += 1
            if tiga_kata in prabowo:
                pra += 1
        if kata in negatif:
            neg += 1
        if kata in positif:
            pos += 1
        if kata in jokowi:
            jok += 1
        if kata in prabowo:
            pra += 1
    print(i+1,' Negatif :',neg, ' ','Positif :',pos, ' ','Jokowi :',jok, ' ','Prabowo :',pra)