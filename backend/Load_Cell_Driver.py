from Backend.HX711 import HX711
import RPi.GPIO as GPIO
import time

class Load_Cell():
    def __init__(self, dout_pin=5, pd_sck_pin=6, ref_unit=162):

        self.is_connected = False

        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.ref_unit = ref_unit

        self.reset()
        
        self.is_connected = True

    def reset(self):
        self.is_connected = False

        self.driver = HX711(dout=self.dout_pin, pd_sck=self.pd_sck_pin)
        self.configure()

        self.is_connected = True

    def configure(self, ref_unit):
        self.driver.set_reading_format("MSB", "MSB")
        self.set_reference_unit(self.ref_unit)
        self.tare() ### MOVE TO EVENT?

    def tare(self):
        self.driver.tare()

    def read_weight(self):
        while True and self.is_connected:
            try:
                yield self.driver.get_weight(5) 
                self.cycle()
                time.sleep(.1)

            except (KeyboardInterrupt, SystemExit):
                self.exit()

    def set_reference_unit(self, unit):
        self.ref_unit = unit
        self.driver.set_reference_unit(unit)
        self.driver.reset()

    def cycle(self):
        self.driver.power_down()
        self.driver.power_up()

    def exit(self):
        self.is_connected = False
        
        self.driver.power_down()
        GPIO.cleanup()
