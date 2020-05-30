from nltk.corpus import wordnet
from word_complexity import findWordComplexity
from input import readInput


words,word_frequency=readInput(input_file="input.txt",output_file="words.txt")


user_words_frequency={}
try:			#this is to store the words frequency from the user before
	user_input_file=open("user.txt","r")
	for line in user_input_file.readlines():
		for word in line.split():
			if word in user_words_frequency:
				user_words_frequency[word]+=1
			else:
				user_words_frequency[word]=1
except:
	print("no such file")

	


medium_level_words=set()

for word in words:
	if findWordComplexity(word,word_frequency)!="easy":
		if word in user_words_frequency and user_words_frequency[word]>3:
			pass
		else:
			medium_level_words.add(word)


medium_level_words=list(medium_level_words)
for i in medium_level_words:
	print(i,)

# for word in medium_level_words:
# 	word_info = wordnet.synsets(word)
# 	print(word,"----------------------------------------------------")
# 	for each in word_info:
# 		print(each.definition())
# 	print()

#store these as the user data, inorder to reject the words which appear again and again in terms of user not in terms of single file
user=open("user.txt","a+")
for i in medium_level_words:
	user.write(i+" ")

user.close()