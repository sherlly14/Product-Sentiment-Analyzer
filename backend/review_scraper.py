from bs4 import BeautifulSoup


def get_reviews(driver):

    soup = BeautifulSoup(driver.page_source, "html.parser")

    print("\nSearching for review titles...\n")

    titles = soup.find_all(string=True)

    count = 0

    for text in titles:

        text = text.strip()

        if len(text) > 8:

            print(text)
            print("-" * 50)

            count += 1

        if count == 100:
            break

    return []