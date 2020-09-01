from imdb_fifth_task import*
def analyse_language_and_directors(movies_list):
    dic={}
    for movie in movies_list:
        director=(movie["Director"])
        dic[director]={}
    # print(dic)
    for i in range(len(movies_list)):
        

        for director in dic:
            if director in movies_list[i]["Director"]:
                for language in movies_list[i]["Language"]:
                    dic[director][language]=0
    
    for i in range(len(movies_list)):
        for director in dic:
            
            if director in movies_list[i]["Director"]:
                for language in movies_list[i]["Language"]:
                    dic[director][language]+=1
    return (dic)
                 
                
print(analyse_language_and_directors(movies_list))
