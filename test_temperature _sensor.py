import spidev
from gpiozero import MCP3008
from time import sleep

# Define the MCP3008 object
mcp3008 = MCP3008(channel=1)

# Define a function to read the analog input from the MCP3008
def read_analog_input(channel):
    return mcp3008.value

# Define a function to convert the analog input to temperature in Celsius
def convert_to_celsius(analog_value):
    voltage = analog_value * 5 # Assuming 3.3V as the reference voltage
    temperature_c = (voltage - 0.5) * 100  # Example conversion formula, adjust as per sensor specifications
    return temperature_c

# Calibration offset
calibration_offset = -50  # Example offset to adjust the temperature readings

# Main loop to read and display the temperature
while True:
    analog_value = read_analog_input(1)  # Read analog input from channel 1
    temperature_celsius = convert_to_celsius(analog_value) + calibration_offset  # Apply the calibration offset
    print(f"Temperature: {temperature_celsius:.2f} °C")  # Display the temperature
    sleep(1)  # Optional: Sleep for 1 second before the next reading