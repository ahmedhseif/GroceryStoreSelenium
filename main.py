from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

EMAIL = "YOUR EMAIL"
PASS = "YOUR PASSWORD"
chrome_driver_path = "C:\\Development\\chromedriver.exe"


class Grocery:

    def check_list(self):
        the_list = open('new_groceries.txt').read().splitlines()
        print(the_list)
        answer = input("Is that what you would like to order? Type 'yes' to continue\n").lower()
        if answer == 'yes':
            recent_list = open('recent.txt').read().splitlines()
            compare = []
            for item in recent_list:
                if item not in the_list:
                    compare.append(item)
            print(compare)
            recent = input("These are the items you purhased last time that you didn't include this time, would you like to add any to the list? Type 'yes' to add and type 'no' to continue\n").lower()
            if recent == 'yes':
                adding = True
                while adding:
                    print("Type 'done' to continue.")
                    add_item = input("Add new item: ")
                    if add_item == 'done':
                        adding = False
                    else:
                        the_list.append(add_item)
                final_list = the_list
                print('Your final list is: ', final_list)
                with open('recent.txt', 'w') as f:
                    for item in final_list:
                        f.write(f'{item}\n')
                sleep(5)
            elif recent == 'no':
                final_list = the_list
                print('Your final list is: ', final_list)
                with open('recent.txt', 'w') as f:
                    for item in final_list:
                        f.write(f'{item}\n')
                sleep(5)
            else:
                print('Invalid answer. Please try again.')
                exit()
        else:
            print('Please edit the txt file and try again.')
        return the_list

    def login(self, driver_path):
        service = ChromeService(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get("https://www.jumia.com.eg/customer/account/login/")
        self.driver.maximize_window()
        enter_email = self.driver.find_element(By.ID, 'fi-email')
        enter_email.send_keys(EMAIL)
        enter_pass = self.driver.find_element(By.ID, 'fi-password')
        enter_pass.send_keys(PASS)
        sleep(2)
        enter_pass.send_keys(Keys.ENTER)
        sleep(5)

    def shop(self, the_list):
        for item in the_list:
            search_bar = self.driver.find_element(By.ID, 'fi-q')
            search_bar.send_keys(item)
            search_bar.send_keys(Keys.ENTER)
            sleep(2)
            first_choice = self.driver.find_element(By.CLASS_NAME, 'core')
            first_choice.click()
            sleep(2)
            add_cart = self.driver.find_element(By.CLASS_NAME, 'add')
            add_cart.click()
            sleep(2)
        process_cart = self.driver.find_element(By.ID, 'ci')
        process_cart.click()
        process_checkout = self.driver.find_element(By.XPATH, '//*[@id="jm"]/main/div/div[2]/div/article/div[3]/a')
        process_checkout.click()
        print('Please fill in your credit card info')


bot = Grocery()
the_list = bot.check_list()
bot.login(chrome_driver_path)
bot.shop(the_list)

