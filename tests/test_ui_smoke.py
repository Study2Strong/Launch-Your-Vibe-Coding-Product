# UI smoke test：點右側「本頁目錄」錨點導覽的第一個連結，確認網址 hash 與對應段落真的有跳過去。
# 需要先有一個跑起來的預覽伺服器可以連（見 .github/workflows/deploy.yml 的 test job）。

import os
from urllib.parse import unquote

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

BASE_URL = os.environ.get(
    "UI_TEST_BASE_URL",
    "http://localhost:4173/Launch-Your-Vibe-Coding-Product/",
)


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    # VitePress 只在 min-width:1280px 才顯示右側 aside 錨點導覽，
    # scrollbar 會吃掉幾 px viewport 寬度，故意抓大一點的視窗尺寸避免卡在邊界
    options.add_argument("--window-size=1440,900")
    drv = webdriver.Chrome(options=options)  # Selenium Manager 會自動抓對應版本的 chromedriver
    yield drv
    drv.quit()


def test_outline_nav_link_jumps_to_its_section(driver):
    driver.get(BASE_URL)

    # VitePress 是掛載後才用 JS 產生「本頁目錄」清單，SSR 的原始 HTML 裡是空的，要等它可以點擊
    first_link = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "a.outline-link"))
    )
    # 標題是中文，瀏覽器回傳的 href／URL 是 percent-encoded，id 屬性本身則是原文，兩邊要解碼後才比得起來
    encoded_target_id = first_link.get_attribute("href").rsplit("#", 1)[-1]
    target_id = unquote(encoded_target_id)

    first_link.click()

    WebDriverWait(driver, 5).until(EC.url_contains(f"#{encoded_target_id}"))
    heading = driver.find_element(By.ID, target_id)
    assert heading.is_displayed()
