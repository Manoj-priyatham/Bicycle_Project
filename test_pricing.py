import pricing
import unittest

class MyTest(unittest.TestCase):
    def test_pass(self):
        output = pricing.main()
        self.assertEqual(2700, output['chain_assembly'])
        self.assertEqual(4500, output['wheels'])
        self.assertEqual(1500, output['frame'])
        self.assertEqual(6000, output['handle_bar_with_brakes'])
        self.assertEqual(4800, output['seating'])
        self.assertEqual(19500, output['total'])

if __name__ == '__main__':
    unittest.main()