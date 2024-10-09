import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from main import base_url_ui


@pytest.fixture()
def driver():
    service = ChromeService(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.title('UI. Проверка - Поиск фильма по названию (русский язык)')
def test_search(driver):
    with allure.step('Главная страница'):
        driver.get(base_url_ui)
    with allure.step('Ввод названия фильма "Джокер"'):
        driver.find_element(By.NAME, "kp_query").send_keys('Джокер')
    with allure.step('Выбор нужного фильма из списка'):
        driver.find_element(By.ID, 'suggest-item-film-1048334').click()
    with allure.step('Нужный фильм открыт на странице'):
        assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == ("Джокер (2019)")

@allure.title("UI. Проверка - Поиск фильма по названию (английский язык)")
def test_search_2(driver):
    with allure.step('Главная страница'):
        driver.get(base_url_ui)
    with allure.step('Ввод названия фильма "Joker"'):
         driver.find_element(By.NAME, "kp_query").send_keys("Joker")
    with allure.step('Выбор нужного фильма из списка'):
        driver.find_element(By.ID, 'suggest-item-film-1048334').click()
    with allure.step('Нужный фильм открыт на странице'):
        assert driver.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == ("Джокер (2019)")


@ allure.title("UI. Проверка - Поиск актера по имени (русский язык)")
def test_search_3(driver):
    with allure.step('Главная страница'):
        driver.get(base_url_ui)
    with allure.step('Ввод имени актера "Колин Фаррелл"'):
        driver.find_element(By.NAME, "kp_query").send_keys("Колин Фаррелл")
    with allure.step('Выбор нужного актера из списка'):
        driver.find_element(By.ID, 'suggest-item-person-373').click()
    with allure.step('Нужный актер открыт на странице'):
        assert "Колин Фаррелл" in driver.title


@allure.title("UI. Проверка кнопки 'СЛУЧАЙНЫЙ ФИЛЬМ'")
def test_search_4(driver):
    with allure.step('Главная страница'):
        driver.get(base_url_ui)
    with allure.step('Нажатие кнопки поиска "ЛУПА"'):
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    with allure.step('Нажатие кнопки "СЛУЧАЙНЫЙ ФИЛЬМ'):
        driver.find_element(By.CSS_SELECTOR, "input[type='button']").click()
    with allure.step('Проверка отображения рандомного фильма'):
        assert "" in driver.name

@allure.title("UI. Проверка результата поиска при невалидном запросе")
def test_search_5(driver):
    with allure.step('Главная страница'):
        driver.get(base_url_ui)
    with allure.step('Ввод несуществующий запрос "qwertyuiop"'):
        driver.find_element(By.NAME, "kp_query").send_keys('qwertyuiop')
    with allure.step('Нажатие кнопки поиска "ЛУПА"'):
        driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
    with allure.step('Проверка отображения сообщение об ошибке'):
        assert driver.find_element(By.XPATH,"//h2[@class='textorangebig']").text == ("К сожалению, по вашему запросу ничего не найдено...")