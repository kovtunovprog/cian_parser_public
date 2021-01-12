def get_excel_params(file_excel):
    """
    Take params from excel file
    :param file_excel:
    :return: params dict
    """

    params_dicts_list = []
    first_column = 'Лист1'
    worksheet = file_excel[first_column]
    excel_row_len = len(list(worksheet.rows))

    item = 0
    while item != excel_row_len - 1:
        item += 1
        param_vars = []
        for cell in list(worksheet.rows)[item]:  # Вывод строки
            if cell.value is None:
                break
            param_vars.append(cell.value)
        try:
            params_excel = {
                'room_1': param_vars[0],
                'room_2': param_vars[1],
                'room_3': param_vars[2],
                'room_4': param_vars[3],
                'room_5': param_vars[4],
                'room_6': param_vars[5],
                'maxprice': param_vars[6],
                'minprice': param_vars[7],
                'min_ago': param_vars[8],
                'location': param_vars[9].replace(u'\xa0', u' ')
            }
        except IndexError:
            print('IndexError: you have to update excel file')
            return None
        params_dicts_list.append(params_excel)

    return params_dicts_list
