from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "Basket items is presented, but should not be"

    def should_be_text_empty_basket(self):
        text = 'Your basket is empty'
        paragraph = self.browser.find_element(*BasketPageLocators.TEXT_EMPTY_BASKET)
        assert text in paragraph.text, f'Page not content information about empty basket'
