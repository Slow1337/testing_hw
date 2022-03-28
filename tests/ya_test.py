import unittest
import requests
import ya

class YaTester(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()
    
    def test_make_directory(self):
        test_pools = {
            200: ['Red', 'Green', 'Blue'],
            404: ['Black', 'Yellow', 'White']
        }
        for code, pool in test_pools.items():
            if code == 200:
                for entry in pool:
                    with self.subTest(entry=entry, code=code):
                      response = ya.ya_instance.make_directory(entry)
                      response_code = response.status_code
                      check_if_exists = ya.ya_instance.get_directory_info(entry)
                      check_response_code = check_if_exists.status_code
                      self.assertEqual(response_code, 201)
                      # не очень красиво с 201, но из-за разницы ответов в методах решил
                      # что пересобирать словарь и переписывать код не стоит
                      # может неправ
                      self.assertEqual(check_response_code, code)
            elif code == 404:
                for entry in pool:
                    with self.subTest(entry=entry, code=code):
                        response = ya.ya_instance.get_directory_info(entry)
                        response_code = response.status_code
                        self.assertEqual(response_code, code)