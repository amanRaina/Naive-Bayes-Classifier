# Naive-Bayes-Classifier

Project Data

In this work, we are using tokens as features. However, rather than use the text of the token as the feature name, we will assign each unique token an integer identifier. For the IMDB movie reviews, the file imdb.vocab is a list of all the unique tokens in the corpus, one per line (all lower case). The token on line 1 of the file should be given the identifier 1; the token on line 2 has the identifier 2 and so on. For the email corpus, we will give you a file, enron.vocab in the same format as imdb.vocab.

Smoothing, and common, rare and unknown tokens: For the machine learning toolkits, you don't need to worry about smoothing or tokens that appear in testing but not training. For your Naive Bayes classifier, you will need to worry about these issues. The reference solution written by the TAs will be using add-one smoothing on the labeled data. For tokens unique to the unlabeled (testing) data, the reference solution will simply ignore these tokens (i.e., pretend they did not occur). There are more sophisticated methods of smoothing and handling unknown tokens that we will discuss in class and on piazza but the TAs will be using the above approach.

The reference solution will not be taking into account the frequency of tokens. All tokens in the labeled data will be considered. However, you have the freedom to remove high frequency and low frequency tokens from consideration if you think this will improve your performance.

For your naive Bayes classifier, you will use the following representation. For training and development data, the first item will be a label for the example. For spam detection, it will be either SPAM or HAM where HAM refers to not spam. For sentiment detection, it will be either POSITIVE or NEGATIVE. Following the label will be a list of features and values for that example. The features correspond to the tokens present in the example which will be represented by their unique identifiers and listed in increasing order. The value of a feature will be the count of how many times that token appears in the example. The feature and value should be separated by ":".

So for a movie review, each feature would correspond to a token followed by ":" followed by the count of that token in the movie review. If "1" corresponded to "the", then "1:38" means that "the" appeared 38 times. If "2" corresponded to "a", then "2:10" means that "a" appeared 10 times.

The next line in the data file will correspond to a different example. It may have a different number of features since it may contain different tokens. For test data, the format will be the same except that there will be no LABEL.

FORMAT OF TRAINING/DEVELOPMENT DATA:

LABEL FEATURE_NAME1:FEATURE_VALUE1 FEATURE_NAME2:FEATURE_VALUE_2 ... FEATURE_NAME_Q:FEATURE_VALUE_Q
Spam Data

On Blackboard, we will post two sets of data: labeled and unlabeled (test) as well as enron.vocab. All data has already been cleaned up (leaving only the text parts of the subjects and bodies) and tokenized with tokens separated by spaces.

All email data will be stored as gzipped tar files. You'll need to gunzip the files and then untar them tar xvf. The archives contain a large number of individual files (one per email) divided into subfolders "ham" and "spam". You will need to write a Python script to convert these large number of individual files into a single file in the Project Data format.

Sentiment Analysis Data

On Blackboard, you will find labeled and unlabeld data as well as a vocabulary list. Use gunzip to uncompress the data. The original data are IMDB reviews associated with ratings either >= 7 (positive) or <= 4 (negative). The vocabulary list defines the 89527 unique tokens in the corpus (one per line of the file). The data is almost in the Project Data format but the identifiers start at 0. So you'll have to go through the file and add one to each.

We are not providing the reviews themselves. But you can write a Python script to tranform the features in the labeled data from numbers into the text of the associated tokens for debugging purposes.

Tools you need to build / install

Naive Bayes classifier in Python

You must not use any additional packages, libraries or modules. Just the standard installation.
You will create two scripts. nblearn.py will learn a model from training data. nbclassify.py will use a model to classify new text.
TRAININGFILE and TESTFILE will be in the Project Data Format. 
We should be able to run your scripts in the following manner:

python3 nblearn.py TRAININGFILE MODELFILE

python3 nbclassify.py MODELFILE TESTFILE
The format for MODELFILE is up to you but should contain sufficient information for nbclassify.py to process a file in the Project Data Format and for each line (example) print to STDOUT the name of the more probable class (one per line).


