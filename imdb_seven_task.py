from imdb_movies1 import*
from imdb_fourth_task import*
from imdb_fifth_task import*
def analyse_movies_language(movies_list):
    Director=[]
    unique_lang=[]
    store={}
    data=[]
    b=0
    count=0
    for index in movies_list:
        Director.append(index["Director"])
    for i in Director:
        if i in store:
            store[i]=+1
        else: 
            store[i]=1
    return store   
# pprint(analyse_movies_language(movies_list)) 