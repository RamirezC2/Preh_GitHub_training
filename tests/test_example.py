"""Tests for the dummy training module."""

from pathlib import Path
import sys
import unittest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from preh_github_training import get_training_message


class TrainingMessageTests(unittest.TestCase):
    def test_default_team_message(self) -> None:
        self.assertEqual(get_training_message(), "Welcome to GitHub training, team!")

    def test_custom_team_message(self) -> None:
        self.assertEqual(
            get_training_message("Preh Team"),
            "Welcome to GitHub training, Preh Team!",
        )


if __name__ == "__main__":
    unittest.main()
