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

class Categorize(object):
	
	def __init__(self):

		## Load Pickle
		self.Cluster_lookUP = load_obj("Cluster_lookUP")
		self.Cosine_Similarity = load_obj("Cosine_Similarity")
		self.num2cat = load_obj("num2cat")
		self.Cluster_Model = load_obj("clusterSmall")
		self.catVec = load_obj("catVec")
		self.model = gensim.models.Word2Vec.load_word2vec_format('vectors.bin', binary=True)
		self.model.init_sims(replace=True)
		#Load Rake
		self.rake = rake.Rake("SmartStoplist.txt")

	def CosSim (self,v1,v2):
		return (1 - spatial.distance.cosine(v1, v2))

	def combine(self,v1,v2):
		A = np.add(v1,v2)
		M = np.multiply(A,A)
		lent=0
		for i in M:
			lent+=i
		return np.divide(A,lent)

	def getCategory(self,text):
		# Text To Categorize = text

		Ptext = u" ".join(twokenize.tokenize(text))
		Ptext = self.rake.run(Ptext.lower().strip())


		scores=dict()
		for i in range(0,22):
			scores[i] = 0.0

		for phrase in Ptext:
			phrase = phrase[0]
			if len(phrase.split()) == 1:
				try:
					scores[self.Cluster_lookUP[phrase]] += self.Cosine_Similarity[phrase]
					#print(num2cat[Cluster_lookUP[phrase]])
				except:
					#print(phrase + " Skipped!")
					continue
			else:
				words = phrase.split()
				try:
					vec = np.array(model[words[0]])
					for word in words[1:]:
						try:
							vec = combine(vec,np.array(model[word]))
						except:
							#print(word + " Skipped!")
							continue
					tempCat = self.Cluster_Model.predict(vec)
					#print(num2cat[tempCat[0]])
					scores[tempCat[0]] += CosSim(vec,self.catVec[tempCat[0]])
				except:
					#print(words[0] + " Skipped!")
					continue
		#print(scores)
		# catNum = max(scores.items(), key=operator.itemgetter(1))[0]
		# if max(scores.items(), key = operator.itemgetter(1))[1] != 0.0:
		# 	return self.num2cat[catNum]
		# else:
		# 	return ("general") #No Category assigned!
		scoreSort  = sorted(scores.items(), key = operator.itemgetter(1), reverse=True)
		cats = []
		f=0
		for s in scoreSort:
			if s[1] != 0.0:
				f=1
				cats.extend([self.num2cat[s[0]]])		
			else:
				continue
		if f==0: #No Category assigned!
			return ("general")
		else:
			if len(cats) == 1:
				ret = str(cats[0])
			else:
				ret = "|".join(cats)
			return ret