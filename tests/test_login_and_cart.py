import allure

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.epic("Web自动化")
@allure.feature("购物车流程")
@allure.story("登录并加购")
@allure.title("标准用户登录后加入商品到购物车")
def test_login_and_add_to_cart(driver):
    with allure.step("打开 SauceDemo 并登录"):
        login_page = LoginPage(driver).open()
        login_page.login("standard_user", "secret_sauce")
        login_page.wait_login_success()

    with allure.step("进入商品列表并加购"):
        inventory_page = InventoryPage(driver)
        inventory_page.add_first_item_to_cart()

    with allure.step("验证购物车角标"):
        assert inventory_page.get_cart_badge_text() == "1"