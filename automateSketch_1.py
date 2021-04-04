from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Firefox()
    driver.get("https://www.impfportal-niedersachsen.de/portal/#/appointment/public")

    # Check Datenschutzerklärung
    checkbox = driver.find_element(By.ID, "mat-checkbox-1")
    checkbox.click()


if __name__ == '__main__':
    main()
