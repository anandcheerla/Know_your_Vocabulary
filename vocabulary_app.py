from nltk.corpus import wordnet
from word_complexity import findWordComplexity
from input import readInput


#-----------------------------
#read input and get the words and their frequeny
words,word_frequency=readInput(input_file="input.txt",output_file="words.txt")



#--------------------------------------------------------
#this is to store the words frequency from the user before
user_words_frequency={}
try:			
	user_input_file=open("user.txt","r")
	for line in user_input_file.readlines():
		for word in line.split():
			if word in user_words_frequency:
				user_words_frequency[word]+=1
			else:
				user_words_frequency[word]=1

	user_input_file.close()

except:
	print("no such file")



#------------------------------------
#segregate the useful words by calling the findWordComplexity function
medium_level_words=set()

for word in words:
	if findWordComplexity(word,word_frequency)!="easy":
		if word in user_words_frequency and user_words_frequency[word]>3:
			pass
		else:
			medium_level_words.add(word)

medium_level_words=list(medium_level_words)




meanings_file=open("meanings.txt","w")
pos_name={"n":"Noun","v":"Verb","a":"Adjective","r":"Adverb","s":"Adjective Satellite"}

for word in medium_level_words:
	word_info = wordnet.synsets(word)
	meanings_file.write(word+" --------------------------\n")
	for each in word_info:
		meanings_file.write(each.definition()+" - ")
		meanings_file.write(pos_name[each.pos()]+"\n")

	meanings_file.write("\n\n")


#store these as the user data, inorder to reject the words which appear again and again in terms of user not in terms of single file
user=open("user.txt","a+")
words_file=open("words.txt","w+")

for i in medium_level_words:
	user.write(i+" ")
	words_file.write(i+" ")


user.close()
words_file.close()