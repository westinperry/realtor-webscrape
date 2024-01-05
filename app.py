import undetected_chromedriver as uc
from selenium.webdriver.common.by import By 
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


options = uc.ChromeOptions() 
my_user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"
options.add_argument(f"user-agent={my_user_agent}")
options.add_argument("--headless") 
driver = uc.Chrome(options=options) 

url_to_scrape = 'https://www.realtor.com/realestateandhomes-search/Rochester_NY'
time_delay = 10

driver.get(url_to_scrape)

try:
    property_list = WebDriverWait(driver, time_delay).until(
        EC.presence_of_element_located((By.CLASS_NAME, "PropertiesList_propertiesContainer__Cud_i"))
    )
except:
    print('Page took too long to load')
    exit()



print(property_list)
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