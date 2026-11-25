import subprocess
import sys
import unittest


class HistimelineTest(unittest.TestCase):
    def run_command(self, text, *arguments):
        return subprocess.run(
            [sys.executable, "histimeline.py", *arguments],
            input=text,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_events_are_sorted_by_date(self):
        result = self.run_command(
            "1945-08-15\t終戦\n"
            "1868-01-03\t王政復古の大号令\n"
        )

        self.assertEqual(
            result.stdout,
            "- 1868-01-03：王政復古の大号令\n"
            "- 1945-08-15：終戦\n",
        )
        self.assertEqual(result.stderr, "")

    def test_invalid_line_is_reported(self):
        result = self.run_command(
            "間違った入力\n"
            "1945-08-15\t終戦\n"
        )

        self.assertIn("入力エラー", result.stderr)
        self.assertEqual(result.stdout, "- 1945-08-15：終戦\n")

    def test_blank_lines_are_ignored(self):
        result = self.run_command(
            "\n"
            "1945-08-15\t終戦\n"
            "\n"
        )

        self.assertEqual(result.stdout, "- 1945-08-15：終戦\n")
        self.assertEqual(result.stderr, "")

    def test_year_filter(self):
        result = self.run_command(
            "1945-08-15\t終戦\n"
            "1868-01-03\t王政復古の大号令\n",
            "--year",
            "1945",
        )

        self.assertEqual(result.stdout, "- 1945-08-15：終戦\n")
        self.assertEqual(result.stderr, "")

    def test_keyword_filter(self):
        result = self.run_command(
            "1600-10-21\t関ヶ原の戦い\n"
            "1945-08-15\t終戦\n"
            "1868-01-03\t王政復古の大号令\n",
            "--keyword",
            "戦い",
        )

        self.assertEqual(result.stdout, "- 1600-10-21：関ヶ原の戦い\n")
        self.assertEqual(result.stderr, "")

if __name__ == "__main__":
    unittest.main()
