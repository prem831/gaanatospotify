from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_driver():
    opt = webdriver.ChromeOptions()
    opt.add_experimental_option("debuggerAddress", "localhost:8989")
    
    driver = webdriver.Chrome(executable_path="E:\\chromedriver\\chromedriver.exe", chrome_options=opt)
    return driver
