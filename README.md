# Topic-Modeing-Social-Network-Text-Data
To categorize any form of text into 22 different topics

The categorizerClass.py and mcategorizerClass.py

categorizerClass.py - based on 22 cluster seeds
mcategorizerClass.py - based on 700+ cluster seeds (more precise)

are have the categorizer class with the function:
getCategory(text) return category

create an object for this class and pass text to this function to get the category

catObj = mcategorizerClass.Categorize()
cat = catObj.getCategory(text)

then refer to csvInput and dumpInput python files for bulk topic processing

vectors.bin file is the W2V vectors bin
download the bigger 3.5 GB W2V vectors bin for better results.
link:code.google.com/p/word2vec/

