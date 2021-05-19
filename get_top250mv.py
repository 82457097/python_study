import requests
from bs4 import BeautifulSoup

def get_movies():
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Host':'movie.douban.com'
    }

    fd = open("movies.txt", "a+")
    movie_list = []
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers= headers, timeout= 10)
        print(str(i+1), "页面响应状态码:", r.status_code)

        soup = BeautifulSoup(r.text, "html.parser")
        div_list = soup.find_all('span', class_='title')
        for each in div_list:
            print(each)
            movie = each.text.strip()
            fd.write(movie)

            movie_list.append(movie)

    fd.close
    return movie_list
        
movies = get_movies()
#print(movies)
