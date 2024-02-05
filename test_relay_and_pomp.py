from gpiozero import OutputDevice
import time

water_pump_relay = OutputDevice(24,)

def test_relay_and_pump():
    water_pump_relay.on()
    print('Pump is running')
    time.sleep(5)
    water_pump_relay.off()
    print('Pump stopped')

# Call the test function
test_relay_and_pump()