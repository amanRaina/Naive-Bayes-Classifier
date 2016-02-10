import sys
import os
import json
import io

def main():

	with open("indexed_doc",'r') as indexed:
		vocab_dict=eval(indexed.read());

	for filename in os.listdir(sys.argv[1]):
		name=(sys.argv[1]+'/'+filename)
		with open(name,'r',encoding="latin1") as infile:
				data=infile.read();
				main_dict={}
				words=data.split();
				for word in words:
					# if word!="Subject:":
					main_dict[vocab_dict.get(word)]=main_dict.get(vocab_dict.get(word),0)+1

				with open('dummy_file.txt','a') as opfile:
					if(filename.find("ham")!=-1):
						opfile.write("HAM ")				
						opfile.write(str(main_dict)[1:-1].replace(',','').replace(': ',':')+'\n')
					elif(filename.find("spam")!=-1):
						opfile.write("SPAM ")				
						opfile.write(str(main_dict)[1:-1].replace(',','').replace(': ',':')+'\n')	

				opfile.close()
		
if __name__ == "__main__":
    main()	