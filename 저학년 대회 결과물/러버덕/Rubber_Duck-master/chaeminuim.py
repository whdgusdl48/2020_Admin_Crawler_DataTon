import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

waiting_sec = 5


def getDriver(Debug=False):
    DRIVER_PATH = './chromedriver.exe'
    USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 ' \
                 'Safari/537.36 '
    options = webdriver.ChromeOptions()
    if not Debug:
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument('disable-gpu')
    options.add_argument('--start-maximized')
    options.add_argument('user-agent={0}'.format(USER_AGENT))  # for pretend not to be a bot
    options.add_argument('incognito')  # for secret window
    chrome_driver = webdriver.Chrome(DRIVER_PATH, options=options)
    return chrome_driver


def click_element(element, driver, ctrl=False):
    if ctrl:
        element.send_keys(Keys.CONTROL + Keys.ENTER)
    else:
        driver.execute_script("arguments[0].click();", element)


def wait(by, div, driver):
    time.sleep(.1)
    WebDriverWait(driver, waiting_sec).until(EC.presence_of_element_located((by, div)))


def click(by, div, driver, isWait=True, ctrl=False):
    if isWait:
        wait(by, div, driver)
    if ctrl:
        driver.find_element(by, div).send_keys(Keys.CONTROL + Keys.ENTER)
    else:
        driver.execute_script("arguments[0].click();", driver.find_element(by, div))
