import requests
from bs4 import BeautifulSoup
from pprint import pprint


import os.path
import random
import time

import json

def scrape_top_list():
    
    if os.path.isfile('data_extract.json'):
        with open("data_extract.json") as file:
            read_file=file.read()
            file_store=json.loads(read_file)
        
        return(file_store)
    url1 = ("https://www.imdb.com/india/top-rated-indian-movies/")
    url=url1.text

    

    soup=BeautifulSoup(url, "html.parser") 
    movie_containers=soup.find("tbody",class_="lister-list")
    movie=movie_containers.find_all("tr")
# print(movie
    c=1 
    movies=[]
    years=[]
    ratings=[]
    urls=[]
    position=[]
    c=0
    b=[]

    j=0
    k=0
    l=0
    imdb=[]
    for i in movie:
        find=i.find_all("td")
        movie=(find[1].a.text)
        movies.append(movie)
        year=find[1].span.text
        second=(year[1:5])
        integar=int(second)
        # print(integar)

        years.append(second)
        rate=find[2].strong["title"]

        rating=(rate[0:3])
        ratings.append(rating)
    
        link=i.find("td", class_="posterColumn").a["href"]
        url="https://www.imdb.com"+link
        urls.append(url)
        position.append(c)
    
    
        c=c+1
    # details=['position' ,"names",'years','ratings','urls']
        a=[movies[j],years[j],ratings[j],urls[j],position[j]]
    
        data = {"position": position[j],
            "year": integar,
            "names": movies[j],
           
            
            "rating": ratings[j],
           
            "urls": urls[j]}
        imdb.append(data)
        j=j+1
    # return(imdb)
    with open("data_extract.json","w") as file:
        json.dump(imdb,file)
    return imdb

movies=scrape_top_list()
# pprint(movies)