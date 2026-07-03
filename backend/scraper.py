# scraper.py

import traceback

from products import PRODUCTS

from scraper_utils import (
    open_browser,
    search_product,
    open_first_product,
    get_product_name,
    get_overall_rating,
    open_all_reviews
)

from review_scraper import get_reviews
from csv_utils import save_reviews_to_csv

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():

    driver = open_browser()

    try:

        # Test first product only
        for product in PRODUCTS[:1]:

            print("\n" + "=" * 60)
            print(f"Searching for: {product}")
            print("=" * 60)

            # Search
            search_product(driver, product)

            # Open first product
            open_first_product(driver)

            # Product details
            product_name = get_product_name(driver)
            overall_rating = get_overall_rating(driver)

            print("\n==============================")
            print("PRODUCT DETAILS")
            print("==============================")
            print("Product Name :", product_name)
            print("Overall Rating :", overall_rating)

            # Open review page
            open_all_reviews(driver)

            print("\nOpened Review Page")

            # Wait for review page to load
            WebDriverWait(driver, 20).until(
                EC.presence_of_element_located(
                    (
                        By.TAG_NAME,
                        "body"
                    )
                )
            )

            # Save HTML (for debugging)
            with open("review_page.html", "w", encoding="utf-8") as f:
                f.write(driver.page_source)

            print("Saved review_page.html")

            # Get reviews
            reviews = get_reviews(driver)

            print("\n==============================")
            print("SCRAPED REVIEWS")
            print("==============================")

            for i, review in enumerate(reviews, start=1):

                print(f"\nReview {i}")
                print("Rating :", review["rating"])
                print("Title  :", review["title"])
                print("Review :", review["review"])
                print("-" * 60)

            print(f"\nTotal Reviews Scraped: {len(reviews)}")

            # Save CSV
            save_reviews_to_csv(
                reviews,
                product_name,
                overall_rating
            )

    except Exception:

        print("\n========== FULL ERROR ==========\n")
        traceback.print_exc()

    finally:

        input("\nPress Enter to close browser...")
        driver.quit()


if __name__ == "__main__":
    main()