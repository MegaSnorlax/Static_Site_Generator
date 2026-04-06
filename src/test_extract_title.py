import unittest

from extract_title import extract_title


class TestExtractTitle(unittest.TestCase):

    def test_extract_title(self):
        md = """
# H1 Heading
## H2 Heading
### H3 Heading

Text in a paragraph


This is another paragraph with _italic_ text and `code` here

"""

        heading = extract_title(md)

        self.assertEqual(
            heading,
            "H1 Heading"
        )


if __name__ == "__main__":
    unittest.main()

