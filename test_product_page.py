import time

# from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
# import pytest


# @pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
# "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
# ])
# def test_guest_can_add_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7"
#     main_page = ProductPage(browser, link)
#     main_page.go_to_site()
#     main_page.pressing_buttons()
#     main_page.mathematical_equation()
#     main_page.checking_if_an_item_is_in_the_cart()
#     main_page.product_name()
#     main_page.the_price_of_the_product()
#
#
# @pytest.mark.xfail
# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     main_page = ProductPage(browser, link)
#     main_page.go_to_site()
#     main_page.pressing_buttons()
#     main_page.should_not_be_success_message()
#
#
# def test_guest_cant_see_success_message(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     main_page = ProductPage(browser, link)
#     main_page.go_to_site()
#     main_page.should_not_be_success_message()
#
#
# @pytest.mark.xfail
# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     main_page = ProductPage(browser, link)
#     main_page.go_to_site()
#     main_page.pressing_buttons()
#     main_page.no_success_message_with()
#
# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     main_page = ProductPage(browser, link)
#     main_page.go_to_site()
#     main_page.should_be_login_link()

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    main_page = LoginPage(browser, link)
    main_page.go_to_site()
    main_page.go_to_login_page()
    main_page.should_be_login_link()
    time.sleep(2)