import unittest
from score import Score

class TestScore(unittest.TestCase):

    def setUp(self):
        self.who_score1 = Score("1,강호민,85,90,95")
        self.who_score2 = Score("2,김광호,80,70,60")

    def tearDown(self):
        del self.who_score1 
        del self.who_score2

    def test_constructor(self):
        self.assertIsNotNone(self.who_score1)
        self.assertIsNotNone(self.who_score2)

    def test_number(self):
        self.assertEqual(1, self.who_score1.number)
        self.assertEqual(2, self.who_score2.number)


    def test_name_1(self):
        self.assertEqual("강호민", self.who_score1.name)

    def test_name_2(self):
        self.assertEqual("김광호", self.who_score2.name)

    def test_kor(self):
        self.assertEqual(85, self.who_score1.kor)
        self.assertEqual(80, self.who_score2.kor)

    def test_eng(self):
        self.assertEqual(90, self.who_score1.eng)
        self.assertEqual(70, self.who_score2.eng)

    def test_math(self):
        self.assertEqual(95, self.who_score1.math)
        self.assertEqual(60, self.who_score2.math)

    def test_total(self):
        self.assertEqual(270, self.who_score1.total)
        self.assertEqual(210, self.who_score2.total)

    def test_avg(self):
        self.assertEqual(90, self.who_score1.avg)
        self.assertEqual(70, self.who_score2.avg)