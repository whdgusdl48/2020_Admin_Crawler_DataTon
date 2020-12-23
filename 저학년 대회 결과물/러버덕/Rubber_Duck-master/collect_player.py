import csv_handler
from selenium.webdriver.common.by import By
import chaeminuim

# CSV Initialization
Month = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6, 'July': 7, 'August': 8,
         'September': 9, 'October': 10, 'November': 11, 'December': 12}
csv_columns = ['Name', 'Month', 'Player']
dict_data = []
csv_file = "data/player_of_month_100.csv"

# Driver Initialization
driver = chaeminuim.getDriver(Debug=True)
URL = r'https://steamcharts.com/top/p.'

# open all of List
for page in range(1, 4 + 1):
    driver.get(URL + str(page))
    for index in range(1, 25 + 1):
        chaeminuim.click(By.XPATH, '//*[@id="top-games"]/tbody/tr[' + str(index) + ']/td[2]/a', driver, ctrl=True)

for i in range(1, 100 + 1):
    # switch to game status page
    driver.switch_to.window(driver.window_handles[-1])
    chaeminuim.wait(By.XPATH, '//*[@id="content-wrapper"]/div[6]/table', driver)

    # get game_name & table
    Name = driver.find_element_by_xpath('//*[@id="app-title"]/a').text
    table = driver.find_element_by_xpath('//*[@id="content-wrapper"]/div[6]/table')
    # split table and append to dict_data
    for tr in table.find_elements_by_tag_name("tr"):
        tokens = str(tr.text).split()
        if tokens[0] == 'Month': continue
        if tokens[0] == 'Last':
            dict_data.append({'Name': Name, 'Month': 12, 'Player': int(float(tokens[3].replace(',', '')))})
            continue
        if tokens[1] != '2020': break
        dict_data.append({'Name': Name, 'Month': Month[tokens[0]], 'Player': int(float(tokens[2].replace(',', '')))})
    # close status page
    driver.close()

# save dict_data as csv type
csv_handler.save(csv_file, csv_columns, dict_data)
