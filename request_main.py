from operations import Operation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.ui import Select

def write_file(output: str):
    with open('output.txt', 'w') as f:
        f.write(output)
def write_html(output: str):
    with open('output.html', 'w') as f:
        f.write(output)

if __name__ == "__main__":
    # operation = Operation("Berlin Immigration Office", "https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en")

    CHROME_PATH = '~/Library/Application Support/Google/Chrome'
    main_page = "https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en"
    driver = webdriver.Chrome(executable_path=CHROME_PATH)
    # driver.get(main_page)

    import requests
    r = requests.get('https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng')
    ams_url = "ams/TerminBuchen/wizardng;jsessionid="
    restoftheurl = str(r.content).split(ams_url)[1].split("\'")[0]

    redirectUrl = "https://otv.verwalt-berlin.de/" + ams_url + restoftheurl
    driver.get(redirectUrl)

    time.sleep(2)
    driver.quit()