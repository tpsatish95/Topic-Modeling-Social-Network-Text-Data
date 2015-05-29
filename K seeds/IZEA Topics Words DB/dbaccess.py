import sqlite3
import pickle

def save_obj(obj, name ):
    with open( name + '.pkl', 'wb') as f:
        pickle.dump(obj, f,  protocol=2)

def load_obj(name ):
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)

conn = sqlite3.connect("categoryMap.s3db")

c = conn.cursor()

categoryMap = c.execute("SELECT * FROM TagCategoryMap")

cat = [
"advertising",
"beauty",
"business",
"celebrity",
"diy / craft",
"entertainment",
"family",
"fashion",
"food",
"general",
"health",
"lifestyle",
"music",
"news",
"pop",
"culture",
"social",
"media",
"sports",
"technology",
"travel",
"video games"
]

num = range(0,22)
cat2num = dict(zip(cat, num))

wordMap = dict()

stoplist =[")","(",".","'",",",";",":","?","/","!","@","$","*","+","-","_","=","&","%","`","~","\"","{","}"]

for row in categoryMap:
	word = row[0]
	word = word.lower().strip()
	word = word.replace(".","")
	f=0
	for s in stoplist:
		if s in word:
			word = word.replace(s," ")
			f=1
	if f==1:
		words = word.split()
	else:
		words = [word]	
	try:
		if "|" not in row[1]:
			for w in words:
				wordMap[w] = [cat2num[row[1].lower()]]
		else:
			for w in words:
				wordMap[w] = [cat2num[l.lower()] for l in row[1].split("|")]
	except:
		print(row)
		continue

#####
save_obj(wordMap,"baseWord2CatMap")
#print(wordMap)
print(len(wordMap))

## test the cat list and words intersection
## has all cat in base word list (Ready to Seed)
# for bw in wordMap.keys():
# 	for c in cat:
# 		if c in bw:
# 			print(bw)