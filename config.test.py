#!/usr/bin/env python

#extend this config depending on your requirements

driver = "Chrome"

mobile_test = False
mobile_name = "iPhone 6/7/8"

path = {
    "host": 'https://google.com',
}

drivers = {
    'chrome': './drivers/chromedriver',
    'firefox': './drivers/geckodriver',
    'safari': '/usr/bin/safaridriver',
}


sleep_on_wait = False