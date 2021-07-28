import time
import json
from selenium import webdriver 
from selenium import common
from selenium.webdriver.common import keys
from selenium.webdriver.common.keys import Keys 
from webdriver_manager.chrome import ChromeDriverManager
 
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()  
loopTest = 1
x = '''{
        "username"  : "sigendats",
        "email"     : "", 
        "pass"      : "Ipb117158", 
        "text"      : "tweet ini dikirim dari automated test dengan python selenium",
        "image"     : "C:/Users/ASUS S14/Documents/New folder/selenium.jpg"
    }'''

y = json.loads(x)
 
def signIn():
    driver.get("https://www.twitter.com/login")
    time.sleep(1)
 
    usernameInput=driver.find_element_by_name("session[username_or_email]")
    passwordInput=driver.find_element_by_name("session[password]")

    try:
        usernameInput.send_keys(y["username"])
        time.sleep(1)
        passwordInput.send_keys(y["pass"])
        time.sleep(1)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(1)
        
        postTweets()

    except Exception as err:
        print ("this error: ", err) 
    
def postTweets():
    body = y["text"]
    
    for x in range(loopTest):
        tweet = driver.find_element_by_css_selector("br[data-text='true']")
        tweet.send_keys(y["text"])

        try:
            file = driver.find_element_by_xpath("//input[@data-testid='fileInput']")
            file.send_keys(y["image"])
        except common.exceptions.NoSuchElementException:
            time.sleep(1)
            file = driver.find_element_by_xpath("//input[@data-testid='fileInput']")
            file.send_keys(y["image"])

        button = driver.find_element_by_css_selector("div[data-testid='tweetButtonInline']")
        button.click()

        time.sleep(5)


    time.sleep(1)
    print('\n================================')
    print('texting telah selesai dan sukses')
    time.sleep(2)
    driver.close() 

if __name__=="__main__":  
    signIn() 
