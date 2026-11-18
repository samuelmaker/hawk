import unittest

from csv_safety import spreadsheet_safe


class CsvSafetyTests(unittest.TestCase):
    def test_formula_payloads_remain_text(self):
        for payload in ['=HYPERLINK("https://example.test")', '+1+1', '-1+1', '@SUM(1)', '  =1+1', '\ttext', '\r=1', '\n=1']:
            with self.subTest(payload=payload):
                self.assertEqual(spreadsheet_safe(payload), "'" + payload)

    def test_normal_titles_and_numbers_are_preserved(self):
        for value in ['Safari video', '', 'https://example.test/video', 12, 0]:
            self.assertEqual(spreadsheet_safe(value), value)

    def test_escaped_titles_are_not_escaped_again(self):
        self.assertEqual(spreadsheet_safe(spreadsheet_safe('=1+1')), "'=1+1")


if __name__ == '__main__':
    unittest.main()
