import unittest
import ipynb.fs.full.exercises as ex
import numpy as np
import pandas as pd

class TestAssignmentFive(unittest.TestCase):
    def test_01_create_nba_teams(self):
        nba_teams = ex.create_nba_teams()
        self.assertIsInstance(nba_teams, pd.core.frame.DataFrame)
        self.assertEqual(nba_teams.shape, (30, 6))
        self.assertEqual(nba_teams["tricode"].nunique(), 30)
        self.assertEqual(nba_teams["confName"].nunique(), 2)
        self.assertEqual(nba_teams["divName"].nunique(), 6)
    def test_02_create_nba_coaches(self):
        nba_coaches = ex.create_nba_coaches()
        self.assertIsInstance(nba_coaches, pd.core.frame.DataFrame)
        self.assertEqual(nba_coaches.shape, (243, 3))
        self.assertEqual(nba_coaches["tricode"].nunique(), 30)
        self.assertEqual(nba_coaches["is_assistant"].nunique(), 2)
    def test_03_create_nba_players(self):
        nba_players = ex.create_nba_players()
        self.assertIsInstance(nba_players, pd.core.frame.DataFrame)
        self.assertEqual(nba_players.shape, (506, 2))
        self.assertEqual(nba_players["current_team_id"].nunique(), 30)
    def test_04_create_nba_teams_and_coaches(self):
        nba_teams_and_coaches = ex.create_nba_teams_and_coaches()
        self.assertIsInstance(nba_teams_and_coaches, pd.core.frame.DataFrame)
        self.assertEqual(nba_teams_and_coaches.shape, (243, 3))
        self.assertEqual(nba_teams_and_coaches["is_assistant"].nunique(), 2)
    def test_05_create_nba_teams_and_players(self):
        nba_teams_and_players = ex.create_nba_teams_and_players()
        self.assertIsInstance(nba_teams_and_players, pd.core.frame.DataFrame)
        self.assertEqual(nba_teams_and_players.shape, (506, 2))
        self.assertEqual(nba_teams_and_players["fullName"].nunique(), 30)
    def test_06_find_nba_head_coaches(self):
        nba_head_coaches = ex.find_nba_head_coaches()
        self.assertIsInstance(nba_head_coaches, pd.core.frame.DataFrame)
        self.assertEqual(nba_head_coaches.shape, (30, 3))
        self.assertEqual(nba_head_coaches["is_assistant"].nunique(), 1)
    def test_07_find_bkn_phx_rosters(self):
        bkn_phx_rosters = ex.find_bkn_phx_rosters()
        self.assertIsInstance(bkn_phx_rosters, pd.core.frame.DataFrame)
        self.assertEqual(bkn_phx_rosters.shape, (52, 3))
        self.assertEqual(bkn_phx_rosters["type"].nunique(), 3)
    def test_08_summarize_pandemic_by_country(self):
        pandemic_by_country = ex.summarize_pandemic_by_country()
        self.assertIsInstance(pandemic_by_country, pd.core.frame.DataFrame)
        self.assertEqual(pandemic_by_country.shape, (196, 3))
    def test_09_find_taiwan_from_covid_time_series(self):
        taiwan_from_covid_time_series = ex.find_taiwan_from_covid_time_series()
        self.assertIsInstance(taiwan_from_covid_time_series, pd.core.frame.DataFrame)
        self.assertEqual(taiwan_from_covid_time_series.shape, (685, 4))
    def test_10_transform_taiwan_data(self):
        taiwan_data = ex.transform_taiwan_data()
        self.assertIsInstance(taiwan_data, pd.core.frame.DataFrame)
        self.assertEqual(taiwan_data.shape, (1370, 3))
        self.assertEqual(taiwan_data["Variable"].nunique(), 2)

suite = unittest.TestLoader().loadTestsFromTestCase(TestAssignmentFive)
runner = unittest.TextTestRunner(verbosity=2)
if __name__ == '__main__':
    test_results = runner.run(suite)
number_of_failures = len(test_results.failures)
number_of_errors = len(test_results.errors)
number_of_test_runs = test_results.testsRun
number_of_successes = number_of_test_runs - (number_of_failures + number_of_errors)
print("You've got {} successes among {} questions.".format(number_of_successes, number_of_test_runs))
