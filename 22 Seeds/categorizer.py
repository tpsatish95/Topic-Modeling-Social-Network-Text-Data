import pickle
from rake import rake
import twokenize
import gensim
from scipy import spatial
import operator
import numpy as np

def save_obj(obj, name ):
    with open( name + '.pkl', 'wb') as f:
        pickle.dump(obj, f,  protocol=2)

def load_obj(name ):
    with open( name + '.pkl', 'rb') as f:
        return pickle.load(f)

## Load Pickle
Cluster_lookUP = load_obj("Cluster_lookUP")
Cosine_Similarity = load_obj("Cosine_Similarity")
num2cat = load_obj("num2cat")
Cluster_Model = load_obj("cluster")
catVec = load_obj("catVec")
model = gensim.models.Word2Vec.load_word2vec_format('vectors.bin', binary=True)
model.init_sims(replace=True)
#Load Rake
rake = rake.Rake("SmartStoplist.txt")

def CosSim (v1,v2):
	return (1 - spatial.distance.cosine(v1, v2))

def combine(v1,v2):
	A = np.add(v1,v2)
	M = np.multiply(A,A)
	lent=0
	for i in M:
		lent+=i
	return np.divide(A,lent)

while(1):
	# Text To Categorize
	text = input("Enter Text to Categorize or EXIT: ")
	if text == "EXIT":
		break
	# text = "I am taking a flight to chicago by monday evening."
	Ptext = u" ".join(twokenize.tokenize(text))
	Ptext = rake.run(Ptext.lower().strip())

	#print(Ptext)

	scores=dict()
	for i in range(0,22):
		scores[i] = 0.0

	for phrase in Ptext:
		phrase = phrase[0]
		if len(phrase.split()) == 1:
			try:
				scores[Cluster_lookUP[phrase]] += Cosine_Similarity[phrase]
				#print(num2cat[Cluster_lookUP[phrase]])
			except:
				print(phrase + " Skipped!")
				continue
		else:
			words = phrase.split()
			try:
				vec = np.array(model[words[0]])
				for word in words[1:]:
					try:
						vec = combine(vec,np.array(model[word]))
					except:
						print(word + " Skipped!")
						continue
				tempCat = Cluster_Model.predict(vec)
				#print(num2cat[tempCat[0]])
				scores[tempCat[0]] += CosSim(vec,catVec[tempCat[0]])
			except:
				print(words[0] + " Skipped!")
				continue
	#print(scores)
	catNum = max(scores.items(), key=operator.itemgetter(1))[0]
	if max(scores.items(), key = operator.itemgetter(1))[1] != 0.0:
		print("The Category is : " + num2cat[catNum])
	else:
		print("No Category assigned!")