from selenium import webdriver
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Firefox()
    driver.get("https://www.impfportal-niedersachsen.de/portal/#/appointment/public")

    # Page 1: Datenschutzerklärung
    # Check Datenschutzerklärung
    checkbox = driver.find_element(By.ID, "mat-checkbox-1")
    checkbox.click()
    # Click Weiter
    continue_data = driver.find_element_by_xpath("/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[2]/div/button[2]/span[1]")
    continue_data.click()

    # Page 2: Choose appointment type
    # "Einzeltermin" is already checked, therefore, continue
    continue_appointment_type = driver.find_element_by_xpath("/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[2]/div/button[2]")
    continue_appointment_type.click()




if __name__ == '__main__':
    main()
