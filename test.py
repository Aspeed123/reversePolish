import unittest
import Calculator as calc


class TestCalculator(unittest.TestCase):

    def test_precedence(self):
        self.assertEqual(calc.precedence('+'), 1)
        self.assertEqual(calc.precedence('-'), 1)
        self.assertEqual(calc.precedence('*'), 2)
        self.assertEqual(calc.precedence('/'), 2)
        self.assertEqual(calc.precedence('^'), 3)
        self.assertEqual(calc.precedence('('), 0)
        self.assertEqual(calc.precedence('x'), 0)

    def test_to_rpn_simple(self):
        self.assertEqual(calc.to_rpn("3+4*2/(1-5)^2^3"),
                         ['3', '4', '2', '*', '1', '5', '-', '2', '^', '3',
                          '^', '/', '+'])
        self.assertEqual(calc.to_rpn("1+(2*3)"), ['1', '2', '3', '*', '+'])
        self.assertEqual(calc.to_rpn("(1+2)*3"), ['1', '2', '+', '3', '*'])

    def test_eval_rpn_basic(self):
        rpn = ['3', '4', '2', '*', '+']
        self.assertAlmostEqual(calc.eval_rpn(rpn), 11.0)
        rpn2 = ['5', '1', '2', '+', '4', '*', '+', '3', '-']
        self.assertAlmostEqual(calc.eval_rpn(rpn2), 14.0)

    def test_calculate_integration(self):
        self.assertAlmostEqual(calc.calculate("3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3"),
                               3.001953125)
        self.assertAlmostEqual(calc.calculate("1 + (2 * 3)"), 7)
        self.assertAlmostEqual(calc.calculate("(1 + 2) * 3"), 9)


if __name__ == "__main__":
    unittest.main()
