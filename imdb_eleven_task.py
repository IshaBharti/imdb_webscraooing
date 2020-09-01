from imdb_fifth_task import*
from imdb_fourth_task import*
from imdb_movies1 import*
def analyse_movie_genre(movies_list):
    genres={}
    lst=[]
    dict={}

    
    for  i in movies_list[:50]:
        a=(i["Genres"])
        lst.append(a)
    for string in lst:
        if string in dict.keys():
            dict[string] += 1
        else:
            dict[string] = 1
    return(dict)
        


        

        
    
print(analyse_movie_genre(movies_list))
        