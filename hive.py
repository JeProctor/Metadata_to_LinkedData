from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import csv
import pandas as pd
import rdflib
import re

def getLongest(item_str, web_str):
    longest_match = ''
    for match in re.finditer(r'(?:\b%s\b\s?)+' % item_str, web_str):
        if len(match.group(0)) > len(longest_match):
            longest_match = match.group(0)
    return longest_match

##Enter your namespace for NEW URIs (your collection items, for example)
basespace = rdflib.namespace.Namespace('http://example.org/')
##Enter the collection name formulated to also be a name for the linked data spreadsheet
collection = 'Spelman_Linked_Data'
##Enter path to triples csv (generated)
path = "/home/jj/Desktop/Spr_IP/triples.csv"
  

t_list=[]


##import triples csv
trips = pd.read_csv(path)
for index, rows in trips.iterrows():
    e_list=[]
    # Create list for the current row
    e_list.append(rows.S)
    e_list.append(rows.V)
    e_list.append(rows.O)
    t_list.append(e_list)



#query HIVE for each term
driver = webdriver.Firefox()
driver.get("https://hive2.cci.drexel.edu/search")
for group in t_list:
    hold_list=[]
    for item in group:
        print(item)
        if re.match("http", item):
            hold_list.append(item)
        else:
            #driver.implicitly_wait(10)
            WebDriverWait(driver, 10)
            driver.find_element(By.ID, "LCSH").click()
            driver.find_element(By.ID, "FASTgeo").click()
            driver.find_element(By.ID, "FASTpersonal").click()
            driver.find_element(By.ID, "USGS").click()
            driver.find_element(By.ID, 'searchterm').send_keys(item)
            driver.find_element(By.CSS_SELECTOR, '#search-button').send_keys(Keys.RETURN)
            driver.implicitly_wait(10)
            elements = driver.find_element(By.ID, "termlist")
            try:
                elements.find_element(By.CLASS_NAME, "usermsg")
                driver.implicitly_wait(2)
                item = re.sub("\s", "_", item)
                item1=basespace+str(item)
                hold_list.append(item1)
            except NoSuchElementException:
                driver.implicitly_wait(10)
                elements3 = elements.find_elements(By.CLASS_NAME, "linkedterm concept")
                for e in elements3:
                    matching=getLongest(item, e)
                    if len(matching) > 4:
                        link=driver.find_element(By.ID, "conceptview").click()
                        link=link.find_element(By.ID, "uri")
                        URI=link.text
                        hold_list.append(URI)
                    else:
                        driver.implicitly_wait(2)
                        item = re.sub("\s", "_", item)
                        item1=basespace+str(item)
                        hold_list.append(item1)
            
            driver.find_element(By.ID, 'searchterm').clear()
    print(hold_list)
    t_set.append(hold_list)


df = pd.DataFrame(t_set, columns = ['Subject', 'Predicate', 'Object'])
df.to_csv(str(collection)+'.csv', index=False)

driver.close()