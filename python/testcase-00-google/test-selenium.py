import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


#mkvirtualenv cvt -p python3
#cd ~/.virtualenvs/cvt/lib/python3.6/site-packages/
#ln -s /usr/local/lib/python3.6/site-packages/cv2/python-3.6/cv2.cpython-36m-darwin.so cv2.so
#workon cvt
#pip install numpy
#pip install imutils
#pip install selenium
#brew cask install chromedriver

#python test-selenium.py

def main():
  browser = webdriver.Chrome()
  browser.get('https://www.google.com')
  delay = 5 # seconds
  try:
    myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'q')))
    print("Page is ready!")
  except TimeoutException:
    print("Loading took too much time!")

  search_box = browser.find_element_by_name('q')
  search_box.send_keys('Knock, Knock, Neo')
  search_box.submit()
  time.sleep(2) # Let the user actually see something!
  browser.quit()


if __name__ == '__main__':
  main()
