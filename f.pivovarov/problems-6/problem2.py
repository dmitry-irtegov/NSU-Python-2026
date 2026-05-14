import re
import unittest

_URL_PATTERN = re.compile(
    r'''
    (?:
        (?:https?|ftp)://
        [a-zA-Z0-9]
        (?:[a-zA-Z0-9.-]*[a-zA-Z0-9])?
        \.[a-zA-Z]{2,}
        (?::\d+)?
        (?:/[^\s?#]*)?
    |
        www\.
        [a-zA-Z0-9]
        (?:[a-zA-Z0-9.-]*[a-zA-Z0-9])?
        \.[a-zA-Z]{2,}
        (?::\d+)?
        (?:/[^\s?#]*)?
    )
    (?![a-zA-Z0-9_-])
    ''',
    re.VERBOSE | re.IGNORECASE
)

def find_urls(text):
    return _URL_PATTERN.findall(text)


class TestFindUrls(unittest.TestCase):
    # Basic protocol URLs
    def test_http_url(self):
        self.assertEqual(find_urls("Visit http://example.com"), ["http://example.com"])
    
    def test_https_url(self):
        self.assertEqual(find_urls("Secure: https://secure.example.com"), ["https://secure.example.com"])
    
    def test_ftp_url(self):
        self.assertEqual(find_urls("FTP: ftp://files.example.com"), ["ftp://files.example.com"])
    
    # www. prefix URLs
    def test_www_without_protocol(self):
        self.assertEqual(find_urls("Go to www.example.com"), ["www.example.com"])
    
    def test_www_with_subdomain(self):
        self.assertEqual(find_urls("API: www.api.example.com"), ["www.api.example.com"])
    
    # URLs with paths
    def test_url_with_simple_path(self):
        result = find_urls("See https://example.com/page")
        self.assertIn("https://example.com/page", result)
    
    def test_url_with_nested_path(self):
        result = find_urls("Link: www.example.com/path/to/resource")
        self.assertIn("www.example.com/path/to/resource", result)
    
    def test_url_with_path_and_extension(self):
        result = find_urls("File: https://cdn.example.com/js/app.min.js")
        self.assertIn("https://cdn.example.com/js/app.min.js", result)
    
    # URLs with ports
    def test_url_with_port(self):
        self.assertEqual(
            find_urls("Fronted: www.example.com:3000 check VUE"),
            ["www.example.com:3000"]
        )
    
    def test_www_with_port_and_path(self):
        result = find_urls("Dev: www.example.com:3000/api/v1")
        self.assertIn("www.example.com:3000/api/v1", result)
    
    # Multiple URLs
    def test_multiple_urls_in_text(self):
        text = "Check http://a.com and www.b.org/path or https://c.net:443"
        result = find_urls(text)
        self.assertEqual(len(result), 3)
        self.assertIn("http://a.com", result)
        self.assertIn("www.b.org/path", result)
        self.assertIn("https://c.net:443", result)
    
    # Boundary and punctuation tests
    def test_url_at_sentence_end(self):
        self.assertEqual(
            find_urls("Visit https://example.com."),
            ["https://example.com"]
        )
    
    def test_url_in_parentheses(self):
        self.assertEqual(
            find_urls("Link (www.example.com) here"),
            ["www.example.com"]
        )
    
    def test_url_with_comma_separation(self):
        result = find_urls("Sites: http://a.com, www.b.org, https://c.net")
        self.assertEqual(len(result), 3)
    
    # Negative
    def test_no_protocol_no_www(self):
        """example.com without www or protocol should not match"""
        self.assertEqual(find_urls("Go to example.com"), [])
    
    def test_url_with_query_params_excluded(self):
        """Query parameters should not be included"""
        result = find_urls("Search: https://example.com?q=test")
        self.assertEqual(result, ["https://example.com"])
    
    def test_url_with_fragment_excluded(self):
        result = find_urls("Page: www.example.com/page#section")
        self.assertEqual(result, ["www.example.com/page"])
    
    def test_invalid_tld_single_char(self):
        self.assertEqual(find_urls("Bad: www.example.c"), [])
    
    def test_malformed_domain(self):
        self.assertEqual(find_urls("Bad: http://.example.com"), [])
        self.assertEqual(find_urls("Bad: www.-example.com"), [])
    
    # Edge cases
    def test_empty_string(self):
        self.assertEqual(find_urls(""), [])
    
    def test_no_urls_in_text(self):
        self.assertEqual(find_urls("Just plain text without URLs"), [])
    
    def test_case_insensitivity(self):
        result = find_urls("Mixed: HTTP://EXAMPLE.COM and WWW.Test.ORG")
        self.assertEqual(len(result), 2)
    
    def test_url_with_hyphens_in_domain(self):
        self.assertEqual(
            find_urls("Site: https://my-site.example.com"),
            ["https://my-site.example.com"]
        )
    
    def test_url_with_numbers_in_domain(self):
        result = find_urls("API: www.api2.example123.com/v2")
        self.assertIn("www.api2.example123.com/v2", result)
    
    def test_consecutive_urls_no_spaces(self):
        # URLs separated by punctuation
        text = "Links:http://a.com,www.b.org;https://c.net"
        result = find_urls(text)
        self.assertEqual(len(result), 3)
    
    def test_url_at_start_and_end(self):
        text = "www.start.com middle text https://end.org"
        result = find_urls(text)
        self.assertEqual(result, ["www.start.com", "https://end.org"])
    
    # Complex real-world scenarios 
    def test_html_like_text(self):
        html = '<a href="https://example.com">Link</a> and www.test.org/page'
        result = find_urls(html)
        self.assertIn("https://example.com", result)
        self.assertIn("www.test.org/page", result)
    
    def test_mixed_valid_invalid(self):
        text = "Valid: http://ok.com, invalid: bad-domain, valid: www.also.org"
        result = find_urls(text)
        self.assertEqual(result, ["http://ok.com", "www.also.org"])
    
    def test_multiple_generation(self):
        """Test with large text to ensure efficiency"""
        base_url = "www.example.com/page"
        large_text = " ".join([f"URL{i}:{base_url}{i}" for i in range(1000)])
        result = find_urls(large_text)
        self.assertEqual(len(result), 1000)
        # Verify all URLs have correct format
        for url in result:
            self.assertTrue(url.startswith("www.example.com/page"))


if __name__ == '__main__':
    unittest.main()