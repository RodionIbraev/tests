import requests
import unittest


class RestAPITest(unittest.TestCase):

    def test_create_folder(self):
        request_url = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = {'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'OAuth AQAAAAAWIRZ6AADLW4WPeyRunU23rhRXMetuykM'}
        new_folder = 'music'

        # Success 201
        response_1 = requests.put(request_url, headers=headers, params={'path': new_folder})
        self.assertEqual(response_1.status_code, 201)

        # DiskPathPointsToExistentDirectoryError 409
        response_2 = requests.put(request_url, headers=headers, params={'path': new_folder})
        self.assertEqual(response_2.status_code, 409)

        # FieldValidationError 400
        response_3 = requests.put(request_url, headers=headers, params={'path': []})
        self.assertEqual(response_3.status_code, 400)

        # UnauthorizedError 401
        del headers['Authorization']
        response_4 = requests.put(request_url, headers=headers, params={'path': new_folder})
        self.assertEqual(response_4.status_code, 401)


