from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup
import requests
import chromedriver_binary

text="hello"
option = Options()                          # オプションを用意
option.add_argument('--headless')           # ヘッドレスモードの設定を付与
  # Chromeを準備(optionでヘッドレスモードにしている）
#ChromeDriverのパスを引数に指定しChromeを起動
driver = webdriver.Chrome('/usr/local/bin/chromedriver',options=option)
#指定したURLに遷移する
driver.get("https://translate.google.co.jp/?hl=ja&tab=TT&sl=en&tl=ja&op=translate")
#検索テキストボックスの要素をId属性名から取得
element = driver.find_element_by_class_name("er8xn")

#検索テキストボックスに文字列を入力
element.send_keys("hello")
time.sleep(3)

element1 = driver.find_element_by_class_name("VIiyi").text
driver.quit()
print(element1)
