import serial
import time

# Set up the serial communication (check which port your Arduino is using)
ser = serial.Serial('COM3', 9600)  # On Windows (check the COM port)
# ser = serial.Serial('/dev/ttyACM0', 9600)  # On Linux

def send_rgb(red, green, blue):
    if 0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255:
        ser.write(bytes([red, green, blue]))
    else:
        print("Values must be between 0 and 255")

while True:
    try:
        # Input values in the format 'green, red,  blue'
        rgb_input = input("Enter the RGB values in the format 'green, red, blue': ")
        red, green, blue = map(int, rgb_input.split(','))
        
        # Send the values to the Arduino
        send_rgb(red, green, blue)
        
        # Add a small delay to allow the Arduino to process the data
        time.sleep(0.1)
    
    except KeyboardInterrupt:
        print("Program interrupted")
        ser.close()
        break
    except ValueError:
        print("Please enter values in the format 'green, red, blue' with integers between 0 and 255.")
    except Exception as e:
        print(f"An error occurred: {e}")
