from sikulix4python import *

import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.firefox.options import Options

#browser = webdriver.Chrome()
browser = webdriver.Firefox()
#options = Options()
#options.headless = True
#browser = webdriver.Firefox(firefox_options=options)

scr = Screen()


def take_screenshot():
    file = "screen_{}.png".format(datetime.now()).replace(':', '_').replace(' ', '_')
    browser.save_screenshot(file)
    return file


def detect_image(image_file, click_on_it: bool = False):
    #match = scr.exists(image_file, 4.0)

    #aRegion = Region(0, 0, 300, 300)
    #match = aRegion.exists(image_file)
    match = scr.exists(image_file)

    # for match in matches:
    #     print(match.getIndex(), match.getScore(), match.toStringShort())

    if match:
        print("target={}".format(match.getTarget()))
        print("cv sees image {} on screen at {}".format(image_file, match))
        match.highlight()
        print("Found image={} on screen={}".format(image_file, take_screenshot()))
        if click_on_it:
            match.click()
    else:
        print("Can't find an image={} on screen, going to take a screenshot={}".format(image_file, take_screenshot()))
        sys.exit(-1)


def main():
    browser.get('https://www.google.com')
    delay = 5  # seconds
    try:
        myElem = WebDriverWait(browser, delay).until(EC.presence_of_element_located((By.NAME, 'q')))
        print("Page is ready!")
    except TimeoutException:
        print("Loading took too much time!")

    browser.set_window_size(1024, 768)
    search_box = browser.find_element_by_name('q')
    search_box.send_keys('Knock, Knock, Neo')
    search_box.submit()

    # CV scenarion
    reset()
    switchApp("Firefox")
    addImagePath("/Users/ruslan/workspace/cvtesting/python/testcase-00-google")
    hover()

    #detect_image("search_input_knock_neo.png")
    detect_image("googlelogo_color_92x30dp.png")

    time.sleep(3)  # Let the user actually see something!
    browser.quit()
    reset()


if __name__ == '__main__':
    main()
