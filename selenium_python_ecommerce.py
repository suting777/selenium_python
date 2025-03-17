from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Login
username = driver.find_element(By.ID,"user-name")
password = driver.find_element(By.ID,"password")
username.send_keys("standard_user")
password.send_keys("secret_sauce")

login = driver.find_element(By.ID,"login-button")
login.click()

print("Login Successful!")

# Add one item to cart

driver.maximize_window()

# add_to_cart = driver.find_element(By.XPATH,"//button[text()='Add to cart']")
# add_to_cart.click()
# print("One product added to cart!")

# add multiple-item to cart
add_items = driver.find_elements(By.XPATH,"//button[text()='Add to cart']")
for add_item in add_items[:3]:
    add_item.click()

print("Items added to cart!")

# Go to cart page
cart = driver.find_element(By.CLASS_NAME,"shopping_cart_link")
cart.click()

print("cart page")

# Click checkout
check_out = driver.find_element(By.ID,"checkout")
check_out.click()
print("check out page")

# Fill in checkout information

firstname = driver.find_element(By.ID,"first-name")
lastname = driver.find_element(By.ID,"last-name")
postcode = driver.find_element(By.ID,"postal-code")

firstname.send_keys("tester")
lastname.send_keys("King")
postcode.send_keys("SW1 8ER")

continue_button = driver.find_element(By.ID,"continue")
continue_button.click()

finish_button = driver.find_element(By.ID,"finish")
finish_button.click()

# Verify checkout success message

check_message = driver.find_element(By.CLASS_NAME,"complete-header")

# .text : Extracts the text content from that element.
check_message = check_message.text

assert check_message == "Thank you for your order!","Check out failed"
print("Checked out")

# if you want to keep website open insted [driver.quit()], use [input("Press Enter to exit...")]
driver.quit()