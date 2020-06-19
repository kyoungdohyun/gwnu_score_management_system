import unittest
from Score_Management import Score_Management_System
from unittest.mock import mock_open
from unittest.mock import patch


class TestScoreManagement(unittest.TestCase):

    def setUp(self):
        self.s_open_1 = mock_open(read_data="1,강호민,85,90,95\n")
        self.s_open_2 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n") 
        self.s_open_3 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n3,김민식,75,85,80\n") 

    
    def test_constructor(self):
        sms = Score_Management_System()
        self.assertIsNotNone(sms)

    def test_read1(self):
        with patch('Score_Management.open', self.s_open_1):
            sms = Score_Management_System()
            self.assertEqual(1, sms.read('score.csv')) 

    def test_read2(self):
        with patch('Score_Management.open', self.s_open_2):
            sms = Score_Management_System()
            self.assertEqual(2, sms.read('score.csv'))

    def test_read3(self):
        with patch('Score_Management.open', self.s_open_3):
            sms = Score_Management_System()
            self.assertEqual(3, sms.read('score.csv'))

    def test_sort1(self):
        with patch('Score_Management.open', self.s_open_1):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort(order_key="reg", order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90.0', result)

    def test_sort2(self):
        with patch('Score_Management.open', self.s_open_2):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort(order_key="reg", order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90.0\n2,김광호,80,70,60,210,70.0', result)

    def test_sort3(self):
        with patch('Score_Management.open', self.s_open_2):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort(order_key="reg", order_way="des")
            self.assertEqual('2,김광호,80,70,60,210,70.0\n1,강호민,85,90,95,270,90.0', result)

    def test_sort4(self):
        with patch('Score_Management.open', self.s_open_2):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort("avg", "asc")
            self.assertEqual('2,김광호,80,70,60,210,70.0\n1,강호민,85,90,95,270,90.0', result)

    def test_sort5(self):
        with patch('Score_Management.open', self.s_open_2):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort("avg", "des")
            self.assertEqual('1,강호민,85,90,95,270,90.0\n2,김광호,80,70,60,210,70.0', result)

    def test_sort6(self):
        with patch('Score_Management.open', self.s_open_3):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort('avg', "asc")
            self.assertEqual('2,김광호,80,70,60,210,70.0\n3,김민식,75,85,80,240,80.0\n1,강호민,85,90,95,270,90.0', result)


    def test_sort7(self):
        with patch('Score_Management.open', self.s_open_3):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort('avg', "des")
            self.assertEqual('1,강호민,85,90,95,270,90.0\n3,김민식,75,85,80,240,80.0\n2,김광호,80,70,60,210,70.0', result)


    if __name__ == "__main__":
        unittest.main()