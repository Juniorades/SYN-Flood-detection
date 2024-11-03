
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

## Configuration

- **SYN_THRESHOLD**: Adjust the threshold in the code to set the maximum allowable SYN packets per second per IP.

## Testing the IDS

1. Set up a test environment with two machines: one as the target (running this script) and the other as the attacker.
2. On the attacker machine, simulate a SYN flood attack using `nmap`:

   ```bash
   sudo nmap -p 80 --max-rate 1000 -Pn -sS <target_ip>
   ```

3. The IDS should detect the attack and block the attacker's IP.

## Logs

The IDS logs each blocked IP and the time of detection in `log.txt`.

## License

MIT License
