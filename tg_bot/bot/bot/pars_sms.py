import time
import re
from bs4 import BeautifulSoup
from selenium import webdriver


def get_data_with_selenium(url):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36")

    try:
        driver = webdriver.Firefox(
            executable_path="C:\\Users\\ПАВЕЛ\\PycharmProjects\\Project\\tg_bot\\bot\\bot\\geckodriver.exe",
            options=options
        )
        time.sleep(4)
        driver.get(url=url)
        time.sleep(4)

        with open("index_selenium.html", "w", encoding="utf-8") as file:
            file.write(driver.page_source)

    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

    with open("index_selenium.html", encoding="utf-8") as file:
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    numbers_info = soup.find_all("div", class_="phone_body")
    info_text = 0

    for number in numbers_info:
        number_text = number.find(id="9046415872")
        if number_text is not None:
            info_text = number_text

    senders_info = info_text.find_all("div", class_="bodysms")

    for sender_info in senders_info:
        if str(sender_info.find("div", class_="smsnumber")).__contains__("KKT.NALOG"):
            return sender_info.find("div", class_="textsms").text


def main():
    url = "https://smska.us/"
    sms_text = get_data_with_selenium(url)
    pattern = r'[0-9]{4}'
    sms = re.findall(pattern, sms_text)
    return str(sms[0])


if __name__ == "__main__":
    main()
