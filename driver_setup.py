# import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# os.environ['PATH'] += r"E:/chromedriver"
def get_driver():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    
    driver = webdriver.Chrome(executable_path="E:\\chromedriver\\chromedriver.exe", chrome_options=opt)
    # driver.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")
    return driver
