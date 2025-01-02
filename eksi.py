from init import *
from unidecode import unidecode

class Eksi:
    def setup(self):
        logging.info("Setting up the browser...")
        Setup.init(self)
        while True:
            try:
                self.browser.get('https://eksisozluk.com/')
                sleep(5)
                break
            except Exception as e:
                logging.error(f"Error during setup: {str(e)}")
                self.browser.refresh()
        sleep(4)

        actions = ActionChains(self.browser)
        M = 3
        for _ in range(M):
            actions.send_keys(Keys.TAB).perform()
            sleep(2)
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

    def login(self):
        logging.info("Attempting to log in...")
        self.browser.get('https://eksisozluk.com/giris')
        sleep(4)

        while True:
            try:
                WebDriverWait(self.browser, 10).until(
                    EC.element_to_be_clickable((By.ID, 'username'))
                ).send_keys('zorluasim93@gmail.com')
                break
            except Exception as e:
                logging.error(f"Error during login: {str(e)}")

        password = self.browser.find_element(By.ID, 'password')
        password.send_keys('Haschmeth*1')
        sleep(5)

        actions = ActionChains(self.browser)
        actions.send_keys(Keys.RETURN).perform()
        sleep(5)

        try:
            WebDriverWait(self.browser, 10).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="top-navigation"]/ul/li[6]/a'))
            )
            logging.info("Logged in successfully.")
        except Exception as e:
            logging.error(f"Failed to log in: {str(e)}")
            self.login()
        sleep(5)

    def surf(self):
        self.browser.get('https://eksisozluk.com/basliklar/bugun')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/gundem')
        sleep(4)

        self.browser.get('https://eksisozluk.com/debe')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/sorunsal')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/takipentry')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/son')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/kenar')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/caylaklar/bugun')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/kanal/spor')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/kanal/iliskiler')
        sleep(4)

        self.browser.get('https://eksisozluk.com/basliklar/kanal/siyaset')
        sleep(4)

    def send_post(self):
        logging.info("Sending a post...")
        self.browser.get('https://eksisozluk.com/')
        sleep(4)

        try:
            main_title = WebDriverWait(self.browser, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="title"]/a/span'))
            )
            main_title.click()
            sleep(4)

            get_url = self.browser.current_url
            sleep(4)

            self.browser.get(str(get_url) + '?p=3')
            sleep(4)

            copy = self.browser.find_element(By.XPATH, '//*[@id="entry-item"]/div[1]').text
            copy = unidecode(copy)
            sleep(4)

            paste = self.browser.find_element(By.XPATH, '//*[@id="editbox"]')
            paste.send_keys(copy)
            sleep(4)

            actions = ActionChains(self.browser)
            actions.send_keys(Keys.RETURN).perform()
            sleep(4)

            if "efendimiz" in self.browser.page_source:
                logging.info("Your post was sent successfully.")
            else:
                logging.error("An error occurred while sending the post.")
        except Exception as e:
            logging.error(f"Error during sending post: {str(e)}")

    def fav(self):
        self.browser.get('https://eksisozluk.com/')
        sleep(4)

        main_title = WebDriverWait(self.browser, 100).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="entry-item"]/footer/div[1]/span[2]/a[1]'))
        )
        main_title.click()
        sleep(4)
        print('The post has been added to favorites.')
        logging.info('The post has been added to favorites.')

    def close_browser(self):
        logging.info("Closing the browser...")
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
        logging.info('No content has been found to copy. Retrying...')
        eks.close_browser()
        eks.setup()
        try:
            eks.login()
        except:
            sleep(1)