import os
import time

while True:
    # Get all lines containing 'Core' in the output of 'sensors' command
    cores = os.popen('sensors | grep "Core"').readlines()
    # Extract the temperature from each line and convert to float
    temps = [float(line.split()[2][1:-3]) for line in cores]
    # Get the maximum temperature
    max_temp = max(temps)

    with open('cpu_temp.txt', 'a') as f:
        f.write(str(max_temp) + '\n')

    time.sleep(1)
