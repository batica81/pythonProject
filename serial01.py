import serial
import wave


ser = serial.Serial(
    # Serial Port to read the data from
    port='/dev/ttyACM0',

    # Rate at which the information is shared to the communication channel
    baudrate=115200,

    # Applying Parity Checking (none in this case)
    parity=serial.PARITY_NONE,

    # Pattern of Bits to be read
    stopbits=serial.STOPBITS_ONE,

    # Total number of bits to be read
    bytesize=serial.EIGHTBITS,

    # Number of serial commands to accept before timing out
    timeout=1
)
# Pause the program for 1 second to avoid overworking the serial port
while 1:
    x = ser.readline().strip()

    
    print(bytes(x, 'utf-16'))

# with open("output.raw", "rb") as inp_f:
#     data = inp_f.read()
#     with wave.open("sound.wav", "wb") as out_f:
#         out_f.setnchannels(1)
#         out_f.setsampwidth(2) # number of bytes
#         out_f.setframerate(44100)
#         out_f.writeframesraw(data)
#
