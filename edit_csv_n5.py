# cleaned the file from n5vocab.csv to notes2.csv
# going to use this cleaned file for project database
# IDK if I could have done this any smarter way... if you know then suggest me hehee...
# Used this same code for n4vocabclean.csv as well
import csv
csv_file_read = open('notes.csv', mode='r')
reader = csv.reader(csv_file_read, delimiter=",")
csv_file_write = open('notes2.csv', mode='w')
fieldnames = ['result','result1','result2','result3']
writer = csv.DictWriter(csv_file_write, fieldnames=fieldnames)
reader = csv.reader(csv_file_read, delimiter=",")
writer.writeheader()

try:
  for idx,i in enumerate(reader):
    rep = i[0].replace('"', '').replace('<p>', '').replace('</p>', '').replace('...', '.')
    if(idx<10):
      trm = rep[3:]
    elif(idx>=10 and idx<100):
      trm = rep[4:]
    elif(idx>=100 and idx<1000):
      trm = rep[4:]
    
    spl = trm.split(". ")
    lst = []
    print(idx)
    try:
      for jdx, j in enumerate(spl):
        j_spl = j.split(":")
        lst = lst + j_spl
      writer.writerow({'result': lst[0],'result1': lst[1],'result2': lst[2],'result3': lst[3]})
    except IndexError:
      print('error')
      writer.writerow({'result': lst[0],'result1': lst[1]})

  csv_file_read.close()
  csv_file_write.close()
except Exception as e:
  print(e)
  csv_file_write.close()
  csv_file_read.close()
