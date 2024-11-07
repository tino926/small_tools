import os
import time
import datetime

# Define the maximum age of data to keep (in seconds)
# MAX_AGE = 72 * 60 * 60
MAX_AGE = 10

# Define the number of iterations between checks for old data
CHECK_INTERVAL = 60

# Initialize the counter variable
counter = 0

while True:
    # Get all lines containing 'Core' in the output of 'sensors' command
    cores = os.popen('sensors | grep "Core"').readlines()
    # Extract the temperature from each line and convert to float
    temps = [float(line.split()[2][1:-3]) for line in cores]
    # Get the maximum temperature
    max_temp = max(temps)
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open('cpu_temp.txt', 'a') as f:
        f.write(f"{timestamp}: {max_temp}\n")

    print(f"Max CPU Temperature: {max_temp}°C  ", end='\r')

    # Check for and remove old data if necessary
    if counter % CHECK_INTERVAL == 0:
        now = time.time()
        with open('cpu_temp.txt', 'r') as f:
            lines = f.readlines()
        with open('cpu_temp.txt', 'w') as f:
            for line in lines:
                timestamp, temp = line.split(':', 1)
                timestamp = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                if (now - timestamp.timestamp()) < MAX_AGE:
                    f.write(line)

    # Increment the counter variable
    counter += 1

    time.sleep(1)
