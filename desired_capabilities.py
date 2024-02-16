
# Create desired capabilities
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities

desired_capabilities = DesiredCapabilities.CHROME.copy()
desired_capabilities['browserName'] = 'chrome'

driver = webdriver.Remote(command_executor='http://192.168.1.15:4444', desired_capabilities=desired_capabilities)
driver = webdriver.Chrome(desired_capabilities=desired_capabilities)


dc= DesiredCapabilities.CHROME.copy()
dc['browserName'] = 'firefox'
driver = webdriver.Remote(command_executor= 'http://localhost:4444/wd/hub', desired_capabilities = dc)
