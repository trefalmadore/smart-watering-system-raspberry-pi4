from gpiozero import OutputDevice
import spidev
import time
 
#Title
print("""
 _    _                               _____   _                _        
| |  | |                             |  __ \ | |              | |       
| |__| |  __ _  _ __   _ __   _   _  | |__) || |  __ _  _ __  | |_  ___ 
|  __  | / _` || '_ \ | '_ \ | | | | |  ___/ | | / _` || '_ \ | __|/ __|
| |  | || (_| || |_) || |_) || |_| | | |     | || (_| || | | || |_ \__ \\
|_|  |_| \__,_|| .__/ | .__/  \__, | |_|     |_| \__,_||_| |_| \__||___/
               | |    | |      __/ |                                    
               |_|    |_|     |___/                                     
""")
 
  
spi = spidev.SpiDev()
spi.open(0, 0)

moisture_sensor_channel = 0
temperature_sensor_channel = 1

water_pump_relay = OutputDevice(24, initial_value=False)

def read_mcp3008(channel):
    r = spi.xfer2([1, (8 + channel) << 4, 0])
    adc_value = ((r[1] % 3) << 8) + r[2]
    return adc_value

def convert_to_celsius(adc_value):
    voltage = (adc_value * 5.0 / 1023.0)  # Assuming 5V reference voltage and 10-bit ADC
    temperature_celsius = (voltage - 0.5) * 100  # Example formula for thermistor temperature conversion
    temperature_celsius = min(45, max(-6, round(temperature_celsius)))  # Limit the temperature within a reasonable range
    return temperature_celsius

# Calibrate the temperature sensor
calibration_offset_temperature = 20  # Adjusted calibration offset for the temperature sensor

# Calibrate the moisture sensor
calibration_offset_moisture = 20  # Adjusted calibration offset for the moisture sensor

while True:
    temperature_value = read_mcp3008(temperature_sensor_channel)
    temperature_celsius = convert_to_celsius(temperature_value) + calibration_offset_temperature  # Apply the calibrated temperature offset
    print("\033[94m" + f'Temperature of the room: {temperature_celsius}°C' + "\033[0m")

    moisture_value = read_mcp3008(moisture_sensor_channel) + calibration_offset_moisture  # Apply the calibrated moisture offset
    print("\033[94m" + f"Value of the moisture sensor: {moisture_value}" + "\033[0m")
    
    if moisture_value >= 270:
        water_pump_relay.on()
        print("\033[91m\033[1m" + 'Plants need some water' + "\033[0m")
        time.sleep(3)  # Adjust the watering duration as needed
        water_pump_relay.off()
        moisture_value = 0
    else:
        print("\033[93m\033[1m" + 'Happy Plants' + "\033[0m")

    time.sleep(3600)  # Adjust the interval between readings as needed