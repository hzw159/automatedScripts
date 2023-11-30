"""
    页面操作
"""

import time

from page_locs import PageLocs as loc
from basepage import Basepage


class Page(Basepage):
    # 点击弹窗关闭按钮
    def click_off(self):
        self.click_element(loc.off_button_loc)

    # 点击登录按钮
    def click_login_button(self):
        self.click_element(loc.login_button_loc)
        time.sleep(5)

    # 切换登录方式
    def click_login_type_button(self):
        self.click_element(loc.login_type_button_loc)

    # 输入账号
    def input_username(self):
        self.input_text(loc.username_loc, loc.username)

    # 点击同意单选框
    def click_checkbox(self):
        self.click_element(loc.checkbox_loc)

    # 点击下一步按钮
    def click_next_button(self):
        self.click_element(loc.next_button_loc)

    # 输入密码
    def input_password(self):
        self.input_text(loc.password_loc, loc.password)

    # 点击下一步按钮
    def click_next_button2(self):
        self.click_element(loc.next_button2_loc)

    # 点击9个点按钮
    def click_icon_button(self):
        self.click_element(loc.icon_button_loc)

    # 点击消息按钮
    def click_message_button(self):
        self.click_element(loc.message_button_loc)
        # 切换窗口
        self.switch_window()

    # 点击通讯录按钮
    def click_AddressBook_button(self):
        self.click_element(loc.AddressBook_button_loc)

    # 点击添加联系人按钮
    def click_add_button(self):
        self.click_element(loc.add_button_loc)

    # 输入联系人手机号
    def input_mobile(self):
        self.input_text(loc.mobile_loc, loc.mobile)

    # 进行搜索
    def click_search_button(self):
        self.click_element(loc.search_button_loc)

    # 点击添加按钮
    def click_SearchListItem_button(self):
        self.click_element(loc.SearchListItem_button_loc)

    # 点击添加联系人按钮
    def click_usercard_button(self):
        self.click_element(loc.usercard_button_loc)

    # 点击发送按钮
    def click_send_button(self):
        self.click_element(loc.send_button_loc)
        # 刷新页面
        self.refresh_page()

    # 点击消息按钮
    def click_info_button(self):
        self.click_element(loc.info_button_loc)

    # 点击添加联系人按钮
    def click_tester2_button(self):
        self.click_element(loc.tester2_button_loc)

    # 输入发送的消息
    def input_info(self):
        self.input_text(loc.editor_input_loc, loc.info)
        # 回车操作
        self.keys_enter(loc.editor_loc)