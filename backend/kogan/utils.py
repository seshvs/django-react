import logging

import requests
from django.conf import settings
from rest_framework import status

log = logging.getLogger('KoganFactory')


class KoganFactory:

    @staticmethod
    def calc_cubic_weight(length, width, height):
        """ Method to calculate cubic weight.
            All input is recieved in cm's.
        """
        cubic_meters = (length/100) * (width/100) * (height / 100)
        return cubic_meters * settings.CUBIC_WEIGHT_CONVERSION_FACTOR

    @staticmethod
    def request_get(next_url):
        response = requests.get(settings.KOGAN_BASE_URL + next_url)
        if response.status_code != status.HTTP_200_OK:
            # raise exception if required
            return None
        return response

    @staticmethod
    def get_data():
        next_url = settings.KOGAN_FIRST_PAGE
        while next_url:
            log.info(next_url)

            response = KoganFactory.request_get(next_url)
            if response:
                next_url = response.json()['next']
                yield response.json()['objects']

    @staticmethod
    def get_data_for_a_category(category):
        next_data = KoganFactory.get_data()
        result = []

        try:
            data_list = next(next_data)

            while data_list:
                [result.append(i) if i['category'] == category else None for i in data_list]
                data_list = list(next(next_data))
        except StopIteration:
            pass

        return result

    @staticmethod
    def get_data_for_a_category(category):
        next_data = KoganFactory.get_data()
        result = []

        try:
            data_list = next(next_data)

            while data_list:
                [result.append(i) if i['category'] == category else None for i in data_list]
                data_list = list(next(next_data))
        except StopIteration:
            pass

        return result

    @staticmethod
    def get_average_weight_for_a_category(category):
        """ Not using get_data_for_a_category as we want to avoid extra for loop"""

        next_data = KoganFactory.get_data()
        result = []
        cubic_weight = 0
        try:
            data_list = next(next_data)

            while data_list:
                for i in data_list:
                    if i['category'] == category:
                        cubic_weight += KoganFactory.calc_cubic_weight(i['size']['length'],
                                                                       i['size']['width'],
                                                                       i['size']['height'])
                        result.append(i)
                data_list = list(next(next_data))
        except StopIteration:
            pass

        return cubic_weight/len(result) if len(result) else 0, result
