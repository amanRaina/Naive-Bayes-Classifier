import sys
import math


def main():
	count_ham=0;
	count_spam=0;
	count_pos=0;
	count_neg=0;
	vocab_spam=[]

	vocab_sentiment=[]

	ham_dict={}
	spam_dict={}
	pos_dict={}
	neg_dict={}
	model_spam_dict={}
	model_sentiment_dict={}

	with open(sys.argv[1]) as infile:
		for line in infile:
			word,space,lines=line.partition(' ')
			if(word=="HAM"):
				count_ham=count_ham+1
				words=(lines.split(' '))
				for x in words:
					word=x.split(':')
					key=word[0]
					vocab_spam.append(key)
					value=word[1]
					if(key!='None'):
						if(key not in ham_dict.keys()):
							ham_dict[key]=int(value)
						else:
							ham_dict[key]=ham_dict[key]+int(value)

			elif(word=="SPAM"):
				count_spam=count_spam+1
				words=(lines.split(" "))
				for x in words:
					word=x.split(':')
					key=word[0]
					vocab_spam.append(key)
					value=word[1]
					if(key not in spam_dict.keys()):
						spam_dict[key]=int(value)
					else:
						spam_dict[key]=spam_dict[key]+int(value)

			elif(word=="POSITIVE"):
				count_pos=count_pos+1
				words=(lines.split(' '))
				for x in words:
					word=x.split(':')
					key=word[0]
					vocab_sentiment.append(key)
					value=word[1]
					# print(value)
					if(key not in pos_dict.keys()):
						pos_dict[key]=int(value)
					else:
						pos_dict[key]=pos_dict[key]+int(value)

			elif(word=="NEGATIVE"):
				count_neg=count_neg+1
				words=(lines.split(' '))
				for x in words:
					word=x.split(':')
					# print(word)
					key=word[0]
					# print(key)
					vocab_sentiment.append(key)
					value=word[1]
					if(key not in neg_dict.keys()):
						neg_dict[key]=int(value)
					else:
						neg_dict[key]=neg_dict[key]+int(value)

		# print(count_ham)
		# print(count_spam)	
		vocab1=list(set(vocab_spam))	
		# print(len(vocab1))		
		if ham_dict:
			total_count=sum(ham_dict.values())	
			for keys in ham_dict:
				word_count=ham_dict[keys]
				ham_dict[keys]=math.log((word_count+1)/(total_count+len(vocab1)))
			model_spam_dict['HAM']=ham_dict;
			model_spam_dict['HAMNOTFOUND']=math.log(1/(total_count+len(vocab1)))
			# model_spam_dict['HAM']
		if count_ham!=0:
			model_spam_dict['HAMCOUNT']=math.log(count_ham/(count_spam+count_ham))
		if spam_dict:
			total_count=sum(spam_dict.values())	
			for keys in spam_dict:
				word_count=spam_dict[keys]
				spam_dict[keys]=math.log((word_count+1)/(total_count+len(vocab1)))
			model_spam_dict['SPAM']=spam_dict;
			model_spam_dict['SPAMNOTFOUND']=math.log(1/(total_count+len(vocab1)))
		if count_spam!=0:	
			model_spam_dict['SPAMCOUNT']=math.log(count_spam/(count_spam+count_ham))

		vocab_sent_size=len(list(set(vocab_sentiment)))	
		# print(vocab_sent_size)
		# print(count_pos)
		# print(count_neg)

		if pos_dict:
			total_count=sum(pos_dict.values())
			for keys in pos_dict:
				word_count=pos_dict[keys]
				pos_dict[keys]=math.log((word_count+1)/(total_count+vocab_sent_size))
			model_sentiment_dict['POSITIVE']=pos_dict;
			model_sentiment_dict['POSNOTFOUND']=math.log(1/(total_count+vocab_sent_size))
		if count_pos!=0:
			model_sentiment_dict['POSCOUNT']=math.log(count_pos/(count_neg+count_pos))
		if neg_dict:
			vocab_size=(len(neg_dict.keys()))
			total_count=sum(neg_dict.values())	
			for keys in neg_dict:
				word_count=neg_dict[keys]
				neg_dict[keys]=math.log((word_count+1)/(total_count+vocab_sent_size))
			model_sentiment_dict['NEGATIVE']=neg_dict;
			model_sentiment_dict['NEGNOTFOUND']=math.log(1/(total_count+vocab_sent_size))
		if count_neg!=0:
			model_sentiment_dict['NEGCOUNT']=math.log(count_neg/(count_neg+count_pos))


	with open(sys.argv[2],'w') as op:
		# if(sys.argv[2]=="spam.nb"):
		if model_spam_dict:
			op.write(str(model_spam_dict));
		# if(sys.argv[2]=="sentiment.nb"):
		if model_sentiment_dict:
			op.write(str(model_sentiment_dict))
	op.close()		

if __name__=="__main__":
	main();
