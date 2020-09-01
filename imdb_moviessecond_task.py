from pprint import pprint

from imdb_movies1 import scrape_top_list

def group_by_year(Movies):
    

    lst_of_year=[]
    yearly_movies={}
    for i in Movies:
      
        if i["year"] not in lst_of_year:
            lst_of_year.append(i["year"])
        lst_of_year.sort(reverse=True)
        # print(lst_of_year)
        for j in lst_of_year:
            same_year=[]
            for k in Movies:
           
            
                if j==k["year"]:
                    same_year.append(k)
            yearly_movies[j]=same_year
    return(yearly_movies)
# pprint(group_by_year(scrape_top_list()))
