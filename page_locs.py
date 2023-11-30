"""
    页面元素
"""
from selenium.webdriver.common.by import By


class PageLocs:
    # 弹窗关闭按钮
    off_button_loc = (By.XPATH, '//div[@class="hc_Popup-content"]/div/div/div')

    # 登录按钮
    login_button_loc = (By.XPATH, '//a[text()="登录"]')

    # 登录方式切换按钮
    login_type_button_loc = (By.XPATH, '//span[@class="universe-icon switch-icon"]')

    # 输入用户名
    username_loc = (By.XPATH, '//input[@class="mobile-input-phone"]')
    username = 18170662885

    # 同意单选框
    # checkbox_loc = (By.XPATH, '//input[@class="ud__checkbox__input"]')
    checkbox_loc = (By.XPATH, '//span[text()="我已阅读并同意 "]')

    # 下一步按钮
    next_button_loc = (By.XPATH, '//button[text()="下一步"]')

    # 输入密码
    password_loc = (By.XPATH, '(//input[@class="ud__native-input"])[2]')
    password = "hxx@1234"

    # 下一步按钮
    next_button2_loc = (By.XPATH, '(//button[text()="下一步"])[2]')

    # 9个点按钮
    icon_button_loc = (By.XPATH, '//span[@class="universe-icon _pp-product-icon"]')

    # 消息按钮
    message_button_loc = (By.XPATH, '//span[text()="消息"]')

    # 通讯录按钮
    AddressBook_button_loc = (By.XPATH, '(//div[@class="larkc-badge"])[5]')

    # 添加联系人按钮
    add_button_loc = (By.XPATH, '//button[text()="添加联系人"]')

    # 输入联系人手机号
    mobile_loc = (By.XPATH, '//input[@class="larkc-searchInput--input"]')
    mobile = 18179699465

    # 搜索联系人
    search_button_loc = (By.XPATH, '//div[@class="ExternalContactsSearch_empty"]')

    # 添加按钮
    SearchListItem_button_loc = (By.XPATH, '//button[text()="添加"]')

    # 添加联系人按钮
    usercard_button_loc = (By.XPATH, '(//button[text()="添加联系人"])[2]')

    # 发送按钮
    send_button_loc = (By.XPATH, '//button[text()="发送"]')

    # 消息按钮
    info_button_loc = (By.XPATH, '(//div[@class="larkc-badge"])[1]')

    # 选中联系人，打开聊天框
    tester2_button_loc = (By.XPATH, '//p[text()="tester2"]')

    # 输入消息
    editor_input_loc = (By.XPATH, '//div[@class="lark-editor-container"]//p')
    info = "123456789"

    # 发送消息
    editor_loc = (By.XPATH, '//div[@class="lark-editor-container"]')




