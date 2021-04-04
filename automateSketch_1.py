from selenium import webdriver


def main():
    driver = webdriver.Firefox()
    driver.get("https://www.impfportal-niedersachsen.de/portal/#/appointment/public")


if __name__ == '__main__':
    main()
