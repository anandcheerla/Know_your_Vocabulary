import re   #for regualar expressions

def readInput(input_file,output_file):
	words_file=open(output_file,"a")
	input_file_name=input_file

	word_frequency={}
	words=set()
	with open(input_file_name,'r') as f:
		for line in f:
			for word in line.split():
				pattern="([a-z]+(-|'|)[a-z]+)"     #which will atleast take two letters in a word
				word=re.fullmatch(pattern,word)
				if word is not None:
					word=word.string
					words.add(word)
					if word in word_frequency:
						word_frequency[word]+=1
					else:
						word_frequency[word]=1

	
	words=list(words)

	return (words,word_frequency)


