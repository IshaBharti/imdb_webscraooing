from imdb_movies1 import*
from imdb_fourth_task import*
def get_movie_list_details(movies_list):
    url_list=[]

    top_movies_details=[]
    for i in movies_list[:25]:
        url_list.append(i["urls"])
    # return url_list

    for link_url in url_list:
            # print(link_url)
        top_movies_details.append(scrape_movie_details(link_url))
    return(top_movies_details)
movies_list=(get_movie_list_details(movies))
# pprint(movies_list)

        