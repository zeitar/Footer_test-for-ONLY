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
            "Проекты": "a.Header_linkItem__AqdrQ:nth-child(1)",
            "Кампания": "a.Header_linkItem__AqdrQ:nth-child(2)",
            "Направления": "a.Header_linkItem__AqdrQ:nth-child(3)",
            "Карьера": "a.Header_linkItem__AqdrQ:nth-child(4)",
            "Блог": "a.Header_linkItem__AqdrQ:nth-child(5)",
            "Контакты": "a.Header_linkItem__AqdrQ:nth-child(6)"
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
                print(f"Элемент '{element_name}' отсутствует в футере!")


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