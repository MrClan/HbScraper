# NOTE: need to have chromeDriver downloaded for correct version of chrome and it's path set in path variable.

import random
import traceback
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

# Get random user-agent for scraping:
def get_user_agent():
    ua_strings = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 "
        "Safari/600.1.25",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 "
        "Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 "
        "Safari/537.85.10",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko",
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36"
    ]

    return random.choice(ua_strings)

user_agent = {'User-Agent': get_user_agent()}
selenium_arguments = [f"user-agent= {user_agent}", "window-size=1400,900", '--silent', '--no-sandbox',
                                    'disable-notifications', '--disable-dev-shm-usage', '--disable-gpu', '--headless']


def setupChromeBrowser():
    chromeDriverPath = 'C:/Selenium/ChromiumDriver/chromedriver.exe'
    chromeOptions = webdriver.ChromeOptions()
    # Mimicking as a client while making a request to server:
    for arg in selenium_arguments:
        chromeOptions.add_argument(arg)
    chromeBrowser = webdriver.Chrome(options=chromeOptions, executable_path=chromeDriverPath)
    return chromeBrowser


def useChromeForScraping(url, chromeBrowser, timeout_in_seconds):    
    try:

        chromeBrowser.get(url)
        # body_page = WebDriverWait(chromeBrowser, 10).until((ec.presence_of_element_located((By.TAG_NAME, 'body'))))

        # Wait for search results to be populated
        product_links = WebDriverWait(chromeBrowser,timeout_in_seconds).until((ec.visibility_of_all_elements_located((By.CLASS_NAME,'lists'))))
        body_page = chromeBrowser.page_source  #WebDriverWait(chromeBrowser, 1).until((ec.presence_of_element_located((By.TAG_NAME, 'body'))))
        l = len(product_links)
        print(f'length={l}')
    except Exception as e:
        print(e)


def setupFirefoxBrowser():
    geckoDriverPath = 'C:/Selenium/GeckoDriver/geckodriver.exe'
    geckoOptions = webdriver.FirefoxOptions()
    geckoOptions.add_argument('--headless')
    # Mimicking as a client while making a request to server:
    for arg in selenium_arguments:
        geckoOptions.add_argument(arg)
    
    geckoBrowser = webdriver.Firefox(options=geckoOptions, executable_path=geckoDriverPath)
    return geckoBrowser

def useFirefoxForScraping(url, geckoBrowser, timeout_in_seconds):
    try:
        # geckoBrowser.implicitly_wait(10)
        geckoBrowser.get(url)
        # WebDriverWait(browser, timeout_in_seconds).until(ec.presence_of_element_located((By.CLASS_NAME, 'resultado_busca')))
        product_links = WebDriverWait(geckoBrowser,timeout_in_seconds).until((ec.visibility_of_all_elements_located((By.CLASS_NAME,'lists'))))
        # WebDriverWait(geckoBrowser, timeout_in_seconds).until(ec.text_to_be_present_in_element((By.TAG_NAME, 'strong'), 'cars'))
        html = geckoBrowser.page_source
        soup = BeautifulSoup(html, features="html.parser")
        print(soup)
    except Exception as e:
        print(e)
        traceback.print_exc()
    finally:
        geckoBrowser.quit()



##########################################################

url = 'https://hamrobazaar.com/search/product?q=cars'

firefoxBrowser = setupFirefoxBrowser()
useFirefoxForScraping(url, firefoxBrowser, 10)

# chromeBrowser = setupChromeBrowser()
# useChromeForScraping(url, chromeBrowser, 10)
