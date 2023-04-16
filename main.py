import unittest
from unittest import TestCase
from tests_data import get_visits, get_unique_ids, make_dict_from_list
from ya_disc import YaUploader

ya = YaUploader(token='123')

class Tests(TestCase):
    def test_get_visits(self):
        current_value = get_visits()
        expected_value =[{'visit1': ['Москва', 'Россия']}, {'visit3': ['Владимир', 'Россия']},
                         {'visit7': ['Тула', 'Россия']},
                         {'visit8': ['Тула', 'Россия']}, {'visit9': ['Курск', 'Россия']},
                         {'visit10': ['Архангельск', 'Россия']}]
        self.assertEqual(current_value, expected_value)

    def test_unique_ids(self):
        current_value = get_unique_ids()
        expected_value = [98, 35, 15, 213, 54, 119]
        self.assertEqual(current_value, expected_value)

    def test_make_dict_from_list(self):
        current_value = make_dict_from_list()
        expected_value = {'2018-01-01': {'yandex': {'cpc': 100}}}
        self.assertEqual(current_value, expected_value)


    def test_create_folder(self):
        resp_code = 201
        res = ya.create_folder()
        self.assertEqual(res, resp_code)

    def test_check_folder(self):
        resp_code = 200
        res = ya.check_folder()
        self.assertEqual(res, resp_code)

    @unittest.expectedFailure
    def test_is_folder_exist(self):
        resp_code = 201
        res = ya.create_folder()
        self.assertEqual(res, resp_code, 'Такая папка уже существует. status code 409')

    @unittest.expectedFailure
    def test_invalid_data(self):
        resp_code = 201
        res = ya.failure_function()
        self.assertEqual(res, resp_code, 'Некорректные данные. status code 400')
