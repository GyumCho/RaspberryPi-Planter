import busio
import digitalio
import board
import time
import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import matplotlib.pyplot as plt

# Create a SPI Bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
cs = digitalio.DigitalInOut(board.CE0)  # Create the chip select
ADC = MCP.MCP3008(spi,cs)  # Create an object for the ADC

# Create an analog input channel on pin 0
LDRChan = AnalogIn(ADC,MCP.P0)

## Setting up the plot
# Create arrays for the plots
t = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
LDR = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

plt.ion()  # Run GUI event loop
figure, ax = plt.subplots(figsize=(10,8))
line1, = ax.plot(t,LDR)

plt.title('LDR connected to Pi')  # Adding a title
# Adding labels
plt.xlabel('Time (ms)')
plt.ylabel('Value of LDR')
plt.ylim(0,65535)

# Plot the table
def Plot():
    # Update the data
    line1.set_xdata(t)
    line1.set_ydata(LDR)
    # Draw
    figure.canvas.draw()

    figure.canvas.flush_events()
    return

while True:
    # Read LRD data
    print('ADC Voltage: ' + str(LDRChan.voltage) + 'V')
    LDR.pop(0)    
    LDR.append(LDRChan.value)

    time.sleep(0.01)