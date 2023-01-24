# Description: This program will scrape the Hacker News website and find the article with the highest score using BeautifulSoup
# Author: Pinak Mehta

from bs4 import BeautifulSoup
import requests


def highest_upvote():
    # get the web page
    response = requests.get(url="https://news.ycombinator.com/")
    yc_web_page = BeautifulSoup(response.text, "html.parser")

    article_titleline_tag = yc_web_page.find_all(
        name="span", class_="titleline")
    article_score_tag = yc_web_page.find_all(name="span", class_="score")

    # create a list of article title
    article_title = [article_titleline_tag[i].a.getText()
                     for i in range(len(article_titleline_tag))]
    # create a list of article link
    article_link = [article_titleline_tag[i].a.get(
        "href") for i in range(len(article_titleline_tag))]
    # create a list of article score
    article_score = [int((article_score_tag[i].getText()).split()[0])
                     for i in range(len(article_score_tag))]
    # find the highest score article
    larget_score = max(article_score)
    # find the index of the highest score article text
    highest_score_article_text = article_title[article_score.index(
        larget_score)]
    # find the index of the highest score article link
    highest_score_artocle_link = article_link[article_score.index(
        larget_score)]

    print(
        f"The highest score article is {highest_score_article_text} with a score of {larget_score} and the link is {highest_score_artocle_link}")


# call the function
highest_upvote()
