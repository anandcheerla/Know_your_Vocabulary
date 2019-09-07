from PyDictionary import PyDictionary
import sys
dictionary=PyDictionary()
print("Enter the name of input text file")
input_file=input()
out=open("output.txt","w")
out_meanings=open("output_meanings.txt","w")
inp=input("enter the minimum length of words you want\n")
print("Working on by neglecting the casual words")
li=['is','i','the','am','because','in','you','be','to','but','your','I','That','that','again','of','to','on','it','because','for','My','my','give','he','she','a','an','since','did','do','just','you','but']
print("Want  to proceed,input yes else no")
if(input()=='yes'):
	with open(input_file,'r') as f:
		for line in f:
			for word in line.split():
				try:
					a=int(word[0])
				except ValueError as ve:
					if word[0]!='-':
						word=word.replace('<i>', '')
						word=word.replace('</i>', '')
						word=word.replace('.', '')
						word=word.replace('"', '')
						word=word.replace('?', '')
						word=word.replace(',', '')
						if word not in li and len(word)>=int(inp):
							out.write(word+"\n")
							out_meanings.write(word+" : "+str(dictionary.meaning(word))+"\n")
	print("The vocabulary words are generated and is stored in output file")
	print("The vocabulary meanings are generated and stored in output_meanings file")
else:
	print("Thank You")
	
