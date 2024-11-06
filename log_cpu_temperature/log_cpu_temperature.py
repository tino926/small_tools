import os
import time

while True:
    # The command to get CPU temperature may vary depending on your OS
    # For example, on Linux, you can use 'sensors' command and parse the output
    # Here, I'm using a placeholder command, replace it with the actual command for your system
    temp = os.popen('sensors | grep "Core 0" | awk \'{print $3}\'').read()

    with open('cpu_temp.txt', 'a') as f:
        f.write(temp + '\n')

    time.sleep(1)
