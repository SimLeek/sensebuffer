import unittest as ut
from sensebuffer.wifisense import WifiSense

import os
from os import listdir
from os.path import isfile, join
import time
cwd = os.getcwd()

class TestWifiSense( ut.TestCase ):
    def test_log(self):
        ws = WifiSense()
        ws.set_logging()
        ws.start()
        time.sleep(10)
        ws.running = False
        ws.join()

        log_files = [f for f in listdir(cwd) if isfile(join(cwd, f)) and 'wifisense_log' in f]
        self.assertEqual(len(log_files),1)
        os.remove(join(cwd, log_files[0]))