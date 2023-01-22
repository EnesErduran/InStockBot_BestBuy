from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


import undetected_chromedriver as uc

import info

# make sure this path is correct
PATH = "C:\Development\ChromeDriverForSelenium\chromedriver.exe"

#driver = webdriver.Chrome(PATH)
driver = uc.Chrome()

Link1 = "https://www.bestbuy.com/site/hogwarts-legacy-collectors-edition-playstation-5/6518482.p?skuId=6518482"
TestLink = "https://www.bestbuy.com/site/msi-nvidia-geforce-gtx-1660-super-ventus-xs-oc-6gb-gddr6-pci-express-3-0-graphics-card/6518174.p?skuId=6518174"

driver.get(Link1)

isComplete = False

while not isComplete:
    # find add to cart button
    try:

        atcBtn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".add-to-cart-button"))
        )
    except:
        driver.refresh()
        continue

    print("Add to cart button found")

    try:
        # add to cart
        atcBtn.click()

        # go to cart and begin checkout as guest
        driver.get("https://www.bestbuy.com/cart")

        checkoutBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div/button"))
        )
        checkoutBtn.click()
        print("Successfully added to cart - beginning check out")



        # fill in email and password
        emailField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-e"))
        )
        emailField.send_keys(info.email)

        pwField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "fld-p1"))
        )
        pwField.send_keys(info.password)


        # click sign in button
        signInBtn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/section/main/div[2]/div[1]/div/div/div/div/div/form/div[3]/button"))
        )
        signInBtn.click()
        print("Signing in")


        #Enter address and info

        firstNameField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[3]/div[1]/section/div[1]/div[2]/div/div/form/div[1]/div/input"))
        )
        firstNameField.send_keys(info.firstName)
        print("First Name Entered")

        lastNameField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "lastName"))
        )
        lastNameField.send_keys(info.lastName)
        print("Last Name Entered")


        addressField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "street"))
        )
        addressField.send_keys(info.address)
        print("Address Entered")


        cityField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "city"))
        )
        cityField.send_keys(info.city)
        print("City Entered")


        zipcodeField = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "zipcode"))
        )
        zipcodeField.send_keys(info.zipcode)
        print("Zipcode Entered")


        select = Select(driver.find_element(By.ID, "state"))
        select.select_by_value(info.state)
        print("State Entered")


        billingCheckBox = driver.find_element(By.ID, "save-for-billing-address-Map {}")
        billingCheckBox.click()
        print("Billing Checkbox Selected")

        applyButton = driver.find_element(By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[3]/div[1]/section/div[1]/div[2]/div/div/div[3]/button")
        applyButton.click()
        print("Applied all info")

        paymentInfoButton = WebDriverWait(driver, 10).until(
          EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[3]/div[1]/section/div[2]/section/div/div/button"))
        )
        paymentInfoButton.click()
        print("Navigating to payment info")

        cvvField = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.ID, "cvv"))
        )
        cvvField.send_keys(info.cvv)
        print("CVV entered")


        placeOrderButton = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div[2]/div/div[2]/div[1]/div[1]/main/div[3]/div[2]/div/section/div[3]/div/div[2]/button"))
        )
        placeOrderButton.click()
        print("Placing order")

        isComplete = True

    except:
        # make sure this link is the same as the link passed to driver.get() before looping
        driver.get(Link1)
        print("Error - restarting bot")
        continue

print("Order successfully placed")



