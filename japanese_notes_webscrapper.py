# I was struggling while making notes for JLPT N4 exam
# Like, the vocabs are all over the internet
# Plus I needed to make a sentense with every vocab in order to memorise this.
# This script help in crawl all the pages where I found meaningfull content and paste in a csv
# I need to run another script to bring the csv into shape but it fine


from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import csv

csv_file = open('notes.csv', mode='w')
fieldnames = ['result']
writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
writer.writeheader()

thislist = [
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-1.html", 
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-2.html",
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-3.html",
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-4.html",
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-5.html",
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-6.html",
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-7.html",
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-8.html",
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-9.html",
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-10.html",
  "https://learnjapanesedaily.com/jlpt-n4-vocabulary-week-11.html"
  ]

try:
  for x in thislist:
    print(x)
    req = Request(x, headers={'User-Agent': 'Mozilla/5.0'})
    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml')
    table = soup.findAll('p')

    for p in table:
      writer.writerow({'result': p})
  csv_file.close()
except:
  print('expection')
  csv_file.close()
