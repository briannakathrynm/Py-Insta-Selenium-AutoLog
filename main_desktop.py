from selenium import webdriver
from AutoLog import login
import pandas as pd
from AutoLog import scrape

# Creating Instances
driver = 0
username = ''  # Username of account
password = ''  # Password of account
backup_code = None  # Backup Code of account if 2Fact
post_count = 2


def main():
    global driver
    print("Running...")
    # The below line of code will create an instance of Chrome using selenium
    driver = webdriver.Chrome("C://Users/Brianna's HP17/Desktop/chromedriver.exe")
    # Logging in to selected profile...
    log = login.Login(driver, username, password, backup_code, post_count)
    log.sign_in()
    # Scraping selected profile...
    print("Fetching URLS...")
    instagram_urls = scrape.recent_post_links(driver, username, post_count)
    print("Fetching Details...")
    instagram_details = [scrape.insta_details(driver, url) for url in instagram_urls]
    print("Compiling into Dataframe...")
    details = pd.DataFrame(instagram_details)
    print(details.head())
    # Exports all Details to a CSV file at the following path:
    print("Exporting to CSV...")
    details.to_csv("C://Users/Brianna's HP17/Desktop/details_csv.csv")


if __name__ == '__main__':
    main()
