import requests						#to make requests
from bs4 import BeautifulSoup		#for parsing html which is reqested using url
import re          #for regular expressions

print("Enter the name of input text file")
input_file=input()
out=open("output.txt","w")
out_meanings=open("output_meanings.txt","w")
inp=input("enter the minimum length of words you want\n")
print("Working on by neglecting the casual words",end="\n")
li=['is','i','the','am','because','in','you','be','to','but','your','I','That','that','again','of','to','on','it','because','for','My','my','give','he','she','a','an','since','did','do','just','you','but']
print("Want  to proceed, input yes or no",end="\n")
count=1
if(input()=='yes'):
	print("This may take sometime as we need to get every vocabulary meaning",end="\n")
	print("Working.....")
	words=set()
	with open(input_file,'r') as f:
		for line in f:
			for word in line.split():
				word=re.sub('[^a-zA-Z]', '', word)
				if word != "" and word not in li and len(word)>=int(inp):
					words.add(word)
	
	words=list(words)
	for i in words:
		out.write(i+"\n")
					
	print("The vocabulary words are generated and is stored in output file")
	if(input("If you want meanings of the vocabulary, input yes")):
		for word in words:
			html=BeautifulSoup(requests.get("https://www.google.co.in/search?q=meaning:{0}".format(word)).text,'html.parser')
			table=html.find("table", {"style": "font-size:14px;width:100%"})
			if table != None:
				meaning = table.find_all("li")
				out_meanings.write(word+" : "+"\n")
				for i in meaning:
					out_meanings.write(i.getText()+"\n")
				out_meanings.write("\n")
				print("finished "+str(count),end="\r")
				count+=1
					
		print("The vocabulary meanings are generated and stored in output_meanings file")
	else:
		print("Thank You")
else:
	print("Thank You")
	
