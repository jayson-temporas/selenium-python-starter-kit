import unittest
from optparse import OptionParser
from test_case.home_page_test import HomePageTest

import config

parser = OptionParser()
parser.add_option("-m", "--mobile", action="store_true", default=False, help="Run test on mobile")
parser.add_option("-c", "--chrome", action="store_true", default=False, help="Run in chrome")
parser.add_option("-f", "--firefox", action="store_true", default=False, help="Run in firefox")
parser.add_option("-s", "--safari", action="store_true", default=False, help="Run in safari")
parser.add_option("-w", "--wait", action="store_true", default=False, help="Use sleep")

(options, args) = parser.parse_args()

config.mobile_test = options.mobile

if config.mobile_test:
    print("Running test in mobile")

if options.chrome:
    config.driver = 'Chrome'
elif options.firefox:
    config.driver = 'Firefox'
elif options.safari:
    config.driver = 'Safari'

if options.wait:
    config.sleep_on_wait = True


# we should add all test here
appTestSuite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(HomePageTest),
])

unittest.TextTestRunner(verbosity=2).run(appTestSuite)

