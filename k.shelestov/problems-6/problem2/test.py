import unittest
from problem2 import find_urls 

class TestFindUrls(unittest.TestCase):

    def test_simple_http_https_www(self):
        text = "http://example.com https://secure.org www.site.net"
        expected = ["http://example.com", "https://secure.org", "www.site.net"]
        self.assertEqual(find_urls(text), expected)

    def test_hyphens_and_numbers(self):
        text = "www.site-123.com http://abc-456.org https://my-789-site.net"
        expected = ["www.site-123.com", "http://abc-456.org", "https://my-789-site.net"]
        self.assertEqual(find_urls(text), expected)

    def test_subdomains(self):
        text = "www.sub.domain.com https://deep.sub.domain.org"
        expected = ["www.sub.domain.com", "https://deep.sub.domain.org"]
        self.assertEqual(find_urls(text), expected)

    def test_edges(self):
        text = "www.start.com some text in the middle http://end.org"
        expected = ["www.start.com", "http://end.org"]
        self.assertEqual(find_urls(text), expected)

    def test_uppercase(self):
        text = "WWW.EXAMPLE.COM Http://Test.Org"
        expected = ["WWW.EXAMPLE.COM", "Http://Test.Org"]
        self.assertEqual(find_urls(text), expected)

    def test_punctuation(self):
        text = "Check www.example.com, and http://test.org!"
        expected = ["www.example.com", "http://test.org"]
        self.assertEqual(find_urls(text), expected)

    def test_multiple_dots(self):
        text = "www.sub.domain.example.com http://a.b.c.d.org"
        expected = ["www.sub.domain.example.com", "http://a.b.c.d.org"]
        self.assertEqual(find_urls(text), expected)

    def test_non_urls(self):
        text = "example.com not a URL, test@site.org neither"
        expected = []
        self.assertEqual(find_urls(text), expected)

    def test_mixed_text(self):
        text = ("Hello www.site1.com, visit http://site2.org or https://secure-site.net. "
                "Also check www.site-3.org, notmail@example.com, and numbers123.com")
        expected = ["www.site1.com", "http://site2.org", "https://secure-site.net", "www.site-3.org"]
        self.assertEqual(find_urls(text), expected)

    def test_long_domains(self):
        text = "www." + "sub-"*10 + "domain.com"
        expected = ["www.sub-sub-sub-sub-sub-sub-sub-sub-sub-sub-domain.com"]
        self.assertEqual(find_urls(text), expected)

    def test_mixed_protocols_www(self):
        text = "www.example.com https://example.org http://example.net"
        expected = ["www.example.com", "https://example.org", "http://example.net"]
        self.assertEqual(find_urls(text), expected)

    def test_hyphens_subdomains(self):
        text = "https://sub-domain.example-site.org www.a-b.c-d.net"
        expected = ["https://sub-domain.example-site.org", "www.a-b.c-d.net"]
        self.assertEqual(find_urls(text), expected)

    def test_no_www_no_http(self):
        text = "example.com justtext another-site.org"
        expected = []
        self.assertEqual(find_urls(text), expected)

    def test_various_combinations(self):
        text = ("Visit www.one.com, www.two-site.org, http://three.net, "
                "https://four-site.com, www.five-six-seven.org")
        expected = ["www.one.com", "www.two-site.org", "http://three.net", "https://four-site.com", "www.five-six-seven.org"]
        self.assertEqual(find_urls(text), expected)

    def test_empty_text(self):
        self.assertEqual(find_urls(""), [])

    def test_text_without_urls(self):
        text = "No links here, just text and numbers 1234."
        self.assertEqual(find_urls(text), [])

    def test_numbers_hyphens_domains(self):
        text = "www.123-site.com http://456-test.org https://7-8-9.net"
        expected = ["www.123-site.com", "http://456-test.org", "https://7-8-9.net"]
        self.assertEqual(find_urls(text), expected)

    def test_complex_domains(self):
        text = "www.a-b.c-d.e-f.g-h.i-j.k-l.com"
        expected = ["www.a-b.c-d.e-f.g-h.i-j.k-l.com"]
        self.assertEqual(find_urls(text), expected)

if __name__ == "__main__":
    unittest.main()