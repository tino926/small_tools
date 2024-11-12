# CPU Temperature Logger

This is a simple Python script designed to log the maximum CPU temperature at regular intervals. The script will append the current timestamp and the maximum CPU temperature to a text file (`cpu_temp.txt`).

## Prerequisites

- Python 3.x
- `sensors` command-line utility (you can install it using your package manager)

## Installation

1. Clone the repository or download the script.
2. Make sure the script has execute permissions. If not, you can set them using the following command:

   ```bash
   chmod +x log_cpu_temperature.py
   ```

## Usage

Run the script with the following command:

```bash
python log_cpu_temperature.py
```

The script will continuously log the maximum CPU temperature every second.

## Configuration

You can configure the script by modifying the following variables at the beginning of the script:

- `MAX_AGE`: The maximum age of data to keep in the log file (in seconds). Default is 10 seconds.
- `CHECK_INTERVAL`: The number of iterations between checks for old data. Default is 60 iterations (i.e., every minute).

## Output

The script will create a `cpu_temp.txt` file in the same directory. Each line in the file will have the following format:

```
YYYY-MM-DD HH:MM:SS: temperature
```

Where `YYYY-MM-DD HH:MM:SS` is the timestamp and `temperature` is the maximum CPU temperature in degrees Celsius.

