import sys

with open(sys.argv[1],'r') as infile:
	with open(sys.argv[2],'w') as op:
		lines=infile.readlines()
		for line in lines:
			words=line.split()
			if(words[0]=="POSITIVE"):
				op.write("POSITIVE")
			elif(words[0]=="NEGATIVE"):
				op.write("NEGATIVE")
			op.write("\n")		

