#!/usr/bin/python3
import sys
import signal


# Initialize variables
total_file_size = 0
status_code_counts = {
    200: 0, 301: 0, 400: 0, 401: 0, 
    403: 0, 404: 0, 405: 0, 500: 0
}
line_count = 0

def print_stats():
    """Prints the statistics."""
    print("File size: {}".format(total_file_size))
    for code in sorted(status_code_counts.keys()):
        if status_code_counts[code] > 0:
            print("{}: {}".format(code, status_code_counts[code]))

def signal_handler(sig, frame):
    """Handles the keyboard interruption signal (CTRL + C)."""
    print_stats()
    sys.exit(0)

# Set up the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        try:
            # Split and validate the line format
            parts = line.split()
            if len(parts) < 7:
                continue
            
            ip = parts[0]
            date = parts[3][1:] + " " + parts[4][:-1]
            request = parts[5] + " " + parts[6] + " " + parts[7]
            status_code = int(parts[-2])
            file_size = int(parts[-1])
            
            # Ensure the line matches the expected format
            if request != '"GET /projects/260 HTTP/1.1"':
                continue
            
            # Update total file size and status code counts
            total_file_size += file_size
            if status_code in status_code_counts:
                status_code_counts[status_code] += 1
            
            # Increment the line count
            line_count += 1

            # Print statistics every 10 lines
            if line_count % 10 == 0:
                print_stats()
                
        except (IndexError, ValueError):
            continue

except KeyboardInterrupt:
    # Print statistics on keyboard interruption
    print_stats()
    sys.exit(0)
