import undetected_chromedriver as uc
from selenium.webdriver.common.by import By 
import csv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
import pyautogui
import time
import chrome

def click_and_hold(x, y, hold_time):
    """
    Click and hold the mouse at the specified (x, y) coordinates for a given amount of time.

    :param x: The x-coordinate for the mouse click.
    :param y: The y-coordinate for the mouse click.
    :param hold_time: The amount of time in seconds to hold the mouse button down.
    """
    pyautogui.moveTo(x, y)   # Move the mouse to the specified coordinates
    pyautogui.mouseDown()    # Press the mouse button down
    time.sleep(hold_time)    # Wait for the specified hold time
    pyautogui.mouseUp()      # Release the mouse button



options = webdriver.ChromeOptions() 
options.add_argument("--head")
driver = uc.Chrome(options=options)

town = 'Hornell'
state = 'NY'
property_type = 'type-single-family-home'

url_to_scrape = f'https://www.realtor.com/realestateandhomes-search/{town}_{state}/{property_type}'
time_delay = 20
# driver.get('https://www.realtor.com/')
driver.get(url_to_scrape)


try:
    print('Try')
    # Wait for the properties container to load
    properties_container = WebDriverWait(driver, time_delay).until(
        lambda driver: driver.find_elements(By.XPATH, "//*[starts-with(@class, 'PropertiesList_propertiesContainer')]")
    )
    # Find all the property elements within the container
    property_list = properties_container.find_elements(By.XPATH, "//*[starts-with(@class, 'BasePropertyCard_propertyCardWrap')]")
except:
    chrome.close_chrome()
    exit()
#     print('Except')
#     time.sleep(5)
#     click_and_hold(1400, 1600, 15)
#     # Repeat the same steps in the except block
#     properties_container = WebDriverWait(driver, time_delay).until(
#         lambda driver: driver.find_element(By.CLASS_NAME, "PropertiesList_propertiesContainer__Cud_i")
#     )
#     property_list = properties_container.find_elements(By.XPATH, "//*[starts-with(@class, 'BasePropertyCard_propertyCardWrap')]")


for element in property_list:
    print(element.text)
# Save results into a csv file

# Specify the file path to save the CSV file
csv_file_path = 'results.csv'

# Open the CSV file in write mode
with open(csv_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)

    # Write the header row
    writer.writerow(['Brokered by', 'Status', 'Type', 'Price', 'Size', 'Address'])

    # Write each property as a row in the CSV file
    for element in property_list:
        # Split the text by newline characters to get a list of lines
        lines = element.text.split('\n')
        lines = lines.strip()
        # Extract the necessary information from the lines
        brokered_by = lines[0]
        status = lines[1]
        type = lines[2]
        price = lines[3]
        size = lines[4]
        address = lines[7]
        # Write the information to the CSV file
        writer.writerow([brokered_by, status, type, price, size, address])

# Print a message to indicate that the results have been saved
print('Results saved to', csv_file_path)



driver.quit()