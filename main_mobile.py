from selenium import webdriver
import insights

# Creating Instances
username = ''  # Username of account
password = ''  # Password of account


def main():
    print("Running...")
    # The below line of code will create an instance of Chrome using selenium
    # Logging in to selected profile...
    log = insights.mobileLogin(username, password)
    log.sign_in()


if __name__ == '__main__':
    main()
