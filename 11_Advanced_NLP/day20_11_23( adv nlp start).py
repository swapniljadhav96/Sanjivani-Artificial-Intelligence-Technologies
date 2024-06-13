# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:25:27 2023

@author: suraj
"""

'''Text- minimng'''

###############
# fiinding the index of the letter
senctence="we are learning textmining from Sanjivani AI"
# if we want to know position of learning
senctence.index("learning")
# it will show learning is at the 7 position
# this is going to show thw charater position from 0  inculding

###################################
# finding the position of the words
# we want to know postion textminig word
senctence.split().index('textmining')
#it will split the words  in list  and count the position
# if you want to see the list select senectence.split() and
# it will show at 3

############################################################
#suppose we want print any word in the reverse order
senctence.split()[2][: :-1]
# [start:end end:-1 (start)]  will start from -1,-2,-3 till the end
#learnig will be printed in the reverse order

################################################
# suppose we want to print first and last word of the sentence
words=senctence.split()
first_words=words[0]
first_words
last_words=words[-1]
last_words

##########################################
# now we want to concate the first and last words
concate_word=first_words+" "+last_words
concate_word
###########################################
# we want the to print  even words from the sentence
[words[x] for x in range(len(words)) if x%2==0]
# the words having the odd length are not print
##############################################
senctence
# now we want to display only ai
senctence[-3:]
# balaji  publication
############################################
# suppose we want to display the entire sentence in the revrese order
senctence[::-1]
# now the all the sentence are print in the reverse order

##########################################
# suppose we want to select each word and print in the reverse order
words
print(" ".join(word[::-1] for word in words))
# 


#############################################################
''' ********************tokenization*******************************'''
import nltk
nltk.download('punkt')          # it is install here only
from nltk import word_tokenize
words=word_tokenize("I am reading NLP Fundamentals")
print(words)
# it is split the hole sentance into each words


###################################################################
#day 21/11/23

#parts of speech (POS) tagging
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(words)
# it is going mention parts of speech
############################################################
# stop words from nltk library
from nltk.corpus import stopwords
stop_words= stopwords.words("English")
#you can verify 179  stop words in varible explorer
print(stop_words)
sentence1= "I am learning NLP: It is one of the most popular like"
# first we will tokenize the sentance
sentence_words= word_tokenize(sentence1)
print(sentence_words)
##remove the stop_words from the sentance
# now let us filter the sentance1 using stop_words
sentence_no_stops=" ". join([words for words in sentence_words if words not in stop_words])
print(sentence_no_stops)
sentence1
# you can notice that am , is , of, the , most, popular, in are missing from the result
###################################################
# suppose we want to replace words in string
sentence2= 'I visited My from IND on 14-02-19'
normalized_sentence=sentence2.replace("My","Malaysia"). replace("IND", "India")
normalized_sentence=normalized_sentence.replace("-19","-2020")
print(normalized_sentence)
###############################################
#suppose  we want auto correction in the sentence
from autocorrect import Speller
#install the autocorrect 
# declare the function speller definned for english
spell=Speller(lang='en')
spell("Enilish")
######################################
# suppose we want to correct the whole sentence
sentence3= "Ntural lanagage processin deals withh the aart of extracting sentiiiments"
# let us first tokenize sentence
sentence3= word_tokenize(sentence3)
corrected_sentence =" ". join ([spell(word) for word in sentence3])
print(corrected_sentence)
spell("Suitm")




#####################################################################
'''------------------day 22/11/23-------------------------------'''
#stemming
# data preprocessing phase of nlp
import nltk
stemmer=nltk.stem.PorterStemmer()
stemmer.stem("programming")
stemmer.stem("programmed")
stemmer.stem("Jumping")
stemmer.stem("Jumped")

####################################
#lematizer:- mapping the word to the dictionray in the original form
#lematizer looks into dictionary words
nltk.download("wordnet")
from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize("programed")
lemmatizer.lemmatize("programs")
lemmatizer.lemmatize("battling")
lemmatizer.lemmatize("amazing")



# next code is in the google colab

###############################################################################
'''-----------------------------day 23/11/23-------------------------'''

#chunking(shallow parsing )
# identifying named entities
import nltk

nltk.download('punkt')          # it is install here only
from nltk import word_tokenize
nltk.download("maxent_ne_chunker")
nltk.download('words')
sentence4="We are learing NLP in python by SanjivaniAI based in India "
# first we are tokenize
words=word_tokenize(sentence4)
nltk.download('averaged_pwerceptron_tagger')
words=nltk.pos_tag(words)
i=nltk.ne_chunk(words, binary=True)
[a for a in i if len(a)==1]

#########################################
#sentence tokenization
from nltk.tokenize import sent_tokenize
sent= sent_tokenize("we are learning NLP in python . Deliver By sanjivaniAi . Do you Know where it is located? In kopargoan")
sent
############################################
# type of the word or cheking the meaningof the words
from nltk.wsd import lesk
sentence1="keep your saving in the bank"
print(lesk(word_tokenize(sentence1),'bank'))
##output:-Synset('savings_bank.n.02')
sentence2="It is so risky to drive over the banks of the river"
print(lesk(word_tokenize(sentence2),'bank'))
##output Synset('bank.v.07')

##########
##Synset('savings_bank.n.02') a slope in the turn of the road or a track;
# the outside is highre than the inside inorder to reduce the 
##
#"bank " as multiple meaning:- if you wnt to find eaxcat meaning
# excecte the following code
# the defination for the " bank can be seen here
from  nltk.corpus import wordnet as wn
for ss in wn.synsets('bank'):print(ss,ss.definition)
###################################################
'''****************************************************************************'''
'''tokenization___ cleaning of the text'''
# unigram sentence tokenization
import re
sentence5 = "sharat twitted ,Witnessing 70th republic day India from Rajpath,\new Delhi, Mesmorizing performance by Indian Army!"
re.sub(r'([^\s\w]|_)+',' ',sentence5).split()
####Extracting n-grams 
#n-gram can be extracted using three techniques 
#1.custom defined function 
#2.NLTK 
#3.TextBlob 

#################################
#exctrating the n-grams using custom defined function

import re
def n_gram_extractor(input_str,n):      #n number of the tokenizer
    tokens=re.sub(r'([^\s\w]|_)+',' ',input_str).split()
    for i in range(len(tokens)-n+1):
        print(tokens[i:i+n])
        
n_gram_extractor( " The cute little boy is playing with the kitten",2)
n_gram_extractor( " The cute little boy is playing with the kitten",3)


######################################################
from nltk import ngrams
# exctaraction n-grams with nltk
list(ngrams(" The cute little boy is playing with the kitten".split(),2))
list(ngrams(" The cute little boy is playing with the kitten".split(),3))

#########################################
# doing the sentence tokenizer with the another method
from textblob import TextBlob
blob=  TextBlob(" The cute little boy is playing with the kitten.")
blob.ngrams(n=2)
blob.ngrams(n=3)
#####################################################################################



'''*****************************************************************'''
"""day 24/11/23"""

'''Tensor Flow and keras'''
#install the keras, tensor flow
#tokenization using keras,
# keras is most used in tthe deepm learnig for the data cleaning
sentence5 = "sharat twitted ,Witnessing 70th republic day India from Rajpath,\new Delhi, Mesmorizing performance by Indian Army!"
sentence5
from keras.preprocessing.text import text_to_word_sequence
text_to_word_sequence(sentence5)
#################################################
# we are donig the tokenization using the various tecqnuice
#tokenizationn using the textBlob
from textblob import TextBlob
blob=TextBlob(sentence5)
blob.words
#################################################
#Tweet tokenizer
from nltk.tokenize import TweetTokenizer
tweet_tokenizer=TweetTokenizer()
tweet_tokenizer.tokenize(sentence5)

#################################################
#Multi-Word_Expression
from nltk.tokenize import MWETokenizer
sentence5
mwe_tokenizer=MWETokenizer([('republic','day')])
mwe_tokenizer.tokenize(sentence5.split())
mwe_tokenizer.tokenize(sentence5.replace('!',' ').split())
###################################################
#regular Expression tokenizer
from nltk.tokenize import RegexpTokenizer
reg_tokenier=RegexpTokenizer('\w+|\$[\d\.]+|\S+')
reg_tokenier.tokenize(sentence5)
#######################################################
#white space tokenizer
from nltk.tokenize import WhitespaceTokenizer
wh_tokenizer=WhitespaceTokenizer()
wh_tokenizer.tokenize(sentence5)


#######################################################
#wordpuncttokenizer
from nltk.tokenize import WordPunctTokenizer
wp_tokenizer=WordPunctTokenizer()
wp_tokenizer.tokenize(sentence5)
#######################################################
"""----------stemmer---------"""
# it is used to remove the ing ed and last word we can write it before the $ symbol
sentence6='I love playing cricket.Cricket players practices hard in their inn'
from nltk.stem import RegexpStemmer
regex_stemmer= RegexpStemmer('ing$')
' '.join(regex_stemmer.stem(wd) for wd in sentence6.split())
##########################################################
sentence7='Before eating , it would be nice to sanitize your hand with sanitizer'
from nltk.stem.porter import PorterStemmer
ps_stemmer=PorterStemmer()
words=sentence7.split()
' '.join([ps_stemmer.stem(wd) for wd in words])
#######################################################
#lemmatization
import nltk 
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize
nltk.download('wordnet')
lemmatizer=WordNetLemmatizer()
sentence8="The codes executed today are far better than what we executed generally"
words=word_tokenize(sentence8)
' '. join([lemmatizer.lemmatize(word) for word in words])
########################################################

#singularies and pluaralization
from textblob import TextBlob
sentence9=TextBlob("She sells seashells on the seashore")
words=sentence9.words
#we want to make word[2] i.e. seashells in sigular form
sentence9.words[2].singularize()
#o.p:-seashell
# we want word 5 i.e seashore in plurel form
sentence9.words[5].pluralize()
#o.p:-'seashores'
########################################################
#language translation from spanish to english
from textblob import TextBlob
en_blob=TextBlob(u'muy bien')
en_blob.translate(from_lang='es',to='en')
#output:- TextBlob("very good")

########################################################
#custom stopwords removal
from nltk import word_tokenize
sentence9="She sells seashells on the seashore"
custom_stop_word_list=['she','on','the','am','is']
words=word_tokenize(sentence9)
' '.join([word for word in words if word.lower() not in custom_stop_word_list])
#select word which are not defined the list
#o.p:-'sells seashells seashore'
######################################################

'''day 25/11/23'''
#to identify or extracting general features from raw text
# number of the words
# detecte presence of the wh words
#polarity
# subjectivity
#lang identification
#####################
# to identify the number of the words
import pandas as pd
df=pd.DataFrame([["the vaccine for covid-19 will be announced on 1st august "],['Do you know how much expections the world population is having from thiis research?'],['The risk of virus will come to an end on 31st july']])
df.columns=['text']
df
#now let us measure the number of the words

from textblob import TextBlob
df['number_of_words']=df['text'].apply(lambda x:len (TextBlob(x).words))
df['number_of_words']
##########################################
#detect presence of the words wh
wh_words=set(['why','who','which','what','where','when','how'])
df['is_wh_words_present']=df['text'].apply(lambda x:True if len(set(TextBlob(str(x)).words).intersection(wh_words))>0 else False)
df['is_wh_words_present']
#explanation
#intersection words is apply to check if the bothe the sentence are inside that if any is absent or present
# it  is give the true it the intialize  set 
#words are present the given sentence else false

######################
#polarity of the sentence
df['polarity']= df['text'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
#practical natural lang processing by orali
df['polarity']
'''0    0.0
1    0.2
2    0.0
0 means neutral and other are showing as per there needs'''

#######################################
#polarity
sentence10='I like this example very much'
pol=TextBlob(sentence10).sentiment.polarity
pol
########
sentence10='this is fantastic example and i like it very much'
pol=TextBlob(sentence10).sentiment.polarity
pol
#######
sentence10='this was helpful example but i would have prefer another one'
pol=TextBlob(sentence10).sentiment.polarity
pol
###########
sentence10='this is my personal opinion that it was helpful example but i would prefer another one'
pol=TextBlob(sentence10).sentiment.polarity
pol
############
#negative polarity
sentence10='She was not happy to be left alone in the desert'
pol=TextBlob(sentence10).sentiment.polarity
pol

################################################
#subjectivity of the dataframe df and check whether there is any personal opnion
df['subjectivity']= df['text'].apply(lambda x:TextBlob(str(x)).sentiment.subjectivity)
#practical natural lang processing by orali
df['subjectivity']
############################################
#to find the language of the seneetence this part of the code will get http error 
#in the below get error go on the google colab 
df['language']= df['text'].apply(lambda x:TextBlob(str(x)).detect_language())

#what is nlp pipeline intterview

#####################################################################################
'''day 28/11/23'''
#text preprocessing
#bag of words

#how to cnovert the corpus into bags of words
#this BOW converts unstructured data to  structured form
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
corpus=[' At least seven india pharam companies are working to develop vaccine against  the corona virus .',' The deadly virus that has already infected more 14 million globally ','Bharat biotect is the among domantic pharam firm working on the corona virus vaccine in India']
bag_of_word_model=CountVectorizer()
print(bag_of_word_model.fit_transform(corpus).todense())
bag_of_word_df=pd.DataFrame(bag_of_word_model.fit_transform(corpus).todense())
# this is creata edataframe
bag_of_word_df.columns=sorted(bag_of_word_model.vocabulary_)
bag_of_word_df.head()
##############################################################
#bag of the words small
bag_of_word_model_small=CountVectorizer(max_features=5)
bag_of_word_df_small=pd.DataFrame(bag_of_word_model_small.fit_transform(corpus).todense())
# this is creata edataframe
bag_of_word_df_small.columns=sorted(bag_of_word_model_small.vocabulary_)
bag_of_word_df_small.head()
#################################################################
'''day 29/11/23'''
#spam email classification
#Nlp pipeline cycle
#1)data Acquisition process
import pandas as pd 
import numpy as np
#read the csv
df=pd.read_csv("C:/Data Science/11-advanced-NLP/NLP_dataset/spam.csv")
#check the first 10 record
df.head(10)
#total number of spam and ham
df.Category.value_counts()
#create one more column comparises 0 and 1
#name of the column
df['spam']=df['Category'].apply(lambda x:1 if x=='spam' else 0)
df.shape
############################
#2)text extracaction and clean up
#3)pre_processing
#train test split
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test= train_test_split(df.Message, df.spam,test_size=0.2)
#test_size=0.2 means we are taking the teh 20% data fro the testing and
#remaing 80% data is for the training
#let us check the shape of X_train and X_test data
X_train.shape
X_test.shape

#let us check the type of the x_train and y_train
type(X_train)
type(y_train)
################################
#4)feature_engineering
#crete the bag of words representation using CountVectorizer
from sklearn.feature_extraction.text import CountVectorizer
v=CountVectorizer()
X_train_cv=v.fit_transform(X_train.values)
X_train_cv
#after creation of the BoW , let  us check the shape
X_train_cv.shape
###############################
#5)model buliding
#apply to the model
#train the naive bayes model
from sklearn.naive_bayes import MultinomialNB
#intialize the model
model=MultinomialNB()
#train the model
model.fit(X_train_cv,y_train)
################################
#create bag of the words representation using the CountVectorizer
#of  X_test
X_test_cv=v.transform(X_test)
#########################################
#Evalution
#Evaluate performance
from sklearn.metrics import classification_report
y_pred=model.predict(X_test_cv)
print(classification_report(y_test,y_pred))


#aaccuracy is more so the model is over fit



############################################################
'''day 30/11/23'''
#TFIDF algorithm
#use of the tfidf

import pandas as pd
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
corpus=['The mouse had a tiny little mouse','The cat saw the mouse', 'The cat catch the mouse','the end of mouse story']
#step1 intialize the count vector
cv=CountVectorizer()
#to count the total no.of Tf
word_count_vector=cv.fit_transform(corpus)
word_count_vector.shape
#now next step is to apply the idf
tfidf_transform=TfidfTransformer(smooth_idf=True, use_idf=True)
tfidf_transform.fit(word_count_vector)

#this matrix is in raw matrix from let us convert it in dataframe
df_idf= pd.DataFrame(tfidf_transform.idf_, index=cv.get_feature_names_out(), columns=['idf_weights'])
#sort asceding
df_idf.sort_values(by=['idf_weights'])
#notice that the word mouse has lowest frequency beacuse it appear in along

##################################################
#we can without use of the idf we caluclate the idf column
from sklearn.feature_extraction.text import TfidfVectorizer

corpus=[
        ' Thor eating pizza, loki is eating pizza, Ironman ate pizza already',
        ' Apple is announcing new iphone tomorrow',
        'Tesla is announcing new model-3 tomorrow',
        'Google is announcing new pixel-6 tomorrow',
        'Microsoft is  announcing new surface tomorrow',
        'Amazon is announcing new eco-dot tomorrow',
        'I am eating biryani and you are eating grapes'
        ]
# let us create the vectorrizer and fit the corpus and transform them accordingly
v=TfidfVectorizer()
v.fit(corpus)

transform_output= v.transform(corpus)
#lets print the vocabulary

print(v.vocabulary_)
#let us print the idf of each words:

all_feature_names= v.get_feature_names_out()

for word in all_feature_names:
    
    #lets  get the index in the vocabulary
    indx=v.vocabulary_.get(word)
    #get the score
    idf_score=v.idf_[indx]
    print(f'{word}:{idf_score}')


############################################################
'''day 1/12/23'''
#use case of the TF-idf 
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
#read the data into the pandas datframe
df=pd.read_csv("C:/Data Science/11-advanced-NLP/NLP_dataset/Ecommerce_data.csv")

print(df.shape)
df.head(5)

#check the disttribution of the labels
df['label'].value_counts()

#add new cplumn whch gives unique number to each of this label

df['label_num']=df['label'].map({
    'Household':0,
    'Books':1,
    'Electronics':2,
    'Clothing & Accessories':3
    })

#check the result
df.head(5)

from sklearn.model_selection import train_test_split

X_train,X_test, y_train, y_test= train_test_split(
    df.Text,
    df.label_num,
    test_size=0.2,          # 20% samples willl go to the test dataset
    random_state=2022,  #a pseudo-random number parameter that allows
                        #you to reproduce the same train test split each time you run the code.
    stratify=df.label_num   # it not generat the size ofthe element in the equal size 
    )
print('Shape of X_train:', X_train.shape)
print('Shape of X_test:', X_test.shape)
y_train.value_counts()
y_test.value_counts()
##################
#apply to the classifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report
 #1. create a pipleine object


clf=Pipeline([
    ('vectorizer_tfidf', TfidfVectorizer()),
    ('KNN', KNeighborsClassifier())
    ])


#2. fit with X_train and y_train
clf.fit(X_train, y_train)

#3.get th epredications for X_test and store it in y_pred
y_pred= clf.predict(X_test)

#4.print the classification report
print(classification_report(y_test, y_pred))


# it give the accuracy is 96% so it 

######################################
''' word embedding'''

#Cell_Phones_and_Accessories_5

#pip install gensim
#pip install python-levenshtein


import gensim
import pandas as pd

df=pd.read_json("C:/Data Science/11-advanced-NLP/NLP_dataset/Cell_Phones_and_Accessories_5.json")
df
df.shape
#simple preprocessing & tokenization
review_text = df.reviewText.apply(gensim.utils.simple_preprocess())
review_text
# let us check first word of each review
review_text.loc[0]
#let us ceck first row of dataframe

