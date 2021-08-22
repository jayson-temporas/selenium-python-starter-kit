# Selenium Python Starter Kit

This selenium python starter kit is designed to get you up and running faster and worry less on settings and configuration.

## Setup

### Install Python and Selenium

- Should have python 3 and selenium installed
- Download webdrivers for Chrome and Firefox and update the config path
- Find your safari browser webdriver, usually located at /usr/bin/safaridriver, update config path if necessary

### Create config.py for our test env variables

```
cp config.test.py config.py
```

## Adding Tests

Add your test file inside test_case directory

```
import unittest
import config
from BaseTestCases import BaseTestCases

class HomePageTest(BaseTestCases.BaseTest):

    def test_homepage_loads_successfully(self):
        self.driver.get(config.path['host'])

        self.wait_for_page_load()

        self.assertIn('Google Search', self.driver.page_source)
    

if __name__ == "__main__":
    unittest.main()
```

import it on app.py

```
from test_case.home_page_test import HomePageTest 
```

then add it on our test suite

```
appTestSuite = unittest.TestSuite([
    unittest.TestLoader().loadTestsFromTestCase(HomePageTest),
])

unittest.TextTestRunner(verbosity=2).run(appTestSuite)
```

You can add test case and test suite as you need

## Run Tests

### Run tests on Desktop

```
python3 app.py --chrome
```

```
python3 app.py --firefox
```

```
python3 app.py --safari
```

### Run tests on Mobile Emulator

```
python3 app.py --chrome --mobile
```

```
python3 app.py --firefox --mobile
```

Safari does not support mobile emulator on test automation

> Note: Web Drivers included in this repo may not work on your system. Download the web drivers that's compatible to your system and place it inside the drivers directory. Update config path if necessary.
