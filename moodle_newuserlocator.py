import datetime
import moodle_locators as locators
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
s = Service(executable_path='chromedriver')

driver = webdriver.Chrome(service=s)

# Fixture methods
def setup():
    #maximizing the screen
    driver.maximize_window()
    #wait for the browser to load up
    driver.implicitly_wait(30)
    #navigate to the moodle app website
    driver.get(locators.moodle_url)
    #checking that the url is addy is correct and that we are seeing the correct title
    if driver.current_url == locators.moodle_url and driver.title == 'SQA Server 1':
        print(f'We are at the correct homepage---{driver.current_url}')
        print(f'We are seeing the title---"SQA Server 1"')
    else:
        print("We are not at the correct homepage. Please check your code")
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'--------------')
        print(f'The test was completed at : {datetime.datetime.now()}')
        driver.close()
        driver.quit()

def log_in():
    if driver.current_url == locators.moodle_url:
        driver.find_element(By.LINK_TEXT,'Log in').click()
        if driver.current_url == locators.moodle_login_url:
            driver.find_element(By.ID,'username').send_keys(locators.moodle_username)
            sleep(.25)
            driver.find_element(By.ID,'password').send_keys(locators.moodle_password)
            sleep(.25)
            driver.find_element(By.ID,'loginbtn').click()
            if driver.title == 'Dashboard' and driver.current_url==locators.moodle_dashboard_url:
                assert driver.current_url==locators.moodle_dashboard_url
                print('Login is successful and the Dashboard is present')
            else:
                print('Dashboard is not present, try again. D\oh')

def log_out():
    driver.find_element(By.CLASS_NAME, 'usermenu').click()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT,'Log out').click()
    sleep(0.25)
    if driver.current_url==locators.moodle_url:
       print(f'Log out successfully at:{datetime.datetime.now()}')

def create_new_user():
    driver.find_element(By.LINK_TEXT, "Site administration").click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Users')
    driver.find_element(By.LINK_TEXT, 'Users').click()
    sleep(0.25)
    assert driver.find_element(By.LINK_TEXT, 'Add a new user').is_displayed()
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Add a new user').click()
    sleep(0.25)
    # send fake data to create a new user
    driver.find_element(By.ID, 'id_username').send_keys(locators.new_username)
    sleep(0.25)
    driver.find_element(By.LINK_TEXT, 'Click to enter text').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_newpassword').send_keys(locators.new_password)
    sleep(0.25)
    driver.find_element(By.ID, 'id_preference_auth_forcepasswordchange').click()
    sleep(0.25)
    driver.find_element(By.ID, 'id_firstname').send_keys(locators.first_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_lastname').send_keys(locators.last_name)
    sleep(0.25)
    driver.find_element(By.ID, 'id_email').send_keys(locators.email)
    sleep(0.25)
    Select(driver.find_element(By.ID,'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    driver.find_element(By.ID, 'id_submitbutton').click()

    #Select(driver.find_element(By.ID,'id_maildisplay')).select_by_visible_text('Allow everyone to see my email address')
    sleep(0.25)
    #breakpoint()

# Calling the methods
#open the chrome browser
setup()

log_in()

create_new_user()

log_out()

tearDown()
