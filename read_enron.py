import sys
import os

def main():
	vocab_dict={}
	with open("enron.vocab",'r',encoding="latin1") as infile:
		count=1;
		for lines in infile.readlines():
			words=lines.split('\n')[0];
			if words not in vocab_dict.values():
				vocab_dict[words]=count
			count=count+1;
	infile.close()		

	with open("indexed_doc",'w') as op:		
		op.write(str(vocab_dict))
	op.close()

if __name__ == "__main__":
    main()