# cleaned the file from n3vocab.csv to notes3.csv
# N3 vocab file was not in good shape so I only cleaned the tags

import csv
csv_file_read = open('n3vocab.csv', mode='r')
reader = csv.reader(csv_file_read, delimiter=",")
csv_file_write = open('notes3.csv', mode='w')
fieldnames = ['result']
writer = csv.DictWriter(csv_file_write, fieldnames=fieldnames)
reader = csv.reader(csv_file_read, delimiter=",")
writer.writeheader()

try:
  for idx,i in enumerate(reader):
    rep = i[0].replace('"', '').replace('<p>', '').replace('</p>', '').replace('...', '.').replace('<br>', '').replace('<br/>', '')
    if(idx<10):
      trm = rep[3:]
    elif(idx>=10 and idx<100):
      trm = rep[4:]
    elif(idx>=100 and idx<1200):
      trm = rep[4:]

    writer.writerow({'result': trm})
  csv_file_read.close()
  csv_file_write.close()
except Exception as e:
  print(e)
  csv_file_write.close()
  csv_file_read.close()
