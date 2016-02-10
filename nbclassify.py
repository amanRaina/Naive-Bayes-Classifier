import sys

def spam_classify(model_dict,spam_file):
	test_dict={}
	split_dict={}
	counth=0
	counts=0
	totalh=0
	totals=0
	total_doc=0
	prec_totalh=0
	prec_totals=0	

	with open("spam.nb.out",'w') as op:	
		with open(spam_file,'r') as testfile:
			for line in testfile:
				total_doc+=1
				ham_label=0.0
				spam_label=0.0
				ham_not=0
				spam_not=0
				ham_val=0.0
				spam_val=0.0
				words=line.split()
				for x in words:
					word=x.split(':')
					# print(word)
					key=word[0]
					value=word[1]
					try:
						if model_dict['HAM'][key]:
							ham_val=model_dict['HAM'][key]*float(value)
							ham_label=float(ham_label+ham_val)
					except KeyError:
							ham_not+=int(value)
					try:
						if model_dict['SPAM'][key]:
							spam_val=model_dict['SPAM'][key]*float(value)
							spam_label=float(spam_label+spam_val)
					except KeyError:
						spam_not+=int(value)

				ham_label+=model_dict['HAMCOUNT']+float((model_dict['HAMNOTFOUND']*ham_not))
				spam_label+=model_dict['SPAMCOUNT']+float((model_dict['SPAMNOTFOUND']*spam_not))

				if(ham_label>spam_label):
					op.write("HAM")
				else:
					op.write("SPAM")
				op.write("\n")
			op.close()			


def sentiment_classify(model_dict,sentiment_file):
	split_dict={}
	countp=0
	countn=0
	totalp=0
	totaln=0
	total_doc=0
	prec_totalp=0
	prec_totaln=0
	test_dict={}

	with open("sentiment.nb.out",'w') as op:
		with open(sentiment_file,'r') as testfile:
			for line in testfile:
				total_doc+=1
				pos_label=0.0
				neg_label=0.0
				pos_not=0
				neg_not=0
				pos_val=0.0
				neg_val=0.0
				words=line.split()
				for x in words:
					word=x.split(':')
					key=word[0]
					value=word[1]
					try:
						if model_dict['POSITIVE'][key]:
							# model_dict['POSITIVE'][key]+=model_dict['POSITIVE'][key]*float(value)
							pos_val=model_dict['POSITIVE'][key]*float(value)
							pos_label=float(pos_label+pos_val)
					except KeyError:
						pos_not+=int(value)
					try:
						if model_dict['NEGATIVE'][key]:
							neg_val=model_dict['NEGATIVE'][key]*float(value)
							neg_label=float(neg_label+neg_val)
					except KeyError:
						neg_not+=int(value)

				pos_label+=model_dict['POSCOUNT']+float((model_dict['POSNOTFOUND']*pos_not))
				neg_label+=model_dict['NEGCOUNT']+float((model_dict['NEGNOTFOUND']*neg_not))						
						
				if(pos_label>neg_label):
					# prec_totalp+=1
					op.write("POSITIVE")
				else:
					op.write("NEGATIVE")

				op.write("\n")	



def main():
	model_dict={}
	with open(sys.argv[1],'r') as modelfile:
		model_dict=eval(modelfile.read())

	# with open(sys.argv[2],'r') as testfile:
	# 	lines=testfile.readlines();
	# 	words=lines[0].split();
	# 	if(words[0]=="POSITIVE" or str(words[0])=="NEGATIVE"):
	# 		sentiment_classify(model_dict,sys.argv[2])
	# 	if(words[0]=="SPAM" or str(words[0])=="HAM"):
	# 		spam_classify(model_dict,sys.argv[2])	
		
	if(sys.argv[1]=="sentiment.nb.model"):
		sentiment_classify(model_dict,sys.argv[2])	
	elif(sys.argv[1]=="spam.nb.model"):
		spam_classify(model_dict,sys.argv[2])


if __name__=="__main__":
	main();