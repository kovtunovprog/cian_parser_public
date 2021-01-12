def params_format(params_list_from_excel: list):
    """
    Transform user params to program data
    :param params_list_from_excel:
    :return:
    """
    params_list = []

    for params_excel in params_list_from_excel:

        params = {}
        rooms = []
        price_list = []
        for item, value in params_excel.items():
            if 'room' in str(item):
                room_num = str(item).split('_')[1]
                rooms.append(f'{room_num}:{value}')

        price_list.append(params_excel['minprice'])
        price_list.append(params_excel['maxprice'])

        params['location'] = params_excel['location']
        params['rooms'] = rooms
        params['price_list'] = price_list
        params['min_ago'] = params_excel['min_ago']
        params_list.append(params)

    return params_list
