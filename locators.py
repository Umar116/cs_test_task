from selenium.webdriver.common.by import By


sign_in_by_steam = (By.XPATH, "(//button[@type=\'button\'])[2]")
login_field = (By.CSS_SELECTOR, 'input[type="text"]')
password_field = (By.CSS_SELECTOR, 'input[type="password"]')
login_submit = (By.CSS_SELECTOR, 'button[type="submit"]')


trade_page_link = (By.XPATH, '//*[@id="layout-page-header"]/div[1]/div/div[2]/a[1]/span')
sort_list_button = (By.ID, 'downshift-1-toggle-button')
user_max_prise_sort_item = (By.ID, 'downshift-1-item-1')
user_min_prise = (By.ID, 'downshift-1-item-2')
user_max_float = (By.ID, 'downshift-1-item-3')
user_min_float = (By.ID, 'downshift-1-item-4')
trade_items_price = (By.CLASS_NAME, "price_price__2aKac")
float_price = (By.CLASS_NAME, "BaseCard_description__31IqW")


banner1 = (By.CSS_SELECTOR, ".ModalCloseIcon-module_container__FZOJt > path:nth-child(1)")
banner2 = (By.CSS_SELECTOR, 'button[aria-label="close"]')
accept_cooke_banner = (By.XPATH, '//span[text()= "Accept all"]')
