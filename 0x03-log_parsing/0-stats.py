#!/usr/bin/python3
import sys
import signal

def print_stats(total_size, status_codes):
    print("File size: {}".format(total_size))
    for code in sorted(status_codes):
        print("{}: {}".format(code, status_codes[code]))

def signal_handler(sig, frame):
    print_stats(total_size, status_codes)
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

total_size = 0
status_codes = {}

try:
    for idx, line in enumerate(sys.stdin, 1):
        parts = line.split()
        if len(parts) >= 7:
            ip, date, request, status, size = parts[0], parts[3][1:], parts[5], int(parts[6]), int(parts[7])
            if request == '"GET /projects/260 HTTP/1.1"':
                total_size += size
                if status in [200, 301, 400, 401, 403, 404, 405, 500]:
                    status_codes[status] = status_codes.get(status, 0) + 1
        if idx % 10 == 0:
            print_stats(total_size, status_codes)

except KeyboardInterrupt:
    print_stats(total_size, status_codes)
    sys.exit(0)
