from init import *
from unidecode import unidecode

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
class Eksi:
    def setup(self):
        self.setup_instance = Setup()
        while True:
            try:
                self.setup_instance.browser.get('https://eksisozluk.com/')
                logger.info("Starting browser setup")
                sleep(5)
                break
            except:
                self.setup_instance.browser.refresh()
        sleep(4)

        actions = ActionChains(self.setup_instance.browser)
        M = 3
        for _ in range(M):
            actions.send_keys(Keys.TAB).perform()
            sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

    def login(self):
        self.setup_instance.browser.get('https://eksisozluk.com/giris')
        sleep(4)

        while True:
            try:
                WebDriverWait(self.setup_instance.browser, 10).until(
                    EC.element_to_be_clickable((By.ID, 'username'))
                ).send_keys('zorluasim93@gmail.com')
                break
            except:
                pass

        password = self.setup_instance.browser.find_element(By.ID, 'password')
        password.send_keys('Haschmeth*1')
        sleep(5)

        actions = ActionChains(self.setup_instance.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

        try:
            WebDriverWait(self.setup_instance.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-navigation"]/ul/li[6]/a'))
            )
            print('Logged in.')
            logger.info("Logged in.")
        except:
            print('Failed to login.')
            logger.info("Failed to login.")
            Eksi.login(self)
        sleep(5)

    def surf(self):
        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/bugun')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/gundem')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/debe')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/sorunsal')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/takipentry')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/son')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/kenar')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/caylaklar/bugun')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/kanal/spor')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/kanal/iliskiler')
        sleep(4)

        self.setup_instance.browser.get('https://eksisozluk.com/basliklar/kanal/siyaset')
        sleep(4)

    def send_post(self):
        self.setup_instance.browser.get('https://eksisozluk.com/')
        sleep(4)

        main_title = WebDriverWait(self.setup_instance.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="title"]/a/span'))
        )
        main_title.click()
        sleep(4)

        get_url = self.setup_instance.browser.current_url
        sleep(4)

        self.setup_instance.browser.get(str(get_url)+'?p=3')
        sleep(4)

        copy = self.setup_instance.browser.find_element(By.XPATH, '//*[@id="entry-item"]/div[1]')
        copy = copy.text
        copy = unidecode(copy)
        sleep(4)

        paste = self.setup_instance.browser.find_element(By.XPATH, '//*[@id="editbox"]')
        paste.send_keys(copy)
        sleep(4)

        N = 2
        actions = ActionChains(self.setup_instance.browser)
        for _ in range(N):
            actions.send_keys(Keys.TAB).perform()
        sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(4)

        if("efendimiz" in self.setup_instance.browser.page_source):
            print('Your post was sent successfully.')
            logger.info("Your post was sent successfully.")
            sleep(180)
        else:
            print('An error occurred while sending the post.')
            logger.info("An error occurred while sending the post.")

    def fav(self):
        self.browser.get('https://eksisozluk.com/')
        sleep(4)

        main_title = WebDriverWait(self.setup_instance.browser, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="entry-item"]/footer/div[1]/span[2]/a[1]'))
        )
        main_title.click()
        sleep(4)
        print('The post has been added to favorites.')
        logger.info("The post has been added to favorites.")

    def close_browser(self):
        Setup.close_browser(self)

eks = Eksi()
eks.setup()
eks.login()

while(True):
    try:
        eks.send_post()
        eks.surf()
        eks.fav()
    except:
        print('No content has been found to copy. Retrying...')
        logger.info("No content has been found to copy. Retrying...")
        eks.close_browser()
        eks.setup()
        try:
            eks.login()
        except:
            sleep(1)