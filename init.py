from time import sleep
import warnings
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

        options.binary_location = "/opt/render/project/.render/chrome/opt/google/chrome/chromedriver"

        # Driver yolunu manuel ayarlamak yerine ChromeDriverManager ile kur
        service = Service(ChromeDriverManager().install())

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
