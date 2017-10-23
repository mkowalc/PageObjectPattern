#!/usr/bin/env python
import unittest
import testCases

if __name__ == "__main__":
    print("TEST")
    suite = unittest.TestLoader().loadTestsFromTestCase(testCases.ExampleTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
