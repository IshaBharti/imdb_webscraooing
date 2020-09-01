from pprint import pprint

from imdb_movies1 import scrape_top_list


def group_by_decade(Movies):
    start_year=1950
    decade_year=[]
    lst_year=[]
    movies_list_by_decade=[]
    for i in Movies:
        lst_year.append(i["year"])
        # print(lst_year)
    for i in range(start_year,2020,9):
            decade_year.append(i)
            # print(decade_year)
    decade_year.sort 
    # print( decade_year)
    for i in decade_year:
        # print(i)
        movie_store_in_dict={}
        movie_store_in_dict[i]=[]
        for j in Movies:
            if j["year"] >= i and j["year"] <= i+9:
                movie_store_in_dict[i].append(j) 
        # pprint (movie_store_in_dict)
        movies_list_by_decade.append(movie_store_in_dict)
    return(movies_list_by_decade)
# pprint((group_by_decade(scrape_top_list())))
