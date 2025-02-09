
# author: Bartlomiej "furas" Burek (https://blog.furas.pl)
# date: 2021.11.03
#
# title: Multiple scraping: problem in the code. What am I doing wrong?
# url: https://stackoverflow.com/questions/69817631/multiple-scraping-problem-in-the-code-what-am-i-doing-wrong/69818379#69818379

# [Multiple scraping: problem in the code. What am I doing wrong?](https://stackoverflow.com/questions/69817631/multiple-scraping-problem-in-the-code-what-am-i-doing-wrong/69818379#69818379)

import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox()
driver.get("https://www.diretta.it/calcio/svezia/allsvenskan/risultati/")
driver.implicitly_wait(12)
#driver.minimize_window()

wait = WebDriverWait(driver, 10)

try:
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[id='event__more event__more--static']"))).click()
except Exception as ex:
    print('EX:', ex)

all_rows = driver.find_elements(By.CSS_SELECTOR, "div[class^='event__round'],div[class^='event__match']")

results = []

current_round = '?'

for row in all_rows:
    classes = row.get_attribute('class')
    #print(classes)
    
    if 'event__round' in classes:
        current_round = row.text
    else:
        date = row.find_element(By.CSS_SELECTOR, "[class^='event__time']")
        team_home = row.find_element(By.CSS_SELECTOR, "[class^='event__participant event__participant--home']")            
        team_away = row.find_element(By.CSS_SELECTOR, "[class^='event__participant event__participant--away']")
        score_home = row.find_element(By.CSS_SELECTOR, "[class^='event__score event__score--home']")
        score_away = row.find_element(By.CSS_SELECTOR, "[class^='event__score event__score--away']")   
    
        row = [current_round, date.text, team_home.text, team_away.text, score_home.text, score_away.text]
        results.append(row)
        print(row)
    
