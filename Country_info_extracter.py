import csv
import requests
from bs4 import BeautifulSoup


def extracting_data(url):

    response = requests.get(url, verify = False)

    soup = BeautifulSoup(response.text, "html.parser")

    fetching_leads = soup.findAll("div", class_ = "col-md-4 country")

    country_list = []

    for leads in fetching_leads:

        extracting_country_name = leads.find("h3", class_ = "country-name").text

        extracting_capital = leads.find("div", class_ = "country-info")

        capital_name = extracting_capital.find("span", class_ = "country-capital").text

        extracting_population = leads.find("div", class_ = "country-info")
        population = extracting_population.find("span", class_ = "country-population").text

        final_population = int(population)

        if final_population > 50000000:

            country_list.append({"Name" : extracting_country_name, "Capital city" : capital_name, "Population": final_population})
    return country_list


def save_to_csv(data_list, filename):

    fields = ["Name", "Capital city", "Population"]

    with open(filename, "w", newline = "") as file:

        writer = csv.DictWriter(file, fieldnames=fields)

        writer.writeheader()
        writer.writerows(data_list)



if __name__ == "__main__":

    print("Starting scraper")

    target_url = "https://www.scrapethissite.com/pages/simple/"

    data_extracted = extracting_data(target_url)

    print("The data is extracted succesfully, now saving it to a CSV file")

    save_to_csv(data_extracted, "Country.csv")
