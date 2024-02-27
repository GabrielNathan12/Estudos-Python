from pathlib import Path
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# chromedriver está para suportar a versão 122 do chrome


# Caminho para a raiz do projeto
ROOT_FOLDER = Path(__file__).parent
# Caminho para a pasta onde o chromedriver está
CHROME_DRIVER_PATH = ROOT_FOLDER / 'bin' / 'chromedriver.exe'

def make_chrome_browser(*options: str) -> webdriver.Chrome:
    chrome_options = webdriver.ChromeOptions()

    # chrome_options.add_argument('--headless')
    if options is not None:
        for option in options:
            chrome_options.add_argument(option)  # type: ignore

    chrome_service = Service(
        executable_path=str(CHROME_DRIVER_PATH),
    )

    browser = webdriver.Chrome(
        service=chrome_service,
        options=chrome_options
    )

    return browser


if __name__ == '__main__':
    TIME_TO_WAIT = 30
    # Example
    # options = '--headless', '--disable-gpu',
    options = ()
    browser = make_chrome_browser(*options)

    browser.get('https://www.google.com')
    search_input = WebDriverWait(browser, TIME_TO_WAIT).until(
        EC.presence_of_element_located(
            (By.NAME, 'q')
        )
    )
    search_input.send_keys('Elden Ring')
    search_input.send_keys(Keys.ENTER)

    results = browser.find_element(By.ID, 'search')
    links = results.find_elements(By.TAG_NAME, 'a')
    links[0].click()
    sleep(TIME_TO_WAIT)