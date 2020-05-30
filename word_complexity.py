from nltk.corpus import wordnet
import nltk
# from nltk.corpus import stopwords

from stop_words import get_stop_words

naive_words = get_stop_words('english')


#parts of speech tagging
def isItEasy(word):
	word=nltk.pos_tag([word])
	pos=word[0][1]

	# if it is conjunction , prepositon or pronoun
	if pos in ["CC","IN","WP"]:
		return True

	return False


#complexity finding method
def findWordComplexity(word,word_frequency):
	word_length=len(word)
	word_complexity=None

	if(word_length<=2):
		word_complexity="easy"
	else:
		if word in naive_words:
			word_complexity="easy"
		elif isItEasy(word) or word_frequency[word]>10:
			word_complexity="easy"
		else:
			word_complexity="medium"

	return word_complexity

