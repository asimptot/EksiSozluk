from time import sleep
import warnings, os
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

class Setup:
    def __init__(self):
        options = Options()
        options.add_argument('--headless')
        options.add_argument("--window-position=-2400,-2400")
        options.add_argument("--incognito")
        options.add_argument("--disable-gpu")
        options.add_argument(
            "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-popup-blocking")
        options.add_argument("--disable-infobars")
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")

        chromedriver_path = os.path.join(os.path.dirname(__file__), 'chromedriver')  # init.py ile aynı dizinde
        if not os.path.exists(chromedriver_path):
            raise FileNotFoundError(f"Chromedriver not found at {chromedriver_path}")

        # ChromeDriver'ı başlat
        service = Service(chromedriver_path)
        self.browser = webdriver.Chrome(service=service, options=options)

        # WebDriver algılamalarını engelle
        self.browser.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
            "source": """
                Object.defineProperty(navigator, 'webdriver', {get: () => undefined})
            """
        })
        self.browser.execute_cdp_cmd("Network.setUserAgentOverride", {
            "userAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        })

    def close_browser(self):
        self.browser.quit()
