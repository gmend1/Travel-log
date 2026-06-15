"""Unit tests to test functionality of project.
"""

import unittest
from travel import normalize_state, calculate_average_rating


class TestTravelLog(unittest.TestCase):

    def setUp(self):
        self.state_map = {
            "ca": "California",
            "california": "California",
            "ny": "New York",
            "new york": "New York",
            "tx": "Texas",
            "texas": "Texas"
        }


    def test_state_abbreviation(self):
        self.assertEqual(
            normalize_state("ca", self.state_map),
            "California"
        )

 
    def test_state_whitespace(self):
        self.assertEqual(
            normalize_state("  tx  ", self.state_map),
            "Texas"
        )

   
    def test_unknown_state(self):
        self.assertEqual(
            normalize_state("florida", self.state_map),
            "Florida"
        )

  
    def test_average_rating(self):
        travel = [
            {"state": "CA", "city": "LA", "rating": 8},
            {"state": "TX", "city": "Austin", "rating": 10},
            {"state": "NY", "city": "NYC", "rating": 6}
        ]

        self.assertAlmostEqual(
            calculate_average_rating(travel),
            8.0
        )

  
    def test_average_rating_with_none(self):
        travel = [
            {"state": "CA", "city": "LA", "rating": None},
            {"state": "TX", "city": "Austin", "rating": 10}
        ]

        self.assertEqual(
            calculate_average_rating(travel),
            10
        )


if __name__ == "__main__":
    unittest.main()
                 
    