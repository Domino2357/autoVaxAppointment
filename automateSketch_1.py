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

    # Page 3: put in date of birth for selection of vaccination priority group
    # please note: above 70 year olds are automatically checked
    input_date_of_birth = driver.find_element_by_xpath('//*[@id="mat-input-2"]')
    input_date_of_birth.send_keys("01.01.1950")
    # Group is automatically checked, therefore, continue
    continue_date_of_birth = driver.find_element_by_xpath("/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[2]/div/button[2]/span[1]")
    continue_date_of_birth.click()

    # Page 4: Stiko Indikation - information regarding the vaccinating rule framework in Germany
    continue_stiko = driver.find_element_by_xpath("/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[2]/div/button[2]")

    
if __name__ == '__main__':
    main()
