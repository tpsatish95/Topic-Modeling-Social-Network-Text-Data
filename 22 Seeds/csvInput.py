import re,sys
from twokenize import *
from collections import defaultdict
import pickle
import categorizerClass
import csv

def load_obj(name):
    with open( name , 'rb') as f:
        return pickle.load(f)

## data loaded below (Emo Tweets)
# rawFile = open("sample_tweets")
# twitter joy data
raw = load_obj("tweetsData.pkl")

# raw = rawFile.readlines()

print("length before duplicate removal:" +str(len(raw)))
raw = set(raw)
print("length after duplicate removal:" +str(len(raw)))


# #Since Text already processed (un comment if aggresive)
# # Preprocessing ....
# Code  = r"\\[a-zA-Z0-9]+"

# ProcessedLines = []
# ReList = [
#     Url_RE,
#     Entity,
#     Timelike,
#     NumNum,
#     NumberWithCommas,
#     Code,
#     Punct,
#     Separators,
#     Decorations
# ]


# stoplist  = ["me","you","this","me","he","she","i","a","an","and","are","as","at","be","by","for","from","has","he","is","in","it","its","of","on","that","the","to","was","were","will","with"]
# stoplist +=[")","(",".","'",",",";",":","?","/","!","@","$","*","+","-","_","=","&","%","`","~","\"","{","}"]


# for line in raw:
#   # line  = line.decode("utf-8").lower()
#   for r in ["@","#"]:
#     line = line.replace(r," ")
#   for ree in ReList:
#     line = re.sub(ree,"", str(line.strip()))

#   if line != []:
#     ProcessedLines.append(line)
# #    print(line)
# print("Final: " +str(len(ProcessedLines)))

catz = categorizerClass.Categorize()

writer = csv.writer(open("output.csv","w"))
for text in raw:
	text = str(text.strip()).encode("utf-8")
	cat = catz.getCategory(text)
	print("The Text:".encode("utf-8")+text)
	print(cat)
	print()
	writer.writerow([str(text),cat.encode("utf-8")])