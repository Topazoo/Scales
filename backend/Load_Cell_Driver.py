from Backend.HX711 import HX711
import RPi.GPIO as GPIO
import time

class Load_Cell():
    def __init__(self, dout_pin=5, pd_sck_pin=6, ref_unit=162):
        self.driver = HX711(dout=dout_pin, pd_sck=pd_sck_pin)
        self.configure(ref_unit)

    def configure(self, ref_unit):
        self.driver.set_reading_format("MSB", "MSB")
        self.driver.set_reference_unit(ref_unit)
        self.driver.reset()

        self.tare() ### MOVE TO EVENT?

    def tare(self):
        self.driver.tare()

    def read_weight(self):
        while True:
            yield self.driver.get_weight(5)
            
            self.driver.power_down()
            self.driver.power_up()
            
            time.sleep(.1)

    def exit(self):
        GPIO.cleanup()

