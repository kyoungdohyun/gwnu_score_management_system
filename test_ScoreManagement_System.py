import unittest
from Score_Management import Score_Management_System
from unittest.mock import mock_open
from unittest.mock import patch


class TestScoreManagement(unittest.TestCase):

    def setUp(self):
        self.m_open_1 = mock_open(read_data="1,강호민,85,90,95\n")
        self.m_open_2 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n") 
        self.m_open_3 = mock_open(read_data="1,강호민,85,90,95\n2,김광호,80,70,60\n3,김민식,75,85,80\n") 

        self.m_write_open = mock_open()
        self.m_w = mock_open().return_value
        self.m_write_open.side_effect = [self.m_open_3.return_value, self.m_w]

    
    def test_constructor(self):
        sms = Score_Management_System()
        self.assertIsNotNone(sms)

    def test_read1(self):
        with patch('Score_Management.open', self.m_open_1):
            sms = Score_Management_System()
            self.assertEqual(1, sms.read('score.csv')) 

    def test_read2(self):
        with patch('Score_Management.open', self.m_open_2):
            sms = Score_Management_System()
            self.assertEqual(2, sms.read('score.csv'))

    def test_read3(self):
        with patch('Score_Management.open', self.m_open_3):
            sms = Score_Management_System()
            self.assertEqual(3, sms.read('score.csv'))

    def test_sort1(self):
        with patch('Score_Management.open', self.m_open_1):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort(order_key="reg", order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90.0', result)

    def test_sort2(self):
        with patch('Score_Management.open', self.m_open_2):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort(order_key="reg", order_way="asc")
            self.assertEqual('1,강호민,85,90,95,270,90.0\n2,김광호,80,70,60,210,70.0', result)

    def test_sort3(self):
        with patch('Score_Management.open', self.m_open_2):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort(order_key="reg", order_way="des")
            self.assertEqual('2,김광호,80,70,60,210,70.0\n1,강호민,85,90,95,270,90.0', result)

    def test_sort4(self):
        with patch('Score_Management.open', self.m_open_2):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort("avg", "asc")
            self.assertEqual('2,김광호,80,70,60,210,70.0\n1,강호민,85,90,95,270,90.0', result)

    def test_sort5(self):
        with patch('Score_Management.open', self.m_open_2):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort("avg", "des")
            self.assertEqual('1,강호민,85,90,95,270,90.0\n2,김광호,80,70,60,210,70.0', result)

    def test_sort6(self):
        with patch('Score_Management.open', self.m_open_3):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort('avg', "asc")
            self.assertEqual('2,김광호,80,70,60,210,70.0\n3,김민식,75,85,80,240,80.0\n1,강호민,85,90,95,270,90.0', result)


    def test_sort7(self):
        with patch('Score_Management.open', self.m_open_3):
            sms = Score_Management_System()
            sms.read('score_data.csv')

            result = sms.sort('avg', "des")
            self.assertEqual('1,강호민,85,90,95,270,90.0\n3,김민식,75,85,80,240,80.0\n2,김광호,80,70,60,210,70.0', result)

    def test_write_1(self):
        with patch('Score_Management.open', self.m_write_open):
            sms = Score_Management_System()
            sms.read('score_data.csv')
            sms.write('result.csv')

        self.m_w.write.assert_called_with('1,강호민,85,90,95,270,90.0\n2,김광호,80,70,60,210,70.0\n3,김민식,75,85,80,240,80.0')

    def test_write_2(self):
        with patch('Score_Management.open', self.m_write_open):
            sms = Score_Management_System()
            sms.read('score_data.csv')
            sms.write('result.csv', 'avg', 'des')

        self.m_w.write.assert_called_with("1,강호민,85,90,95,270,90.0\n3,김민식,75,85,80,240,80.0\n2,김광호,80,70,60,210,70.0")

    def test_write_3(self):
        with patch('Score_Management.open', self.m_write_open):
            sms = Score_Management_System()
            sms.read('score_data.csv')
            sms.write('result.csv', 'avg', 'asc')

        self.m_w.write.assert_called_with("2,김광호,80,70,60,210,70.0\n3,김민식,75,85,80,240,80.0\n1,강호민,85,90,95,270,90.0")

    def test_write_4(self):
        with patch('Score_Management.open', self.m_write_open):
            sms = Score_Management_System()
            sms.read('score_data.csv')
            sms.write('result.csv', 'avg', 'des')

        self.m_w.write.assert_called_with("1,강호민,85,90,95,270,90.0\n3,김민식,75,85,80,240,80.0\n2,김광호,80,70,60,210,70.0")


    if __name__ == "__main__":
        unittest.main()