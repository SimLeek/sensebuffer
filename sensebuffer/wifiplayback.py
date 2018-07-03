from .protobuff.wifisense_proto import WifiLog
import time

class WifiPlayback( object ):
    def __init__(self, blocking = False, skip_if_slow = True):
        self._start_time = None
        self._log = None
        self._log_start_time = None
        self._log_i = None
        self.blocking = blocking
        self.skip_if_slow = skip_if_slow

    def read_log(self, log_filename):
        log_file = open(log_filename, 'rb')
        self._log = WifiLog()
        self._log.ParseFromString(log_file.read())
        log_file.close()

    def get(self):
        assert self._log is not None
        if self._start_time is None:
            self._start_time = time.time()
        if self._log_i is None:
            self._log_i = 0

        if self._log_i < len(self._log.quantas):
            ret = self._log.quantas[self._log_i]
            if self._log_start_time is None:
                self._log_start_time = ret.time.seconds + ret.time.nanos / 1e9
            t = time.time()
            if t - self._start_time >= (ret.time.seconds + ret.time.nanos / 1e9) - self._log_start_time:
                if self.skip_if_slow:
                    while t - self._start_time >= (ret.time.seconds + ret.time.nanos / 1e9) - self._log_start_time:
                        ret = self._log.quantas[self._log_i]
                        self._log_i += 1
                    return ret
                else:
                    self._log_i += 1
                    return ret
            else:
                if self.blocking:
                    time.sleep(((ret.time.seconds + ret.time.nanos/1e9) - self._log_start_time) - (t - self._start_time))
                    self._log_i += 1
                    return ret
                else:
                    return None

        else:
            self._log = None
            self._start_time = None
            self._log_i = None
            self._log_start_time = None




