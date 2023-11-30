"""
    流程操作
"""

from selenium import webdriver
import pytest
from page import Page
import time

@pytest.fixture(scope="class")
# 打开浏览器，访问登录页面
def init():
    driver = webdriver.Chrome()
    driver.maximize_window()
    url = "https://www.feishu.cn/"
    driver.get(url)
    yield driver
    driver.quit()

@pytest.mark.usefixtures("init")
class TestZiJie:

    # 流程操作步骤
    def test_zijie(self, init):
        pg = Page(init)
        pg.click_off()
        pg.click_login_button()
        pg.click_login_type_button()
        pg.input_username()
        time.sleep(2)
        pg.click_checkbox()
        pg.click_next_button()
        pg.input_password()
        pg.click_next_button2()
        # 等待20s手动输入验证码
        time.sleep(20)

        pg.click_icon_button()
        pg.click_message_button()
        pg.click_AddressBook_button()
        pg.click_add_button()
        pg.input_mobile()
        pg.click_search_button()
        pg.click_SearchListItem_button()
        pg.click_usercard_button()
        pg.click_send_button()
        # 等联系人通过好友申请
        time.sleep(20)

        pg.click_info_button()
        pg.click_tester2_button()
        pg.input_info()
        print(1234)

