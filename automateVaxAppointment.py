import smtplib
import ssl
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def main():
    driver = webdriver.Firefox()
    driver.get('https://www.impfportal-niedersachsen.de/portal/#/appointment/public')

    no_appointments = True
    while(no_appointments):
        driver.refresh()
        # Page 1: Datenschutzerklärung
        # Check Datenschutzerklärung
        checkbox = driver.find_element(By.ID, 'mat-checkbox-1')
        checkbox.click()
        # Click continue (Weiter)
        continue_data = driver.find_element_by_xpath('/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[2]/div/button[2]/span[1]')
        continue_data.click()

        # Page 2: Choose appointment type
        # "Einzeltermin" is already checked, therefore, continue
        continue_appointment_type = driver.find_element_by_xpath('/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[2]/div/button[2]')
        continue_appointment_type.click()

        # Page 3: put in date of birth for selection of vaccination priority group
        # please note: above 70 year olds are automatically checked
        input_date_of_birth = driver.find_element_by_xpath('//*[@id="mat-input-2"]')
        input_date_of_birth.send_keys('01.01.1950')
        # Group is automatically checked, therefore, continue
        continue_date_of_birth = driver.find_element_by_xpath('/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[2]/div/button[2]/span[1]')
        continue_date_of_birth.click()

        # Page 4: Stiko Indikation - information regarding the vaccinating rule framework in Germany
        continue_stiko = driver.find_element_by_xpath('/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[2]/div/button[2]')
        continue_stiko.click()

        # Page 5: specify post code and see if there free appointments
        # put post code (Postleitzahl)
        input_post_code = driver.find_element_by_xpath('//*[@id="mat-input-0"]')
        # post code for "Leer"
        input_post_code.send_keys('26789')
        # confirm search (Suchen)
        confirm_search = driver.find_element_by_xpath('/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[1]/div/div[1]/div[3]/div/button/span[1]')
        confirm_search.click()
        # appointments available/not available ((Keine) Termine verfügbar)
        get_appointmentstate = WebDriverWait(driver, timeout=5).until(lambda d: d.find_element_by_xpath('/html/body/my-app/div/div[3]/mat-sidenav-container/mat-sidenav-content/appointment-public-view/div/form/div[1]/div/div[1]/div[5]/div[2]/div/div'))
        no_appointments = (get_appointmentstate.text != 'IZ Leer 2\nAn der Schule 6\n26835 Hesel\n20 km entfernt\ncancel\nKeine Termine verfügbar')
        time.sleep(30)

    # the site has done something unexpected when the code reaches this section, hopefully, an appointment is available
    # -> send a mail to inform someone of the change in the site
    # kudos to https://realpython.com/python-send-email/
    port = 587  # For starttls
    smtp_server = "smtp.gmail.com"
    # dummy mail addresses
    sender_email = "sender@gmail.com"  # Enter your address
    receiver_email = "receiver@gmail.com"  # Enter receiver address
    password = input('Type your password and press enter:')
    message = """ Moin, \n bitte überprüfe den Browserinhalt von Firefox, etwas an der Seite hat sich geändert,
    vielleicht ist ein Termin frei."""

    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

if __name__ == '__main__':
    main()
