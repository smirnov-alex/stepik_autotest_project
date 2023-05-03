from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def click_to_add_to_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_BASKET)
        button_add_to_basket.click()

    def should_be_item_name(self):
        item_name = self.browser.find_element(*ProductPageLocators.ITEM_NAME)
        messages_name = self.browser.find_element(*ProductPageLocators.MESSAGES_NAME)
        assert item_name.text == messages_name.text, f'Name of item not match with name in basket'

    def should_be_item_price(self):
        item_price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE)
        messages_price = self.browser.find_element(*ProductPageLocators.MESSAGES_PRICE)
        assert item_price.text == messages_price.text, f'Price of item not match with price in basket'
