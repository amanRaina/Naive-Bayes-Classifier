import sys

with open(sys.argv[1],'r') as infile:
	with open(sys.argv[2],'w') as op:
		lines=infile.readlines()
		for line in lines:
			words=line.split()
			if(words[0]=="HAM"):
				op.write("HAM")
			elif(words[0]=="SPAM"):
				op.write("SPAM")
			op.write("\n")		

