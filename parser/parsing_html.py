from bs4 import BeautifulSoup


def get_page_data(html, min_ago, location):
    """
    Parsing html page and add data to info list
    :param location:
    :param html:
    :param min_ago:
    :return:
    """
    soup = BeautifulSoup(html, 'lxml')
    articles = soup.find_all('div', class_='_93444fe79c--card--2umme')
    info_list = []

    for article in articles:
        print('Parsing html iteration')

        name = article.find('div', class_='_93444fe79c--container--JdWD4').find('span').text
        print(name.text)
        price = article.find_all('div', class_='_93444fe79c--container--2h0AF')
        print(price.text)
        price1 = price[2].text
        print(price1.text)
        time_ago = article.find_all('div', class_='_93444fe79c--absolute--1BX9t')[0].text
        print(time_ago.text)

        if ('минуту назад' or 'минут назад') in str(time_ago):
            local_min_ago = time_ago[:2]
            print(local_min_ago)
            try:
                local_min_ago = int(local_min_ago)
            except Exception as err:
                print('Incorrect min in excel')
            if min_ago == local_min_ago or min_ago < local_min_ago+5 or min_ago > local_min_ago:
                info_list.append(f'{name}, {price1}, {time_ago}, {location}')
            if ('вчера' or 'сегодня') in str(time_ago):
                info_list.append(f'TESTING: {name}, {price1}, {time_ago}, {location}')

    return info_list
