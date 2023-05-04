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

    # operation.printWebsiteName()
    # operation.printWebsiteUrl()
    DRIVER_PATH = '/drivers/chromedriver'
    CHROME_PATH = '~/Library/Application Support/Google/Chrome'
    # driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    # driver.get('https://google.com')

    options = Options()
    options.headless = False
    # options.add_argument("--window-size=1920,1200")

    bookAppointmentUrl = "https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng?sprachauswahl=en"
    berlin_immigrant_office = "https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en&termin=1&dienstleister=327437&anliegen[]=324659&herkunft=1"
    service_selection = "https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/33f46046-1f80-47eb-9b7b-9899cc539472?dswid=3347&dsrid=837&st=2&v=1677946353785"
    checkboxID = "xi-cb-1"
    checkboxNAME = "gelesen"

    main_page = "https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en"
    driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    # Land in main page
    driver.get(main_page)
    continue_link = driver.find_element(By.LINK_TEXT, 'Book Appointment')
    continue_link.click()
    driver.implicitly_wait(4)
    driver.quit()
    
    # Click to Termin Buchen Button
    time.sleep(4)
    select = Select(driver.find_element(By.NAME, 'sel_staat'))
    select.select_by_value("163")
    time.sleep(1)
    select = Select(driver.find_element(By.NAME, 'personenAnzahl_normal'))
    select.select_by_value("1")
    time.sleep(1)
    select = Select(driver.find_element(By.NAME, 'lebnBrMitFmly'))
    select.select_by_value("2")
    time.sleep(1)
    # driver.find_element(By.XPATH, "//input[@class='ozg-kachel kachel-163-0-2 level1']/input[@id='SERVICEWAHL_EN3163-0-2']").click()
    driver.find_element(By.XPATH, ".//input[@type='radio' and @value='163-0-2']").send_keys()
    # driver.find_element(By.XPATH, "//div[@class='level3']/input[@name='level3']").click()
    time.sleep(5)

    # print("here")
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='link']/a[@href='/ams/TerminBuchen/wizardng?sprachauswahl=en']").click()
    time.sleep(2)
    # Check the gelesen checkbox
    # print(element)
    # write_html(element.page_source)

    driver.find_element(By.XPATH, "//div[@class='x label-right CXCheckbox']/input[@class='XItem XCheckbox left-right']").click()
    time.sleep(2)
        
    driver.quit()