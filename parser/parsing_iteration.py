from openpyxl import load_workbook
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from loader import wb
from parser.format_execl_params import params_format
from parser.parsing_html import get_page_data
from parser.parsing_main_page import selenium_parsing_main_page
from utils.get_exel_params import get_excel_params


def parsing_iteration():
    """
    parsing iteration
    :return:
    """
    print('Get excel params')
    params_excel_list = get_excel_params(wb)
    print('Format excel params')
    params_list = params_format(params_excel_list)
    print('Start selenium')

    main_info_list = []
    chrome_options = Options()
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    web_driver = webdriver.Chrome(chrome_options=chrome_options)
    try:
        for params in params_list:
            min_ago = params['min_ago']
            print('selenium parsing iteration')
            html = selenium_parsing_main_page(web_driver, params['rooms'], params['price_list'],
                                              params['location'])
            info_list = get_page_data(html, min_ago, params['location'])
            print(info_list)
            main_info_list.append(info_list)
    except:
        web_driver.close()
        return None
    web_driver.close()
    print('MAIN INFO LIST' + str(main_info_list))
    return main_info_list
