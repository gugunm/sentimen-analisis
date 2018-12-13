import pandas as pd
df = pd.read_csv('./input/data-bersih.csv')
out = open('./input/bagofword.csv', 'w')
for row in df['sentence']:
    kamus = []
    kalimat = row.split(' ')
    for kata in kalimat:
        if kata not in kamus:
            kamus.append(kata)
    for j in range(len(kamus)):
        out.write(kamus[j] + '\n')
out.close()
print(len(pd.read_csv(out.name)))
# out = open('./input/bagofword.csv', 'w')
# with open("./input/data-bersih.csv") as fobj:
#     text = fobj.read().strip().split()
#     kamus = []
#     for kata in text:
#         if kata not in kamus:
#             kamus.append(kata)
#     for j in range(len(kamus)):
#         out.write(kamus[j] + '\n')
# out.close()
# print (kamus)