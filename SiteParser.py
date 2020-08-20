from bs4 import BeautifulSoup
import requests

class Jokes:
    """
    Парсит с сайта https://nekdo.ru/random/ всякие шутки
    """
    def __init__(self):
        self.heard = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}
        self.__data = BeautifulSoup(requests.get('https://nekdo.ru/random/', headers=self.heard).text, 'html.parser')

    def getJoke(self):
        return self.__data.find('div', {'class': 'text'}).text


class Quotes:
    """
    Парсит с https://citaty.info/random всякие цитаты

    """
    def __init__(self):
        self.heard = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:75.0) Gecko/20100101 Firefox/75.0'}
        self.__data = BeautifulSoup(requests.get('https://citaty.info/random', headers=self.heard).text, 'html.parser')

    def getQuoteMessage(self):
        """
        Возрщает цитату
        :return:
        """
        return self.__data.find('div', {'class': 'field-item even last'}).text
