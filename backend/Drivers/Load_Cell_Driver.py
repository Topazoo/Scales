#! /usr/bin/env python

from backend.Drivers.HX711_Driver import HX711
import time, random
try:
    import RPi.GPIO as GPIO
except Exception as e:
    print(' * Module Warning: {}'.format(e))

class Load_Cell():
    def __init__(self, dout_pin=5, pd_sck_pin=6, ref_unit=162):
        self.is_connected = False

        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.ref_unit = ref_unit

    def connect(self):
        self.reset()
        self.tare() ### MOVE TO EVENT?

    def reset(self):
        self.is_connected = False

        try:
            self.driver = HX711(dout=self.dout_pin, pd_sck=self.pd_sck_pin)
            self.configure(self.ref_unit)
            self.is_connected = True
        except Exception as e:
            print('Load Cell Error: {}'.format(e))

    def configure(self, ref_unit):
        self.driver.set_reading_format("MSB", "MSB")
        self.set_reference_unit(ref_unit)

    def tare(self):
        self.driver.tare()

    def read_weight(self):
        while True:
            try:
                if self.is_connected:
                    yield {'data': self.driver.get_weight(5)}
                    self.cycle()
                else:
                    yield None

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

    def disconnect(self):
        self.driver.power_down()
        GPIO.cleanup()

        self.is_connected = False

class Dummy_Load_Cell():
    def __init__(self, dout_pin=5, pd_sck_pin=6, ref_unit=162):
        self.is_connected = False

        self.dout_pin = dout_pin
        self.pd_sck_pin = pd_sck_pin
        self.ref_unit = ref_unit

    def connect(self):
        self.reset()
        self.tare() ### MOVE TO EVENT?

    def reset(self):
        self.is_connected = False

        print('RESET DUMMY LOAD CELL')
        self.configure(self.ref_unit)

        self.is_connected = True

    def configure(self, ref_unit):
        self.set_reference_unit(ref_unit)

    def tare(self):
        print('TARE DUMMY LOAD CELL')

    def read_weight(self):
        while True:
            try:
                if self.is_connected:
                    yield {'data': random.random()}
                    self.cycle()
                else:
                    yield None

                time.sleep(.1)

            except (KeyboardInterrupt, SystemExit):
                self.exit()

    def set_reference_unit(self, unit):
        print('SET DUMMY LOAD CELL REFERENCE')
        self.ref_unit = unit

    def cycle(self):
        pass
        #print('CYCLING DUMMY LOAD CELL POWER')

    def disconnect(self):
        self.is_connected = False
        print('EXITING DUMMY LOAD CELL')
        