from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys
import pyautogui


options = Options()
options.add_argument("user-data-dir=~/.config/google-chrome")
browser = webdriver.Chrome('./chromedriver', chrome_options=options)

browser.get('https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw')

# thumbnail is the id for a video on HOME of YT CHANNEL
clickOnVideo = browser.find_element_by_id('thumbnail')
clickOnVideo.click()
sleep(5)

while True:
    '''Scrolling to the comment section'''
    # sections is the id of the comment section
    browser.execute_script("window.scrollTo(0, 400)")
    sleep(10)


    '''Commmenting on the video'''
    comment = 'Sub2Pewds -> https://www.youtube.com/channel/UC-lHJZR3Gqxm24_Vd_AJ5Yw'
    pyautogui.click(311, 588, 2)
    pyautogui.typewrite(comment)

    submitButton = browser.find_element_by_id('submit-button')
    submitButton.click()
    sleep(5)

    #  ANOTHER VIDEOOOO LOOP AFTER THISS!

    '''Scrolling to the another video'''
    pyautogui.click(1027, 267, 1)
    sleep(5)


browser.close()
