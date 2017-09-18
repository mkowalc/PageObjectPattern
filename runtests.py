#!/usr/bin/env python
import unittest
import testCases
import environment
import sys

if __name__ == "__main__":
    print(environment.bcolors.HEADER + "TEST" + environment.bcolors.ENDC)
    suite = unittest.TestLoader().loadTestsFromTestCase(testCases.eIDTEST)
    unittest.TextTestRunner(verbosity=2).run(suite)
