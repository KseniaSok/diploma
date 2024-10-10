import allure
from Test.kinopoisk import Kinopoisk
from main import base_url,headers


api = Kinopoisk(base_url+'movie')

@allure.title('API. Проверка - Поиск фильма по названию')
def test_get_movie_by_name():
    with allure.step('Получить список фильмов с названием Naruto'):
        resp = api.get_by_name("Naruto",headers)
        response = resp.json()['docs'][0]['internalNames']
    with allure.step('Проверка - полученный список совпадает c названием фильма'):
        assert response.count('Naruto')
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200

@allure.title('API. Проверка - Поиск фильма по году выпуска')
def test_get_movie_by_date():
    with allure.step('Получить список фильмов 2000 года выпуска'):
        resp = api.get_by_name(2000,headers)
        response = resp.json()['docs'][0]['year']
    with allure.step('Проверка - полученный список фильмов совпадает c годом выпуска'):
        assert response == 2000
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200

@allure.title('API. Проверка - Поиск по рейтингу')
def test_get_movie_by_rating():
    with allure.step('Получить список фильмов с рейтингом 8 у кинопоиска'):
        resp = api.get_by_rating(8,headers)
        response = resp.json()['docs'][0]['rating']['kp']
    with allure.step('Проверка - полученный список фильмов совпадает с рейтингом 8'):
        assert response == 8
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200

@allure.title('API. Проверка - Получить список аниме')
def test_movie_by_type():
    with allure.step('Получить список аниме'):
        resp = api.get_by_type("anime",headers)
        response = resp.json()['docs'][0]['type']
    with allure.step('Проверка - полученный список аниме'):
        assert response == "anime"
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200

@allure.title('API. Проверка - Получить список топ 250')
def test_get_list_top_250():
    with allure.step('Получить список фильмов топ 250'):
        resp = api.get_list_top_250(headers)
        response = resp.json()['docs']
    with allure.step('Проверка - полученный список топ 250'):
        assert len(response) == 250
    with allure.step('Статус код = 200'):
        assert resp.status_code == 200