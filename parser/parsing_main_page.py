import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def selenium_parsing_main_page(web_driver, rooms_list: list, price_list: list, location: str):
    """
    Parsing main page and order apartaments by params
    :param web_driver:
    :param rooms_list:
    :param price_list:
    :param location:
    :return:
    """
    web_driver.get('https://www.cian.ru')
    apart_type_button = web_driver.find_element_by_class_name('_025a50318d--button--2oXjq')
    apart_type_button.click()
    time.sleep(3)
    apart_type_new = web_driver.find_element_by_class_name('_025a50318d--box--VTgYk')
    web_driver.execute_script("arguments[0].click();", apart_type_new)

    rooms_buttons = web_driver.find_element(By.XPATH, '//button[text()="1, 2 комн."]')
    web_driver.execute_script("arguments[0].click();", rooms_buttons)
    # rooms_buttons.click()
    rooms_buttons_list = web_driver.find_element_by_class_name('_025a50318d--list--3ybsu')\
        .find_elements_by_tag_name('li')

    for room in rooms_list:
        current_index = rooms_list.index(room)
        room_data = room.split(':')
        if (current_index == 0 or current_index == 1) and room_data[1] == '1':
            continue
        if room_data[1] == '1' or ((current_index == 0 or current_index == 1) and room_data[1] == '0'):
            time.sleep(2)
            rooms_buttons_list[current_index].click()

    time.sleep(3)

    price_button = web_driver.find_element_by_xpath('//button[text()="Цена"]')
    price_button.click()

    price_inputs = web_driver.find_elements_by_class_name('_025a50318d--input--1lsp8')
    price_inputs[0].send_keys(price_list[0])
    price_inputs[1].send_keys(price_list[1])

    search_buttons = web_driver.find_elements_by_class_name('_025a50318d--button--1sI1I')
    search_buttons[1].click()
    time.sleep(4)

    search_input = web_driver.find_element_by_id('geo-suggest-input')
    search_input.send_keys(location)
    time.sleep(15)
    adress_list = web_driver.find_elements_by_class_name('geosuggest_widget-item-hS8HtB9s')
    try:
        adress_list[0].click()
        time.sleep(6)
    except Exception as err:
        print(err)

    try:
        show_buttons = web_driver.find_elements_by_class_name('_3Lpyrczb3U4kA1TV')
        show_buttons[0].click()
    except Exception as err:
        print(err)
        try:
            search_button = web_driver.find_element_by_xpath('//span[text()="Найти"]')
            search_button.click()
        except Exception as err:
            print(err)
    time.sleep(15)

    return web_driver.page_source
