# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 08:32:49 2023

@author: suraj
"""
'''Recommendation  System'''
# anime.csv
#
import pandas as pd
anime= pd.read_csv("C:/Data Science/data_set/anime.csv", encoding="utf-8")
anime.shape
# you will get 12297X7 matrix
anime.columns
anime.genre
#here we are considering only genre

from sklearn.feature_extraction.text import TfidfVectorizer
#this is term frequency inverse document
# each row is treated as document
tfidf=TfidfVectorizer(stop_words='english')
#it is  going to create TfidfVectorizer to separate all stop words
# it is going to separete
# out all words from the rows
# now let us check is there any null value
anime['genre']=anime['genre'] .fillna('general') #simple iputation
# now let us create  tfidf_matrix
tfidf_matrix=tfidf.fit_transform(anime.genre)
tfidf_matrix.shape
# now will get 12294,47
# it has created the sparse matris it means
# that we have 47 genre
# on this particular matrix
# we want to do item based recommendation , if a user has
# watched Gadar , then you can recommend Shershah movie
from sklearn.metrics.pairwise import linear_kernel
# this is for measuring similarity
cosine_sim_matrix= linear_kernel(tfidf_matrix, tfidf_matrix)
# each element of tfidf_matrix is compared
# with each element of tfidf_matrix only
#output will be similarity matrix of size 12294X122294 size
#here is cosine_sim_matrix
# there are no movies name only idex are provided
# we will try to map movie names only index are provided
# we will try to map movies name  with movie index given
# for that purpose  custom function is written
anime_index=pd.Series(anime.index,index=anime['name']).drop_duplicates() 
# we are convertinng anime_index into series format , we want index and corresponding movie length
anime_id= anime_index['Assassins (1995)']
anime_id


def get_recommendations(Name, topN):
    topN=10
    Name='Assassins (1995)'
    anime_id=anime_index[Name]
    
    
    #we want  to capture whole row of given movie
    # name , its score and column id
    # for that purpose we are applying cosine_sim_matrix to enumerate function
    # Enumerate function create a object,
    # which we need to create in list form 
    # we are using enumerate function,
    # what enumaret does , suppose we have given
    #(2, 10, 15,18) if we applying to enumaret then it will create a list
    #(0,2  1,10  3,15  4,18)
    cosine_scores= list(enumerate(cosine_sim_matrix[anime_id]))
    # the cosine score captured ., we want to arrange in desecding order so that
    # we can recomment top 10 based on highest similarity i.e. score
    # if we will check the cosune score , itt somprise of index:cosine score
    #x[0] = index and x[1] is cosine score
    # we want arrange tupples according to decreasing order
    # of the score not index
    # sorting the cosine_similarity scores based on score ie x[1]
    cosine_scores=sorted(cosine_scores, key= lambda x:x[1] , reverse=True)
    #  get the scores of top N most similar movies
    # to caputre TopN movies , you need to give topN+1
    cosine_scores_N= cosine_scores[0: topN+1]
    #getting the movies index
    anime_idx=[i[0] for i in cosine_scores_N]
    #getting the cosine score
    anime_scores=[i[1] for i in cosine_scores_N]
    # we are going to use this information to create a dataframe
    #  create a empty dataframe
    anime_similar_show= pd. DataFrame(columns=['name', 'score'])
    # assign anime_idx to name column
    anime_similar_show['name']= anime.loc[anime_idx, 'name']
    #assign score to score column
    anime_similar_show['score'] = anime_scores
    # while assigning values , it is by default capturingg original index of the movies 
    # we want to reset the index
    anime_similar_show.reset_index(inplace=True)
    print(anime_similar_show)


# enter your anime and number of anime to be recommendation
get_recommendations('Bad Boys (1995)', topN=10)






