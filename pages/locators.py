from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTRATION_FORM = (By.CSS_SELECTOR, '#register_form')


class ProductPageLocators:
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    ITEM_NAME = (By.CSS_SELECTOR, "h1")
    ITEM_PRICE = (By.CSS_SELECTOR, "p.price_color")
    MESSAGES_NAME = (By.CSS_SELECTOR, "#messages strong")
    MESSAGES_PRICE = (By.CSS_SELECTOR, "#messages div div p:nth-child(1) strong")

