from selenium import webdriver

chromedriver_location = "/Users/andre/Desktop/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.get('http://158.69.76.135/level0.php')
enviar = '/html/body/form/input[2]'
text = '/html/body/form/input[1]'

while (True):
    driver.find_element_by_xpath(text).send_keys(1453)
    driver.find_element_by_xpath(enviar).click()

driver.quit()

