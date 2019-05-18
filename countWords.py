import csv
from collections import Counter

words= []
with open('tweets.csv', 'rb') as csvfile:
    reader = csv.reader(csvfile)
    reader.next()
    for row in reader:
         csv_words = row[0].split(" ")
         for i in csv_words:
              words.append(i)

words_counted = []
for i in words:
    x = words.count(i)
    words_counted.append((i,x))

order_words = sorted(words_counted, key = lambda x: x[1], reverse = True)

#write this to csv file
csvFile = open('output.csv', 'w')
csvWriter = csv.writer(csvFile)
csvWriter.writerow([order_words])