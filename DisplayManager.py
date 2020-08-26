import os
from threading import Timer


class DisplayManager:
    def __init__(self):
        self.timer = None
        self.env = os.getenv('PROPHET_ENV', 'production')
        self.timeout = os.getenv('PROPHET_TIMEOUT', 300)
        self.activated = False

    def activate(self):
        self.activated = True
        if self.timer is not None:
            self.timer.cancel()
            self.timer = None

        if self.timer is None:
            self.timer = Timer(int(self.timeout), self.deactivate)

        self.timer.start()

    def deactivate(self):
        self.activated = False
        self.timer = None
