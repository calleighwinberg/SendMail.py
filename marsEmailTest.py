import unittest

from marsEmail import *
class MyTestCase(unittest.TestCase):
    def test_getPhotoOfDay(self):

        #test that non-string format for date will present an error
        msg = getPhotoOfDay(2023-12-12)
        self.assertEqual('{"code":400,"msg":"time data \'1999\' does not match format \'%Y-%m-%d\'","service_version":"v1"}\n', msg)  # add assertion here

        #test that improper format for date will present an error
        msg = getPhotoOfDay('2023/12/12')
        self.assertEqual('{"code":400,"msg":"time data \'2023/12/12\' does not match format \'%Y-%m-%d\'","service_version":"v1"}\n', msg)  # add assertion here


if __name__ == '__main__':
    unittest.main()
