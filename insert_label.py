import csv

fo = open ('./input/liputan62_label.csv', 'w')
with open ('./input/liputan62_tfidf.csv', 'r') as input1, open ('./input/label_liputan62.csv', 'r') as input2:
    reader1 = input1.read().split("\n")
    reader2 = csv.reader(input2, delimiter=',')
    label=[]
    for row in reader2:
        # print(row[1])
        label.append(row[1])
    # print(reader2[0])
    print(len(label))
    print(len(reader1))
    for baris in range(len(reader1)):
        if label[baris] == "NO":
            label[baris] = '0'
        elif label[baris] == 'YES':
            label[baris] = '1'
        fo.write(reader1[baris] + ',' + label[baris] + '\n')

fo.close()