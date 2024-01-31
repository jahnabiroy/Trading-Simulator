from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main(ticker, exchange):
    url = f"https://www.google.com/finance/quote/{ticker}:{exchange}"
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    prefs = {"profile.default_content_setting_values.notifications": 2}
    options.add_experimental_option("prefs", prefs)
    options.add_argument("window-size=1920x1080")
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    driver.get(url)
    wait = WebDriverWait(driver, 10)
    svg_element = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".ushogf svg"))
    )
    svg_outer_html = svg_element.get_attribute("outerHTML")
    driver.quit()
    return svg_outer_html
