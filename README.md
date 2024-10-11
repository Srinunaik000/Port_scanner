## Port Scanner
A simple Python-based port scanning tool that allows users to scan a target IP address or domain for open, closed, and filtered ports. The tool supports scanning a single port or a range of ports.

### Features
- Scans specific ports or a range of ports on a target IP/domain.
- Identifies whether the port is open, closed, or filtered.
- Provides output based on connection status.

### Prerequisites
- Before running this tool, ensure you have the following installed:
Python 3.x

### Installation
- Clone this repository to your local machine:
- git clone https://github.com/yourusername/Port_scanner.git
- cd Port_scanner

### Install the required dependencies (if any are added in the future):
pip install -r requirements.txt

## Usage
To run the port scanner, use the following syntax:

python main.py scan -t <target-ip/domain> -p <port-range>
Examples:
Scan a single port:

python main.py scan -t 192.168.1.1 -p 80
Scan a range of ports:

python main.py scan -t 192.168.1.1 -p 20-100

## Arguments:
- -t, --target : Specify the target IP address or domain.
- -p, --ports : Specify the port or range of ports to scan (e.g., 80 or 20-100).

## Output
- [+] Port <port> is Open: Indicates that the port is open and accepting connections.
- [-] Port <port> is Closed: Indicates that the port is closed and not accepting connections.
- [?] Port <port> is Filtered: Indicates that the port might be blocked by a firewall or the host is unreachable.

### License
- This project is licensed under the MIT License - see the LICENSE file for details.

