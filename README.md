
# Simple Intrusion Detection System (IDS) for SYN Flood Attack Detection

This project is a basic IDS that detects SYN flood attacks by monitoring incoming SYN packets. If an IP sends SYN packets above a specified threshold, the system blocks the IP using `iptables` and logs the event.

## Requirements

- Python 3.x
- Root privileges (required to manipulate `iptables` and capture raw packets)
- Linux environment

## Installation

1. Ensure Python 3.x is installed.
2. Run the script with root privileges.

## Usage

Execute the script with:
```bash
sudo python3 simple_ids_no_comments.py
```

The script monitors incoming SYN packets and blocks any IP that exceeds the defined SYN threshold.

## Logs

The IDS logs each blocked IP and the time of detection in `log.txt`.

## License

MIT License
