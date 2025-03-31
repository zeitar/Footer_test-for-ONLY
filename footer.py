from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.firefox import GeckoDriverManager
import time

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

PAGES_TO_CHECK = [
    "https://only.digital/",
    "https://only.digital/projects",
    "https://only.digital/company",
    "https://only.digital/fields",
    "https://only.digital/job"
]


def check_footer_elements_on_page(url):
    try:
        driver.get(url)

        time.sleep(5)

        try:
            footer = driver.find_element(By.TAG_NAME, "footer")
            print("Футер найден.")
        except NoSuchElementException:
            print("Футер отсутствует!")
            return

        expected_elements = {
            "Кнопка НАЧАТЬ ПРОЕКТ ": "button.buttons:nth-child(1)",
            "BEHANCE": "div.Socials_socialsWrap__DPtp_:nth-child(3) > a:nth-child(1)",
            "DPROFILE": "div.Socials_socialsWrap__DPtp_:nth-child(3) > a:nth-child(2)",
            "TELEGRAM": "div.Socials_socialsWrap__DPtp_:nth-child(3) > a:nth-child(3)",
            "VKONTAKTE": "div.Socials_socialsWrap__DPtp_:nth-child(3) > a:nth-child(4)",
            "Почта": "a.text1:nth-child(1)",
            "Контакты": "div.ContactsLinks_contactLinks__vex86:nth-child(6) > a:nth-child(2)",
            "телеграм для связи": "div.Telegram_telegramWrap__USZkq:nth-child(4) > a:nth-child(2)",
            "Презентация PDF": "div.Documents_documentsWrap__iNfwU:nth-child(8) > div:nth-child(1) > a:nth-child(1)",
            "Презентация pitch": "div.Documents_documentsWrap__iNfwU:nth-child(8) > div:nth-child(1) > a:nth-child(2)",
            "AGE": "p.h4",
            "CREATIVE DIGITAL PRODUCTION": ".copyrightsBig > span:nth-child(1) > span:nth-child(1)",

        }

        for element_name, element_selector in expected_elements.items():
            try:
                if element_selector.startswith("text:"):
                    text_to_find = element_selector.split("text:")[1]
                    driver.find_element(By.XPATH, f"//*[contains(text(), '{text_to_find}')]")
                else:
                    driver.find_element(By.CSS_SELECTOR, element_selector)
                print(f"Элемент '{element_name}' найден в футере.")
            except NoSuchElementException:
                print(f"---------------Элемент '{element_name}' отсутствует в футере!")


    except Exception as e:
        print(f"Произошла ошибка при проверке страницы {url}: {e}")


def check_footer_on_multiple_pages():
    try:
        for page_url in PAGES_TO_CHECK:
            check_footer_elements_on_page(page_url)

    finally:
        print(f"=================================СТРАНИЦЫ ПРОВЕРЕНЫ=================================")
        driver.quit()


if __name__ == "__main__":
    check_footer_on_multiple_pages()