#!/usr/bin/env python3

import unittest

from main import find_urls


class TestFindUrls(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(
            find_urls(""),
            []
        )

    def test_no_urls(self):
        self.assertEqual(
            find_urls("Just a plain text with no links."),
            []
        )

    def test_single_www(self):
        self.assertEqual(
            find_urls("Visit www.example.com for details."),
            [
                "www.example.com",
            ]
        )

    def test_single_http(self):
        self.assertEqual(
            find_urls("Visit http://example.com for details."),
            [
                "http://example.com",
            ]
        )

    def test_single_https(self):
        self.assertEqual(
            find_urls("Secure site: https://example.com"),
            [
                "https://example.com",
            ]
        )

    def test_multiple_urls(self):
        self.assertEqual(
            find_urls("Links: www.a.com and http://b.org and https://c.net."),
            [
                "www.a.com",
                "http://b.org",
                "https://c.net",
            ]
        )

    def test_urls_with_subdomains(self):
        self.assertEqual(
            find_urls("See www.docs.example.com and http://blog.example.co.uk"),
            [
                "www.docs.example.com",
                "http://blog.example.co.uk",
            ]
        )

    def test_urls_with_path(self):
        self.assertEqual(
            find_urls("Open www.example.com/index and http://site.org/a/b/c"),
            [
                "www.example.com/index",
                "http://site.org/a/b/c",
            ]
        )

    def test_urls_with_hyphen(self):
        self.assertEqual(
            find_urls("Read www.my-site.org and http://great-site.com/page"),
            [
                "www.my-site.org",
                "http://great-site.com/page",
            ]
        )

    def test_urls_with_punctuation(self):
        self.assertEqual(
            find_urls("Go to www.example.com, then http://example.org!"),
            [
                "www.example.com",
                "http://example.org",
            ]
        )

    def test_urls_in_brackets(self):
        self.assertEqual(
            find_urls("(www.example.com) [http://example.org] {https://site.net}"),
            [
                "www.example.com",
                "http://example.org",
                "https://site.net",
            ]
        )

    def test_urls_at_edges(self):
        self.assertEqual(
            find_urls("www.example.com is first and last is http://example.org"),
            [
                "www.example.com",
                "http://example.org",
            ]
        )

    def test_urls_on_separate_lines(self):
        self.assertEqual(
            find_urls(
                "First line www.one.com\n"
                "Second line http://two.org\n"
                "Third line https://three.net/path"
            ),
            [
                "www.one.com",
                "http://two.org",
                "https://three.net/path",
            ]
        )

    def test_duplicate_urls(self):
        self.assertEqual(
            find_urls("www.example.com and again www.example.com"),
            [
                "www.example.com",
                "www.example.com",
            ]
        )

    def test_mixed_case(self):
        self.assertEqual(
            find_urls("WWW.Example.COM and HTTP://Example.ORG/path"),
            [
                "WWW.Example.COM",
                "HTTP://Example.ORG/path",
            ]
        )

    def test_does_not_find_bare_domain(self):
        self.assertEqual(
            find_urls("example.com should not count, but www.example.com should."),
            ["www.example.com"]
        )

    def test_does_not_find_email(self):
        self.assertEqual(
            find_urls("Write to user@example.com or visit www.example.com"),
            [
                "www.example.com",
            ]
        )

    def test_works_with_many_urls(self):
        self.assertEqual(
            find_urls("a www.a.com b http://b.org c https://c.net d www.d.io/e f http://f.ru/path g www.g.org"),
            [
                "www.a.com",
                "http://b.org",
                "https://c.net",
                "www.d.io/e",
                "http://f.ru/path",
                "www.g.org",
            ]
        )


if __name__ == "__main__":
    unittest.main()
