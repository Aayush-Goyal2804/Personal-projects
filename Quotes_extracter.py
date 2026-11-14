import csv
import requests
from bs4 import BeautifulSoup
import time


def extract_data(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    scraped_quotes = []

    finding_quotes = soup.findAll("div", class_ = "quote")

    for quotes in finding_quotes:
        text = quotes.find("span", "text").text
        author = quotes.find("small" , "author").text

        dict_list = {"Quotes" : text, "Author" : author}

        scraped_quotes.append(dict_list)
        return scraped_quotes


def save_to_csv(data_list, filename):

    field = ["Quotes", "Author"]

    with open(filename , "w", newline = "", encoding = "utf-8-sig") as file:

        writer = csv.DictWriter(file, fieldnames=field)

        writer.writeheader()

        writer.writerows(data_list)

        print("Your CSV data has been saved successfully!!")



#Control Panel


if __name__ == "__main__":


    print("Starting scraper....")


    master_list = []

    for page in range(1,6):


        target_url = f"http://quotes.toscrape.com/page/{page}/"

        page_data = extract_data(target_url)

        master_list.extend(page_data)
        time.sleep(2)

    print(f"Finished scraping the data from the website, adding all the {len(master_list)} quotes in an EXCEL file.")
    save_to_csv(master_list, "My_professional_quotes.csv")
