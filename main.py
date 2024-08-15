import subprocess
import re
import time

def ping(host):
    # Run the ping command
    process = subprocess.Popen(["ping", "-c", "4", host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = process.communicate()

    # Extracting ping results using regular expressions
    match = re.search(r"(\d+\.\d+) ms", output)
    if match:
        return float(match.group(1))
    else:
        return None

def main():
    host = input("Enter the host to ping: ")
    log_file = input("Enter the log file name: ")

    with open(log_file, 'w') as file:
        file.write("Timestamp, Ping Result (ms)\n")

        try:
            while True:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                result = ping(host)

                if result is not None:
                    print(f"{timestamp} - Ping Result: {result} ms")
                    file.write(f"{timestamp}, {result}\n")
                else:
                    print(f"{timestamp} - Ping failed.")

                time.sleep(0.5)  # Wait for 0.5 second before the next ping (Probably too often if I continue to run this)
        except KeyboardInterrupt:
            print("\nPing testing stopped. Results saved to", log_file)

if __name__ == "__main__":
    main()
