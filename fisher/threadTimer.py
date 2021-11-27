import threading
from threading import Timer

class ThreadTimer():
    _instance = None
    _lock = threading.Lock() 

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls.theThread = Timer(15,)
                    cls.busy = False
                    cls._instance = super(ThreadTimer, cls).__new__(cls)
        return cls._instance

    def start(cls):
        cls.theThread.start()

    def setBusy(cls):
        cls.busy = True

    def setNotBusy(cls):
        cls.busy = False

    def cancel(cls):
        cls.theThread.cancel()