

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions

urlLogin        = 'https://www.saucedemo.com/'
urlInventory    = 'https://www.saucedemo.com/inventory.html'
urlCart         = 'https://www.saucedemo.com/cart.html'


# Login on website
def login (driver, user, password):
    print ('Trying to Login to https://www.saucedemo.com/')
    driver.get(urlLogin)
    print ('Trying with user: {},  password: {}'.format(user, password))
    driver.find_element_by_id('user-name').send_keys(user)
    driver.find_element_by_id('password').send_keys(password)
    driver.find_element_by_id('login-button').click()
    assert urlInventory in driver.current_url
    print ('Login test passed')

# add items to shopping carts
def add_items(driver):
    items_in_cart = []
    elements = driver.find_elements_by_class_name('inventory_item')
    print('adding elements to the shopping carts:')
    for item in elements:
        item_name = item.find_element_by_class_name('inventory_item_name').text
        items_in_cart.append(item_name)
        item.find_element_by_class_name('btn_inventory').click()
        print('Added {} to shopping cart'.format(item_name))
    cart_element = driver.find_element_by_class_name('shopping_cart_badge')
    assert int(cart_element.text) == len(elements)
    print('Number of elements ok')
    driver.find_element_by_class_name('shopping_cart_link').click()
    assert urlCart in driver.current_url
    print ('element can be clicked')
    for item in driver.find_elements_by_class_name('inventory_item_name'):
        assert item.text in items_in_cart
    print ('Finished adding elements to shopping cart')


# remove all items from shopping cart
def remove_items(driver):
    driver.find_element_by_class_name('shopping_cart_link').click()
    assert urlCart in driver.current_url
    print("Number of items in shopping cart: {}".format(len(driver.find_elements_by_class_name('cart_item'))))
    for item in driver.find_elements_by_class_name('cart_item'):
        item_name = item.find_element_by_class_name('inventory_item_name').text
        item.find_element_by_class_name('cart_button').click()
        print('Removed {} from shopping cart'.format(item_name))
    assert len(driver.find_elements_by_class_name('cart_item')) == 0
    print('test passed: Cart empty.')


def uitests():
    options = ChromeOptions()
# uncomment this for run in Azure DevOps
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
#    driver = webdriver.Chrome()
    print("Browser started successfully.")
    print("starting now tests")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print(" Step 1: ------->>>> login user")
    login(driver, 'standard_user', 'secret_sauce')
    print(" Step 2: ------->>>> add items to cart")
    add_items(driver)
    print(" Step 3: ------->>>> remove items from cart")
    remove_items(driver)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("UI Tests completed.")
    driver.quit()


if __name__ == "__main__":
    uitests()





