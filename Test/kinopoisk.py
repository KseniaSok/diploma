import requests


class Kinopoisk:
    def __init__(self, url) -> None:
        self.url = url

    def get_by_name(self, value, headers):
        """
        :param value: Название фильма
        :param headers: API-KEY
        :return: response
        """
        my_params = {
            'page': '1',
            'limit': '10',
            'query': value
        }
        response = requests.get(self.url + '/search', params=my_params, headers=headers)
        return response

    def get_by_date(self, value, headers):
        """
        :param value: Год выпуска фильма
        :param headers: API-KEY
        :return: response
        """
        params = {
            'page': '1',
            'limit': '10',
            'year': value
        }
        response = requests.get(self.url, params=params, headers=headers)
        return response

    def get_by_rating(self, value, headers):
        """
        :param value: Рейтинг кинопоиска
        :param headers: API-KEY
        :return: response
        """
        params = {
            'page': '1',
            'limit': '10',
            'rating.kp': value
        }
        response = requests.get(self.url, params=params, headers=headers)
        return response

    def get_by_type(self, value, headers):
        """
        :param value: Жанр фильма
        :param headers: API-KEY
        :return: response
        """
        params = {
            'page': '1',
            'limit': '10',
            'type': value
        }
        response = requests.get(self.url, params=params, headers=headers)
        return response

    def get_list_top_250(self, headers):
        """
        :param headers: API-KEY
        :return: response
        """
        params = {
            'limit': '250',
            'lists': 'top250'
        }
        response = requests.get(self.url, params=params, headers=headers)
        return response