import unittest as ut
from sensebuffer.wifisense import WifiSense
from sensebuffer.wifiplayback import WifiPlayback

import os
from os import listdir
from os.path import isfile, join
import time
cwd = os.getcwd()

class TestWifiSense( ut.TestCase ):
    def make_wifi_log(self):
        ws = WifiSense()
        ws.set_logging()
        ws.start()
        time.sleep(10)
        ws.running = False
        ws.join()

        log_files = [f for f in listdir(cwd) if isfile(join(cwd, f)) and 'wifisense_log' in f]
        self.assertEqual(len(log_files), 1, "Extra log files detected in current directory. Please delete.")

        return log_files[0]

    def rm_wifi_log(self):
        log_files = [f for f in listdir(cwd) if isfile(join(cwd, f)) and 'wifisense_log' in f]
        self.assertEqual(len(log_files), 1)

        os.remove(join(cwd, log_files[0]))

    def test_log(self):
        log = self.make_wifi_log()

        wp = WifiPlayback()
        wp.read_log(log)

        # Default: wp.blocking = False

        self.assertIsNotNone(wp.get())
        self.assertIsNone(wp.get())

        wp.blocking = True

        self.assertIsNotNone(wp.get())
        self.assertIsNotNone(wp.get())
        self.assertIsNotNone(wp.get())

        self.rm_wifi_log()



