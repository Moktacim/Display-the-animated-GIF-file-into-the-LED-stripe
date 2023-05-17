import cv2
import imageio
import serial
import struct
import time
from PIL import Image

# Open the serial port
ser = serial.Serial('COM3', 115200)

# Load the GIF file
#gif = imageio.mimread('testgif2.gif')
gif = imageio.get_reader('testgif2.gif')
#while True:
# Loop through each frame in the GIF
for frame in gif:
    # Resize the image to fit the LED strip
    img = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    width = img.shape[1]
    height = img.shape[0]
    #print(width,height)
    ratio = width / height
    #ratio = ratio / 10
    #print(ratio)
    led_count = 32
    led_width = int(ratio * led_count)
    led_height =1
    #print(led_width,led_height)
    led_img = cv2.resize(img, (led_width, led_height))
    #print(led_img)

    # To display the image frme
    frame = cv2.resize(img, (500, 160))
    cv2.imshow("frame",frame)
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

    # Convert the image to a list of RGB values
    pixels = led_img.reshape(led_width * led_height, 3)
    #print(pixels)

    # Format the pixel values into a matrix string with a space separator
    pixel_str = ' '.join([f'{p[0]} {p[1]} {p[2]}' for p in pixels])
    #print(pixel_str)
    matrix_str = f'[{pixel_str}]'
    print(matrix_str)
    matrix_str_1 = '0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0'
    matrix_str_2 = f'[{matrix_str_1}]'
    # Send the matrix string to the Arduino
    ser.write(matrix_str.encode())
    #print(matrix_str)
    time.sleep(0.002)

    # Wait for a short delay

ser.write(matrix_str_2.encode())
ser.write(matrix_str_2.encode())
#print(matrix_str_2)
#time.sleep(0.2)