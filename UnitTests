import unittest

import Shortly

from aiohttp import web


class Test_ShorteningHandler(unittest.TestCase):

    def setUp(self):
        self.shortening_handler = Shortly.ShorteningHandler()

    # Test for encode to decode match
    def test_roundtrip(self):
        original_url = 'www.google.com'
        short_url = self.shortening_handler.encode(original_url)
        decoded_url = self.shortening_handler.decode(short_url)
        self.assertEqual(original_url, decoded_url)

    # Test for encoding twice the same URL that the result is the same
    def test_encode_same_url_twice(self):
        original_url = 'www.google.com'
        short_url1 = self.shortening_handler.encode(original_url)
        short_url2 = self.shortening_handler.encode(original_url)
        self.assertEqual(short_url1, short_url2)

    # Test for encoding two different URLs that the result is NOT the same
    def test_encode_diff_urls(self):
        original_url1 = 'www.google.com'
        original_url2 = 'www.dw.com'
        short_url1 = self.shortening_handler.encode(original_url1)
        short_url2 = self.shortening_handler.encode(original_url2)
        self.assertNotEqual(short_url1, short_url2)

    # Test for non-existent url
    def test_decode_nonexistent_url(self):
        with self.assertRaises(web.HTTPBadRequest):
            self.shortening_handler.decode('non_existent_short_url_suffix')

    # Test URL with subfolders
    def test_roundtrip_using_url_with_subfolders(self):
        original_url = 'www.mysite.com/subfolder1/subfolder2'
        short_url = self.shortening_handler.encode(original_url)
        decoded_url = self.shortening_handler.decode(short_url)
        self.assertEqual(original_url, decoded_url)

    # Test for more than 64 URLs
    def test_encode_many_urls(self):
        for i in range(64):
            current_url = 'www.mysitenumber{}.com'.format(i)
            self.shortening_handler.encode(current_url)

        url = 'www.mybrandnewsite.com'
        short_url = self.shortening_handler.encode(url)
        self.assertTrue(len(short_url) > 1)


if __name__ == '__main__':
    unittest.main()
