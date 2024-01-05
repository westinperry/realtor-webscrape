import undetected_chromedriver as uc
from selenium.webdriver.common.by import By 
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver


options = webdriver.ChromeOptions() 
options.add_argument("--head")
driver = uc.Chrome(options=options)

url_to_scrape = 'https://www.realtor.com/realestateandhomes-search/Canisteo_NY'
time_delay = 10

driver.get(url_to_scrape)



try:
    property_list = WebDriverWait(driver, time_delay).until(
        EC.presence_of_element_located((By.CLASS_NAME, "PropertiesList_propertiesContainer__Cud_i"))
    )
except Exception as e:
    print(e)
    exit()



print(property_list.text)
# Save results into a csv file

# Specify the file path to save the CSV file
csv_file_path = 'results.csv'

# Open the CSV file in write mode
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Property Name', 'Address', 'Price'])

    # Write each property as a row in the CSV file
    for property in property_list:
        writer.writerow([property['name'], property['address'], property['price']])

# Print a message to indicate that the results have been saved
print('Results saved to', csv_file_path)



driver.quit()