import re,sys
from twokenize import *
from collections import defaultdict
import pickle
import mcategorizerClass

def load_obj(name):
    with open( name , 'rb') as f:
        return pickle.load(f)

## data loaded below (Emo Tweets)
# rawL = load_obj("tweets.dmp")
## tmublr data
rawL = load_obj("tumblr.dmp")

raw =[]

for r in rawL:
  raw.append(r.encode("utf-8"))

print("length before duplicate removal:" +str(len(raw)))
raw = set(raw)
print("length after duplicate removal:" +str(len(raw)))

# Preprocessing ....
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

# #Since Text already processed
# stoplist  = ["me","you","this","me","he","she","i","a","an","and","are","as","at","be","by","for","from","has","he","is","in","it","its","of","on","that","the","to","was","were","will","with"]
# stoplist +=[")","(",".","'",",",";",":","?","/","!","@","$","*","+","-","_","=","&","%","`","~","\"","{","}"]


# for line in raw:
#   # line  = line.decode("utf-8").lower()
#   for r in ["@","#"]:
#     line = line.replace(r.encode("utf-8")," ".encode("utf-8"))
#   for ree in ReList:
#     line = re.sub(ree,"", str(line.strip()))

#   if line != []:
#     ProcessedLines.append(line)
# #    print(line)
# print("Final: " +str(len(ProcessedLines)))

catz = mcategorizerClass.Categorize()

for text in raw:
  print("The Text:"+str(text))
  print(catz.getCategory(text))
  print()
