# scraper_utils.py

import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager


# ----------------------------
# Open Browser
# ----------------------------
def open_browser():

    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

    driver.get("https://www.flipkart.com")

    return driver


# ----------------------------
# Search Product
# ----------------------------
def search_product(driver, product):

    wait = WebDriverWait(driver, 20)

    search_box = wait.until(
        EC.presence_of_element_located((By.NAME, "q"))
    )

    search_box.clear()
    search_box.send_keys(product)
    search_box.send_keys(Keys.ENTER)

    time.sleep(5)


# ----------------------------
# Open First Product
# ----------------------------
def open_first_product(driver):

    wait = WebDriverWait(driver, 20)

    wait.until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "a"))
    )

    links = driver.find_elements(By.TAG_NAME, "a")

    product_url = None

    for link in links:

        href = link.get_attribute("href")

        if not href:
            continue

        # Skip advertisement links
        if "ctx=" in href:
            continue

        if "nnc=" in href:
            continue

        # Real product links only
        if "/p/" in href and "pid=" in href:

            product_url = href
            break

    if product_url is None:
        raise Exception("Product not found.")

    print("Opening:", product_url)

    driver.get(product_url)

    time.sleep(5)


# ----------------------------
# Product Name
# ----------------------------
def get_product_name(driver):

    try:

        wait = WebDriverWait(driver, 10)

        element = wait.until(
            EC.presence_of_element_located((By.TAG_NAME, "h1"))
        )

        return element.text.strip()

    except:

        return "Not Found"


# ----------------------------
# Overall Rating
# ----------------------------
def get_overall_rating(driver):

    xpaths = [

        "//div[contains(@class,'XQDdHH')]",

        "//div[contains(@class,'_3LWZlK')]",

        "//div[@dir='auto' and contains(text(),'.')]"

    ]

    for xpath in xpaths:

        try:

            element = driver.find_element(By.XPATH, xpath)

            text = element.text.strip()

            try:

                value = float(text)

                if value <= 5:

                    return text

            except:

                pass

        except:

            pass

    return "Not Found"


# ----------------------------
# Open All Reviews Page
# ----------------------------
def open_all_reviews(driver):

    print("\nSearching for review link...\n")

    links = driver.find_elements(By.TAG_NAME, "a")

    for link in links:

        href = link.get_attribute("href")

        if href and "product-reviews" in href:

            print("Found Review Page:")
            print(href)

            driver.get(href)

            time.sleep(5)

            return

    raise Exception("Review page not found.")


# ----------------------------
# Scroll Reviews
# ----------------------------
def scroll_reviews(driver, times=5):

    for _ in range(times):

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);"
        )

        time.sleep(2)