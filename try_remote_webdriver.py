from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability("browserVersion", "67")
chrome_options.set_capability("platformName", "Windows XP")
driver = webdriver.Remote(
    command_executor='http://www.google.com',
    options=chrome_options
)
berlin_immigrant_office = "https://otv.verwalt-berlin.de/ams/TerminBuchen?lang=en&termin=1&dienstleister=327437&anliegen[]=324659&herkunft=1"
driver.get(berlin_immigrant_office)
driver.quit()  
  