import requests
from bs4 import BeautifulSoup
from pprint import pprint
url="https://www.imdb.com/title/tt0066763/fullcredits"

def scrape_movie_cast(movie_cast_url):
    response=requests.get(url)
    data=response.text
    soup = BeautifulSoup(data, "html.parser")
    movies_name=soup.find("table",class_="cast_list")
    name=movies_name.findAll("td",class_="")
    casr_list=[]
    for i in name:
        actor_dic={}
        imdb_name=i.find('a').get('href')[6:15]
        imdb_id=i.getText().strip()
        actor_dic['imdb_name']=str(imdb_id)
        actor_dic['imdb_id']=str(imdb_name)
        casr_list.append(actor_dic)
    return(casr_list)
# pprint(scrape_movie_cast(url))           