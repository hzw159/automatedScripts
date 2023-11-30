"""
    日志
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
import os
import time
# import pyautogui


class Basepage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    # 等待元素可见
    def wait_ele_visible(self, locator, timeout=10, poll_frequency=0.5):
        """
        :param locator:元素定位，例：(By.XPATH, '//input[@class="login-username"]')
        :param page_action:页面动作，在进行什么操作
        :param timeout:超时时间
        :param poll_frequency:轮循时间
        """
        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
        except:
            raise
        else:
            end = time.time()

    # 等待元素存在
    def wait_page_contains_element(self, locator, timeout=20, poll_frequency=0.5):

        try:
            start = time.time()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.presence_of_element_located(locator))
        except:
            raise
        else:
            end = time.time()

    # 先等待 再查找
    def get_element(self, locator, timeout=20, poll_frequency=0.5, wait=None):
        # 等待元素存在或者可见
        if wait:
            self.wait_page_contains_element(locator,  timeout, poll_frequency)
        else:
            self.wait_ele_visible(locator, timeout, poll_frequency)

        try:
            ele = self.driver.find_element(*locator)
        except:
            raise
        else:
            return ele

    # 点击操作
    def click_element(self, locator,  timeout=20, poll_frequency=0.5, wait=None):
        # 等待 - 查找
        ele = self.get_element(locator,  timeout, poll_frequency, wait)
        # 点击
        try:
            ele.click()
        except:
            raise

    # 输入操作
    def input_text(self, locator, value, timeout=20, poll_frequency=0.5):
        # 等待 - 查找
        ele = self.get_element(locator, timeout, poll_frequency)
        try:
            ele.clear()
            ele.send_keys(value)
        except:
            raise

    # 回车操作
    def keys_enter(self, locator, timeout=20, poll_frequency=0.5):
        # 等待 - 查找
        ele = self.get_element(locator, timeout, poll_frequency)
        try:
            ele.send_keys(Keys.ENTER)
        except:
            raise

    # 获取文本操作
    def get_text(self, locator, timeout=20, poll_frequency=0.5):
        ele = self.get_element(locator, timeout, poll_frequency)
        try:
            return ele.text
        except:
            raise

    # 获取元素属性操作
    def get_attribute(self, locator, value, timeout=20, poll_frequency=0.5):
        ele = self.get_element(locator, timeout, poll_frequency)
        try:
            return ele.get_attribute(value)
        except:
            raise

    # 刷新页面
    def refresh_page(self):
        try:
            self.driver.refresh()
        except:
            raise

    # 页面回退
    def back_page(self):
        try:
            self.driver.back()
        except:
            raise

    # 窗口跳转
    def switch_window(self):
        # 等待一下
        time.sleep(1)
        try:
            # 获取所有的句柄
            wins = self.driver.window_handles
            self.driver.switch_to.window(wins[-1])
        except:
            raise

    # 实现按钮存在但无法点击问题，移动到目标元素处
    def notClick_exist(self, locator, wait):
        element = self.get_element(locator, wait=wait)
        ActionChains(self.driver).click(element).perform()


if __name__ == '__main__':
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.action_chains import ActionChains

    driver = webdriver.Chrome()
    base = Basepage(driver)
    driver.get('https://www.baidu.com')

    a = (By.XPATH, '//input[@id="kw"]')
    b = (By.XPATH, '//input[@id="su"]')

    base.input_text(a, "输入框", "python")
    time.sleep(5)
    base.refresh_page("刷新页面")
    base.input_text(a, "输入框", "python")
    time.sleep(5)
    base.click_element(b, "点击按钮")
    base.back_page("回退页面")
    # c = (By.XPATH, '//div[@class="wbrjf67"]')
    # base.click_element(c, "打开新窗口")
    # time.sleep(5)
    # base.switch_window()
    # d = (By.XPATH, '//a[text()="快速安装"]')
    # base.get_element(d, "确定窗口跳转是否成功！")
    # base.click_element(d, "点击操作")
    # time.sleep(5)
    driver.quit()


