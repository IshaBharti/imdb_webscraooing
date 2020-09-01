from imdb_movies1 import*
from imdb_fourth_task import*
from imdb_fifth_task import*

def analyse_movies_language(movies_list):
    lang=[]
    unique_lang=[]
    store={}
    data=[]
    b=0
    count=0
    count_b=[]
    for index in movies_list:
        # print(index)
        lang.append(index["Language"])
    #(lang)
    for i in lang:
        for j in i:
            unique_lang.append(j)
    for i in unique_lang:
        data.append(i)
    
    for i in data:
        if i in store:
            store[i]+=1
        else:
            store[i]=1

    return store


        
# print(analyse_movies_language(movies_list))        
    

