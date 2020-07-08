from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
a = 0
chromedriver_location = "/Users/andre/Desktop/chromedriver.exe"
driver = webdriver.Chrome(chromedriver_location)
driver.get('http://158.69.76.135/level3.php')
imagen = '/html/body/form/img'
hodor = '/html/body/a/img'
robot = '/html/body/form/input[3]'
enviar = '/html/body/form/input[4]'
text = '/html/body/form/input[1]'
basewidth = 100

while (True):
    if a == 0:
        time.sleep(8)
        a += 1
    else:
        time.sleep(1.5)
    driver.find_element_by_xpath(text).send_keys(1453)
    element = driver.find_element_by_xpath(imagen)
    element.location_once_scrolled_into_view
    driver.save_screenshot("screenshot.png")
    img = Image.open('screenshot.png')
    img_recortada = img.crop((8,0,58,21))
    wpercent = (basewidth/float(img_recortada.size[0]))
    size = int((float(img_recortada.size[1])*float(wpercent)))
    hsize = int((float(img_recortada.size[1])*float(wpercent)))
    img_recortada = img_recortada.resize((basewidth,hsize), Image.ANTIALIAS)
    img_recortada.save("recorte.png")
    img_recortada = img_recortada.convert('L')
    time.sleep(3)
    captcha = pytesseract.image_to_string(img_recortada)
    captcha = captcha.lower()
    driver.find_element_by_xpath(robot).send_keys(captcha)
    time.sleep(2)
    driver.find_element_by_xpath(enviar).click()
driver.quit()