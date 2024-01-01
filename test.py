import os, datetime
from selenium import webdriver
# ドライバの初期化
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(options=options)

# ブラウザのウィンドウサイズを最大に設定
driver.maximize_window()

def fullpage_screenshot(driver, file):
    w = driver.execute_script("return document.body.parentNode.scrollWidth")
    h = driver.execute_script("return document.body.parentNode.scrollHeight")
    driver.set_window_size(w, h)
    driver.save_screenshot(file)

# 1つ目のページ（https://kujirahand.com）を開く
driver.get("https://kujirahand.com")
# 1つ目のページをキャプチャして保存
fullpage_screenshot(driver,"web1.png")

# 2つ目のページ（https://nadesi.com）を開く
driver.get("https://nadesi.com")
# 2つ目のページをキャプチャして保存
fullpage_screenshot(driver,"web2.png")

# ブラウザを閉じる
driver.quit()