import types
import requests

from django.conf import settings
from django.test import TestCase
from rest_framework import status

from ..utils import KoganFactory


class UtilTestCases(TestCase):

    @classmethod
    def setUpClass(cls):
        """ Class level constructor"""
        print("Test Util classes and methods ")
        pass

    @classmethod
    def tearDownClass(cls):
        """ Class level destructor"""
        pass

    def setUp(self):
        """ Test case level constructor"""
        pass

    def tearDown(self):
        """ Test case level destructor """
        pass

    def test_kogan_factory_calc_function(self):
        """ Test logic """
        cubic_weight = KoganFactory.calc_cubic_weight(40, 20, 30)
        self.assertEqual(int(cubic_weight), 6)  # Sample data should have 6 kgs

    def test_request(self):
        response = KoganFactory.request_get(settings.KOGAN_FIRST_PAGE)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.json())  # should be able to decode in json
        self.assertTrue(response.json()['next'] and response.json()['objects'])  # next should be in response

    def test_generator(self):
        response = KoganFactory.get_data()
        self.assertTrue(isinstance(response, types.GeneratorType))

    def test_get_data_from_category(self):
        def validate_category(data_list, category):
            for item in data_list:
                self.assertEqual(item['category'], category)

        category_list = ['Batteries', 'Air Conditioners']
        for i in category_list:
            validate_category(KoganFactory.get_data_for_a_category(i), i)

    def test_average_cubic_weight(self):
        category_list = ['Batteries', 'Air Conditioners']
        for category in category_list:
            data_list = KoganFactory.get_data_for_a_category(category)
            result = []
            cubic_weight = 0

            for i in data_list:
                if i['category'] == category:
                    cubic_weight += KoganFactory.calc_cubic_weight(i['size']['length'],
                                                                   i['size']['width'],
                                                                   i['size']['height'])
                    result.append(i)

            cubic_weight = cubic_weight / len(result) if len(result) else 0
            cubic_weight_from_obj, _ = KoganFactory.get_average_weight_for_a_category(category)
            self.assertEqual(cubic_weight, cubic_weight_from_obj)

    def test_endpoint(self):
        def get_url(catg):
            return settings.BASE_URL+'/kogan/category/'+catg+'/average_cubic_weight'

        category_list = ['Batteries', 'Air Conditioners']

        for category in category_list:
            response = requests.get(get_url(category))
            self.assertTrue(response.status_code==status.HTTP_200_OK)

            avg_cubic_weight = response.json()['avg_cubic_weight']
            cubic_weight_from_obj, _ = KoganFactory.get_average_weight_for_a_category(category)
            self.assertEqual(avg_cubic_weight, cubic_weight_from_obj)
