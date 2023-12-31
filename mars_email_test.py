import unittest

from mars_email import *
class MyTestCase(unittest.TestCase):
    def test_get_photo_of_day(self):

        #test that non-string format for date will present an error
        msg = get_photo_of_day(2023-12-12)
        self.assertEqual('{"code":400,"msg":"time data \'1999\' does not match format \'%Y-%m-%d\'","service_version":"v1"}\n', msg)

        #test that improper format for date will present an error
        msg = get_photo_of_day('2023/12/12')
        self.assertEqual('{"code":400,"msg":"time data \'2023/12/12\' does not match format \'%Y-%m-%d\'","service_version":"v1"}\n', msg)

        #test that four items are returned when a valid date is entered
        lst = get_photo_of_day('2023-12-11')
        self.assertEqual(4, len(lst))

    def test_get_mars_photo(self):

        #test that a valid sol day returns a url containing the call for that sol
        self.assertTrue('http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02300/'
                        in get_mars_photo('2300'))

        #test that the url generated when given a sol that has no photos will generate a url for a picture from
        #the next sol day that has available photos
        #2344 is a sol when there were no pictures. The next sol that has pictures in 2346
        self.assertTrue('http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02346/'
                        in get_mars_photo('2344'))
        self.assertTrue('http://mars.jpl.nasa.gov/msl-raw-images/proj/msl/redops/ods/surface/sol/02346/'
                        in get_mars_photo('2345'))

        #test that entering any number greater than 4000 will always return a url for a photo from sol day 1000
        self.assertTrue('http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/' in get_mars_photo('4001'))
        self.assertTrue('http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/' in get_mars_photo('100001'))


    def test_send_email(self):

        #test that given valid parameters, a 202 status code is returned
        self.assertEqual(202, send_email('mars@calleighwinberg.courses', 'calleighwinberg@gmail.com',
                                         'http://mars.jpl.nasa.gov/msl-raw-images/msss/01000/mcam/1000MR0044630030503563C00_DXXX.jpg', '1000'))

        #test that sending from an unverified sender will return an error
        self.assertEqual('error', send_email('x@gmail.com', 'y@gmail.com',
                                         'z', '1000'))

        # test that sending from an unverified sender will return an error
        self.assertEqual('error', send_email('x@gmail.com', 'y@gmail.com',
                                             'z', '1000'))


if __name__ == '__main__':
    unittest.main()
