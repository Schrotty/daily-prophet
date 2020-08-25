import os
from threading import Timer

from rpi_backlight import Backlight


class DisplayManager:
    def __init__(self):
        self.timer = None
        self.env = os.getenv('PROPHET_ENV', 'production')
        self.timeout = os.getenv('PROPHET_TIMEOUT', 300)
        self.activated = False

        if self.env != 'development':
            self.backlight = Backlight()

    def activate(self):
        self.activated = True
        if self.env != 'development':
            self.backlight.power = True

        if self.timer is not None:
            self.timer.cancel()
            self.timer = None
            print("Timer stopped!")

        if self.timer is None:
            self.timer = Timer(int(self.timeout), self.deactivate)
            print("Timer set!")

        self.timer.start()

    def deactivate(self):
        self.activated = False
        self.timer = None

        if self.env != 'development':
            self.backlight.power = False

        print("Timer executed! Display disabled!")
