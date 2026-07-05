import requests
import json
import os
from bs4 import BeautifulSoup
from urllib.parse import urljoin

URL = 'https://uakinogo.tv/'
URL_PAGE_2 = 'https://uakinogo.tv/page/2'


def parse_films(url, limit=12):
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, 'html.parser')
    all_found_films = soup.find_all('div', class_='shortstory')

    films_data = []
    for film in all_found_films[:limit]:
        title = film.find('h2').text.strip()

        rating_block = film.find('div', class_='film__rating')
        # ocenka (inogda nety)
        kp_rating = rating_block.find('span', class_='kp').text.strip() if rating_block and rating_block.find('span', class_='kp') else None
        imdb_rating = rating_block.find('span', class_='imdb').text.strip() if rating_block and rating_block.find('span', class_='imdb') else None

        img_tag = film.find('img')
        img_src = img_tag.get('data-src') or img_tag.get('src')
        img_url = urljoin(url, img_src)

        link_tag = film.find('a')
        link_url = urljoin(url, link_tag.get('href')) if link_tag else None

        films_data.append({
            "title": title,
            "kp_rating": kp_rating,
            "imdb_rating": imdb_rating,
            "image": img_url,
            "link": link_url
        })

    return films_data


def save_to_json(movies, filename='movies.json'):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(movies, f, ensure_ascii=False, indent=2)


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

if __name__ == '__main__':
    films = parse_films(URL, limit=12)
    films_page_2 = parse_films(URL_PAGE_2, limit=2)

    all_films = films + films_page_2

    save_to_json(all_films, os.path.join(BASE_DIR, 'movies.json'))
    print(f'Сохранено {len(all_films)} фильмов в movies.json')