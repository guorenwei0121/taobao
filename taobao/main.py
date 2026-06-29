# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import time
import random
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def crawl_taobao():
    # 初始化浏览器驱动
    driver = webdriver.Chrome()
    driver.get('https://www.taobao.com')
    driver.maximize_window()

    # 随机等待2 - 3秒模拟用户反应时间
    time.sleep(random.uniform(2, 3))

    # 找到搜索框并输入关键词“方便面”
    search_box = driver.find_element(By.ID, 'q')
    search_box.send_keys('方便面')
    time.sleep(random.uniform(1, 2))

    # 找到搜索按钮并点击
    search_button = driver.find_element(By.CSS_SELECTOR, '.btn-search')
    search_button.click()
    time.sleep(random.uniform(3, 5))

    product_list = []
    for page in range(1, 21):
        print(f"正在爬取第 {page} 页")
        # 随机滚动页面
        scroll_height = random.randint(500, 1500)
        driver.execute_script(f"window.scrollTo(0, {scroll_height});")
        time.sleep(random.uniform(2, 3))

        # 获取商品信息
        products = driver.find_elements(By.CSS_SELECTOR, '.m-itemlist.items.item')
        for product in products:
            try:
                # 模拟鼠标悬停操作
                actions = ActionChains(driver)
                actions.move_to_element(product).perform()
                time.sleep(random.uniform(0.5, 1))

                # 商品标题
                title = product.find_element(By.CSS_SELECTOR, '.Title--title--wJY8TeA').text
                # 商品价格
                price_int = product.find_element(By.CSS_SELECTOR, '.Price--priceInt--BYXeCOI').text
                price_float = product.find_element(By.CSS_SELECTOR, '.Price--priceFloat--rI_BYho').text
                price = price_int + (0.01 * price_float)
                # 发货地址
                procity = product.find_element(By.CSS_SELECTOR, '.Price--procity--Na1DQVe').text

                product_dict = {
                    '标题': title,
                    '价格': price,
                    '发货地址': procity
                }
                product_list.append(product_dict)
            except Exception as e:
                print(f'获取商品信息出错: {e}')

        if page < 20:
            # 尝试查找下一页按钮
            try:
                next_page = driver.find_element(By.CSS_SELECTOR, '.next-btn')
                if 'disabled' not in next_page.get_attribute('class'):
                    # 模拟点击前的随机等待
                    time.sleep(random.uniform(1, 2))
                    next_page.click()
                    time.sleep(random.uniform(3, 5))
                else:
                    break
            except Exception:
                break

    # 关闭浏览器
    driver.quit()

    return product_list


def save_to_excel(data):
    df = pd.DataFrame(data)
    df.to_excel('淘宝方便面商品数据.xlsx', index=False)


if __name__ == "__main__":
    product_data = crawl_taobao()
    save_to_excel(product_data)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
