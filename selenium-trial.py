from operations import Operation
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

def write_file(output: str):
    with open('output.txt', 'w') as f:
        f.write(output)
def write_html(output: str):
    with open('output.html', 'w') as f:
        f.write(output)

# operation.printWebsiteName()
# operation.printWebsiteUrl()
DRIVER_PATH = '/drivers/chromedriver'
CHROME_PATH = '~/Library/Application Support/Google/Chrome'
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
# driver.get('https://google.com')

options = Options()
# options.headless = False
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--disable-popup-blocking")
# options.add_argument("--headless")
options.add_argument("--window-size=1920,1200")

bookAppointmentUrl = "https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng?sprachauswahl=en"
berlin_immigrant_office = "https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en&termin=1&dienstleister=327437&anliegen[]=324659&herkunft=1"
service_selection = "https://otv.verwalt-berlin.de/ams/TerminBuchen/wizardng/33f46046-1f80-47eb-9b7b-9899cc539472?dswid=3347&dsrid=837&st=2&v=1677946353785"
checkboxID = "xi-cb-1"
checkboxNAME = "gelesen"

main_page = "https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en"
# driver = webdriver.Chrome(executable_path=DRIVER_PATH)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

def land_in_main_page():
    # Land in main page
    driver.get(main_page)
    time.sleep(2)
    continue_link = driver.find_element(By.LINK_TEXT, 'Book Appointment')
    continue_link.click()
    time.sleep(5)
    # driver.quit()

    gelesen_checkbox = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, checkboxNAME)))
    gelesen_checkbox.click()
    time.sleep(2)
    # Click the "Next" button
    next_button = driver.find_element(By.NAME, "applicationForm:managedForm:proceed")
    next_button.click()
    time.sleep(60)
    # Click to Termin Buchen Button

    select = Select(driver.find_element(By.NAME, 'sel_staat'))
    select.select_by_value("163")
    time.sleep(1)
    select = Select(driver.find_element(By.NAME, 'personenAnzahl_normal'))
    select.select_by_value("1")
    time.sleep(1)
    select = Select(driver.find_element(By.NAME, 'lebnBrMitFmly'))
    select.select_by_value("2")
    time.sleep(2)

    driver.find_element(By.XPATH, "//div[@class='ozg-kachel kachel-163-0-2 level1']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//div[@class='ozg-accordion accordion-163-0-2-1 level2']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "//input[@id='SERVICEWAHL_EN163-0-2-1-324659']").click()
    time.sleep(5)

    try:
        driver.find_element(By.XPATH, "//div[@class='buttons right']").click()
        time.sleep(20)
    except:
        print("clicking to right button error handled")


while(True):
    land_in_main_page()
    while(driver.find_element(By.XPATH, "//div[@id='progressBar']").text > "01:30"):
        time.sleep(2)
        driver.refresh()
        time.sleep(4)
        driver.switch_to.alert.accept()
        time.sleep(60)
        select = Select(driver.find_element(By.NAME, 'sel_staat'))
        select.select_by_value("163")
        time.sleep(1)
        select = Select(driver.find_element(By.NAME, 'personenAnzahl_normal'))
        select.select_by_value("1")
        time.sleep(1)
        select = Select(driver.find_element(By.NAME, 'lebnBrMitFmly'))
        select.select_by_value("2")
        time.sleep(2)

        driver.find_element(By.XPATH, "//div[@class='ozg-kachel kachel-163-0-2 level1']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//div[@class='ozg-accordion accordion-163-0-2-1 level2']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@id='SERVICEWAHL_EN163-0-2-1-324659']").click()
        time.sleep(30)

        try:
            driver.find_element(By.XPATH, "//div[@class='buttons right']").click()
            time.sleep(10)
        except:
            print("clicking to right button error handled")

        print(driver.find_element(By.XPATH, "//li[@class='errorMessage tabindex=']").text)
        time.sleep(30)