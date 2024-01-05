import selenium as se
import undetected_chromedriver as uc

driver = uc.Chrome(headless=True,use_subprocess=False)
driver.get('https://google.com')