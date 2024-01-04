import pytest
from Test_Data import imdb_data
from Test_Locators import imdb_locators
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class TestAdvSearch:

    @pytest.fixture()
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()

    # Search function with multiple selectors, each field and button names are mentioned
    def test_key_search(self, booting_function):
        self.driver.maximize_window()
        self.driver.get(imdb_data.data().url)
        self.driver.implicitly_wait(20)
        self.wait = WebDriverWait(self.driver, 30)
        self.act = ActionChains(self.driver)
        signin = self.wait.until(EC.presence_of_element_located((By.XPATH, imdb_locators.locators().sign_in)))
        signin.click()
        # used for loop multiple place to move the screen accordingly
        for _ in range(9):
            self.act.send_keys(Keys.DOWN).perform()
        expand_all = self.wait.until(EC.presence_of_element_located((By.XPATH, imdb_locators.locators().exp_all)))
        expand_all.click()
        # Title name
        title_name = self.wait.until(EC.presence_of_element_located((By.ID, imdb_locators.locators().name)))
        title_name.send_keys(imdb_data.data().name)
        # Birth date from
        bd_from = self.wait.until(EC.presence_of_element_located((By.ID, imdb_locators.locators().birth_from)))
        bd_from.send_keys(imdb_data.data().birth_from)
        # Birth date to
        bd_to = self.wait.until(EC.presence_of_element_located((By.ID, imdb_locators.locators().birth_to)))
        bd_to.send_keys(imdb_data.data().birth_to)
        for _ in range(9):
            self.act.send_keys(Keys.DOWN).perform()
        # Birth month and date
        b_m_d = self.wait.until(EC.presence_of_element_located((By.NAME, imdb_locators.locators().month_date)))
        b_m_d.send_keys(imdb_data.data().month_date)
        for _ in range(9):
            self.act.send_keys(Keys.DOWN).perform()
        # Page topics
        trivia = self.wait.until(EC.presence_of_element_located((By.XPATH, imdb_locators.locators().trivia)))
        trivia.click()
        for _ in range(9):
            self.act.send_keys(Keys.DOWN).perform()
        # Topic dropdown
        t_dd = self.wait.until(EC.presence_of_element_located((By.XPATH, imdb_locators.locators().topic_dd)))
        t_dd.click()
        # example input box
        eg = self.wait.until(EC.presence_of_element_located((By.XPATH, imdb_locators.locators().eg_input)))
        eg.send_keys(imdb_data.data().eg_input)
        # death date from
        dd_from = self.wait.until(EC.presence_of_element_located((By.NAME, imdb_locators.locators().death_from)))
        dd_from.send_keys(imdb_data.data().death_from)
        dd_to = self.wait.until(EC.presence_of_element_located((By.NAME, imdb_locators.locators().death_to)))
        dd_to.send_keys(imdb_data.data().death_to)
        for _ in range(5):
            self.act.send_keys(Keys.DOWN).perform()
        # gender
        male = self.wait.until(EC.presence_of_element_located((By.XPATH, imdb_locators.locators().gender)))
        male.click()
        for _ in range(5):
            self.act.send_keys(Keys.DOWN).perform()
        # Adult name
        include = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, imdb_locators.locators().include)))
        include.click()
        # result
        see_res = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, imdb_locators.locators().result)))
        see_res.click()
        for _ in range(20):
            self.act.send_keys(Keys.UP).perform()
        res_data = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, imdb_locators.locators().res_data)))
        res_data.click()
        assert imdb_data.data().Res_url == self.driver.current_url
