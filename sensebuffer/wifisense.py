import pywifi
import time
import threading
from protobuff.wifisense_proto import WifiQuanta, WifiLog
from typing import Optional

class WifiSense( threading.Thread ):
    def __init__(self, poll_time=1):
        super().__init__(target= self.thread)
        self.poll_time = poll_time
        self.running = True

        self.wifi = pywifi.PyWiFi()

        self.iface = self.wifi.interfaces()[0]
        self._log = None

        self.publish = None
        self.atexit = None

    def set_logging(self):
        self.publish = self.log
        self.atexit = self.log_to_file

    def log(self, quanta):
        if self._log is None:
            self._log = WifiLog()

        q = self._log.quantas.add()
        q.profiles.extend(quanta.profiles)
        q.time.seconds = quanta.time.seconds
        q.time.nanos = quanta.time.nanos

    def log_to_file(self, filename=None):
        assert self._log is not None

        if filename is None: filename = "wifisense_log_{}.bin".format(time.time())
        f = open(filename, 'wb')
        f.write(self._log.SerializeToString())
        f.close()

    def thread(self):
        while self.running:
            wq = WifiQuanta()
            self.iface.scan()
            time.sleep(self.poll_time)
            for p in self.iface.scan_results():
                wp = wq.profiles.add()
                wp.ssid = p.ssid
                wp.bssid = p.bssid
            t = time.time()
            wq.time.seconds = int(t)
            wq.time.nanos = int((t - wq.time.seconds) * 1e9)
            if self.publish is not None:
                self.publish(wq)
        if self.atexit is not None:
            self.atexit()