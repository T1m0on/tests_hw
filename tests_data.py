def get_visits():
    geo_logs = [
        {'visit1': ['Москва', 'Россия']},
        {'visit2': ['Дели', 'Индия']},
        {'visit3': ['Владимир', 'Россия']},
        {'visit4': ['Лиссабон', 'Португалия']},
        {'visit5': ['Париж', 'Франция']},
        {'visit6': ['Лиссабон', 'Португалия']},
        {'visit7': ['Тула', 'Россия']},
        {'visit8': ['Тула', 'Россия']},
        {'visit9': ['Курск', 'Россия']},
        {'visit10': ['Архангельск', 'Россия']}
    ]
    new_list = []

    for visits in geo_logs:
        for value in visits.values():
            if 'Россия' in value:
                new_list.append(visits)

    geo_logs.clear()

    geo_logs += new_list

    return geo_logs


def get_unique_ids():
    ids = {'user1': [213, 213, 213, 15, 213],
           'user2': [54, 54, 119, 119, 119],
           'user3': [213, 98, 98, 35]}

    ids_set = set()
    for i in ids.values():
        ids_set.update(i)
    return list(ids_set)


def make_dict_from_list():
    random_list = ['2018-01-01', 'yandex', 'cpc', 100]

    new_dict = random_list.pop()

    for i in random_list[::-1]:
        new_dict = {i: new_dict}

    return new_dict
