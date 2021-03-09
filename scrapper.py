"""
Crawler implementation
"""

import re
import os
import requests
import json
from bs4 import BeautifulSoup
from constants import CRAWLER_CONFIG_PATH, ASSETS_PATH


class IncorrectURLError(Exception):
    """
    Custom error
    """


class NumberOfArticlesOutOfRangeError(Exception):
    """
    Custom error
    """


class IncorrectNumberOfArticlesError(Exception):
    """
    Custom error
    """


class UnknownConfigError(Exception):
    """
    Most general error
    """


class Crawler:
    """
    Crawler implementation
    """
    def __init__(self, seed_urls: list, max_articles: int):
        self.search_urls = seed_urls
        self.max_articles = max_articles
        self.found_urls = []
        self.link_pattern = r'/?news-\d+-\d+\.htm'

    def _extract_url(self, article_bs):
        links = []
        for link in article_bs.find_all('a', href=True):
            potential_link = re.match(self.link_pattern, link['href'])
            if potential_link:
                links.append(potential_link.group(0))
        return links

    def find_articles(self):
        """
        Finds articles
        """
        for url in self.search_urls:
            request = requests.get(url).content
            soup = BeautifulSoup(request,
                                 features='lxml')
            for article_url in self._extract_url(soup):
                if len(self.found_urls) != self.max_articles \
                        and url+article_url not in self.found_urls:
                    self.found_urls.append(url+article_url)

    def get_search_urls(self):
        """
        Returns seed_urls param
        """
        return self.found_urls


class ArticleParser:
    """
    ArticleParser implementation
    """
    def __init__(self, full_url: str, article_id: int):
        pass

    def _fill_article_with_text(self, article_soup):
        pass

    def _fill_article_with_meta_information(self, article_soup):
        pass

    @staticmethod
    def unify_date_format(date_str):
        """
        Unifies date format
        """
        pass

    def parse(self):
        """
        Parses each article
        """
        pass


def prepare_environment(base_path):
    """
    Creates ASSETS_PATH folder if not created and removes existing folder
    """
    if not os.path.exists(base_path):
        os.makedirs(base_path)


def validate_config(crawler_path):
    """
    Validates given config
    """
    with open(crawler_path, 'r', encoding='utf-8') as data:
        settings = json.load(data)
    url_pattern = 'https://'

    for url in settings['base_urls']:
        if url_pattern not in url:
            raise IncorrectURLError

    if not isinstance(settings['total_articles_to_find_and_parse'], int):
        raise IncorrectNumberOfArticlesError

    if settings['total_articles_to_find_and_parse'] > 100:
        raise NumberOfArticlesOutOfRangeError
    return settings['base_urls'], settings['total_articles_to_find_and_parse']


if __name__ == '__main__':
    urls, num_articles = validate_config(CRAWLER_CONFIG_PATH)
    prepare_environment(ASSETS_PATH)

    crawler = Crawler(seed_urls=urls, max_articles=num_articles)
    crawler.find_articles()
    print(crawler.get_search_urls())
