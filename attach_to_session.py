from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

# executor_url = driver.command_executor._url
# session_id = driver.session_id

def attach_to_session(executor_url, session_id):
    original_execute = WebDriver.execute
    def new_command_execute(self, command, params=None):
        if command == "newSession":
            # Mock the response
            return {'success': 0, 'value': None, 'sessionId': session_id}
        else:
            return original_execute(self, command, params)
    # Patch the function before creating the driver object
    WebDriver.execute = new_command_execute
    driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={})
    driver.session_id = session_id
    # Replace the patched function with original function
    WebDriver.execute = original_execute
    return driver

bro = attach_to_session('104.16.53.111:443', 'Avoh7DnDy0_KzpmLa')
bro.get('http://ya.ru/')