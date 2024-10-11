import argparse
from modules.port_scanner import main as port_scanner_main


def print_banner():
    ascii_art = """
     ____            _     ____                                  
    |  _ \\ ___  _ __| |_  / ___|  ___ __ _ _ __  _ __   ___ _ __ 
    | |_) / _ \\| '__| __| \\___ \\ / __/ _` | '_ \\| '_ \\ / _ \\ '__|
    |  __/ (_) | |  | |_   ___) | (_| (_| | | | | | | |  __/ |   
    |_|   \\___/|_|   \\__| |____/ \\___\\__,_|_| |_|_| |_|\\___|_|   
    """
    print(ascii_art)
    print("Author: SrinuNaik (D3V1L)\n")

def main():
    print_banner()  # Call to print the banner at the start of the script

    parser = argparse.ArgumentParser(description='Bug Bounty Tool')
    subparsers = parser.add_subparsers(dest='command')

    # Port Scanner Command
    port_parser = subparsers.add_parser('scan', help='Run the port scanner')
    port_parser.add_argument('-t', '--target', required=True, help='Target IP Address or Domain Name')
    port_parser.add_argument('-p', '--ports', required=True, help='Port range (e.g., 20-80 or 80)')

    args = parser.parse_args()

    if args.command == 'scan':
        port_scanner_main(args.target, args.ports)

if __name__ == '__main__':
    main()
