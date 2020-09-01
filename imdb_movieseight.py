
from imdb_movies1 import*
# movie_url=("https://www.imdb.com/title/tt8108198/")
def scrape_movie_details(movie_url):
    movies_id=movie_url[27:-1]
    movies_path=(f"Movies_Details/{movies_id}.json")
    if os.path.exists(movies_path):
        with open(movies_path,"r") as  file:
             read_fil=file.read()
             file_str=json.loads(read_fil)
        return file_str
        
    top_movies=[]   
    store={
	"Movie_Title": "",
	"Director": [],
	"Country": "",
	"Language":[] ,
	"Poster_image_url": "",
	"Bio": "",
	"RunTime":"",
	"Genres":[]
	}
   
    movie_url=requests.get(movie_url)
    # print (movie_url)
    # response = requests.get(movie_url)
    # htmlcontent=response.content
    # soup=BeautifulSoup(url,"lxml")
    # return soup

    #name
    soup = BeautifulSoup(movie_url,("html.parser"))
    title_movie=soup.find('div',class_='title_wrapper').h1.get_text()
    movie_names=""
    for i in title_movie:
        if '(' not in i:
            movie_names=(movie_names+i).strip()
        else:
            break
    store["Movie_Title"]=movie_names
    
    #rdirector name
    director = soup.find('div', class_='credit_summary_item').get_text().strip()
    a=(director[10:])
    store["Director"]=a
    # director_name
    movie_time=soup.find('div',class_ ='subtext')

    movie_runtime=movie_time.time.get_text().strip()
    movie_hour=movie_runtime[0]
    run_hour=int(movie_hour)*60
    # return movie_runtime
    
    if 'min' in movie_time:
        runtime_min=int(movie_1[3:]).strip('min')
        # return runtime_min
        run_hour_all=runtime_min+run_hour
    else:
        run_hour_all=run_hour
    store["RunTime"] =run_hour_all

    #genre name
    genre=movie_time.a.text
    store["Genres"]=genre
    # return genre
    #summary name
    summary=soup.find('div',class_='summary_text').get_text().strip()
    store["Bio"]= summary
    #urlname
    url_name=soup.find('div',class_='poster').a.img["src"]
    store["Poster_image_url"]=url_name
    #language
    find_country=soup.find("div", id="titleDetails")
    find_all_class=find_country.find_all("div",class_="txt-block")
    count=0
    for i in find_all_class:
        h4_tag=i.find("h4",class_="inline")
        if count==2:
            break
        if h4_tag.get_text() == "Country:":
            country=i.find("a").get_text()
            store["Country"]=country
            count=count+1
		#How many languages in this Movies
        if h4_tag.get_text()=="Language:":
            language=i.find_all("a")
            for i in language:
                store["Language"].append(i.get_text())
            count+=1
        with open(movies_path,"w") as file:
            json.dump(store,file,indent=4)
            return store
scrape_single_movie=(scrape_movie_details("https://www.imdb.com/title/tt8108198/"))
pprint(scrape_single_movie)
