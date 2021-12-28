import requests
from bs4 import BeautifulSoup
import psycopg2
import time

# BD connect
connection = psycopg2.connect(database="metro", user="postgres", password="*****", host="localhost", port="5432")


# Postgresql add data
def add_data(values):
    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO "news" (url, image, description, date) VALUES (%s,%s,%s,%s)"""
    record_to_insert = values
    cursor.execute(postgres_insert_query, record_to_insert)
    connection.commit()


# PG exist test
def exist_test(url):
    cur = connection.cursor()
    cur.execute("select url from news where url=%s", (url,))
    if cur.fetchone():
        return False
    else:
        return True


# Date converter
def convert_date(date):
    if "декабря" in date:
        return "2021-12-" + date.split(" ")[0]
    elif "ноября" in date:
        return "2021-11-" + date.split(" ")[0]
    elif "октября" in date:
        return "2021-10-" + date.split(" ")[0]
    elif "сентября" in date:
        return "2021-09-" + date.split(" ")[0]
    elif "августа" in date:
        return "2021-08-" + date.split(" ")[0]
    elif "июля" in date:
        return "2021-07-" + date.split(" ")[0]
    elif "июня" in date:
        return "2021-06-" + date.split(" ")[0]
    elif "мая" in date:
        return "2021-05-" + date.split(" ")[0]
    elif "апреля" in date:
        return "2021-04-" + date.split(" ")[0]
    elif "марта" in date:
        return "2021-03-" + date.split(" ")[0]
    elif "февраля" in date:
        return "2021-02-" + date.split(" ")[0]
    elif "января" in date:
        return "2021-01-" + date.split(" ")[0]

while True:
    # BS4 preparationpip freeze > my_flask_app/requirements.txt
    url = "https://mosmetro.ru/news/"
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    news = soup.find_all("a", {"class": "news-card"})

    # Get description, url, date, image
    for i in range(len(news)):
        news_url = "https://mosmetro.ru" + news[i].get('href')
        news_image = news[i].find("div", {"class": "news-card__image"}).get('style').split('url(')[1][:-1]
        news_description = news[i].find("div", {"class": "news-card__caption"}).get_text()
        news_date = convert_date(news[i].find("div", {"class": "news-card__date"}).get_text())
        data = (news_url, news_image, news_description, news_date)
        if exist_test(news_url):
            add_data(data)
    time.sleep(600)
    print("next pars")
