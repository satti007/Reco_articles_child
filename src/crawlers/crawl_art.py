import sys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from time import sleep

cap = DesiredCapabilities().FIREFOX
cap["marionette"] = True

def isReady(browser):
    return browser.execute_script("return document.readyState") == "complete"


def waitUntilReady(browser):
    if not isReady(browser):
        waitUntilReady(browser)



class_name = ['k1','g2','g34','g56']
for c in class_name:
    file_name  = c+'_links'
    with open(file_name) as file:
        links = file.readlines()
    links = [x.strip() for x in links]
    links = set(links)
    print len(links)
    # file.close()
    # binary = '/home/anveshbagary/Downloads/geckodriver-v0.20.1-linux64/geckodriver'
    # browser = webdriver.Firefox(capabilities=cap,executable_path=binary)
    # for link in links:
    #     if not '/sections/' in link:
    #         browser.get(link)
    #         sleep(5)
    #         # waitUntilReady(browser)
    #         delay = 100
    #         try:
    #             myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.CLASS_NAME,'_2xsP_Jt7')))
    #         except TimeoutException:
    #             print "Loading took too much time!"
    #         lins = browser.find_elements_by_tag_name('p')
    #         #print len(lins)
    #         abc=link.split('/')
    #         abc = abc[len(abc)-2]
    #         print abc
    #         f = open(c+'/'+abc,'w+',0)
    #         for lin in lins:
    #             x = lin.text
    #             if not x.isupper():
    #                 f.write(x.encode('utf-8').strip()+'\n')
    #         f.close()
    # browser.quit()
