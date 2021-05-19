#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup

def get_movies():
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
        'Host':'movie.douban.com'
    }

    fd = open("movies.txt", "a+")
    movie_list = []
    index = 0
    for i in range(0, 10):
        link = 'https://movie.douban.com/top250?start=' + str(i * 25)
        r = requests.get(link, headers= headers, timeout= 10)
        print(str(i+1), "页面状态响应码:", r.status_code)

        soup = BeautifulSoup(r.text, "html.parser")
        div_list = soup.find_all('span', class_='title')
        
        for each in div_list:
            movie = each.text.strip()
            print(movie)
            if movie[0] != '/':
                print(movie)
                index = index+1
                fd.write(str(index) + ": " + movie + "\n")
                movie_list.append(movie)
            else:
                continue
    fd.close
    return movie_list
        
movies = get_movies()
#print(movies)
