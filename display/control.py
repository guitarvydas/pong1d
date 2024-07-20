import requests
import sys

def send_command(endpoint):
    response = requests.post(f'http://127.0.0.1:5000/{endpoint}')
    if response.status_code == 200:
        print("Command sent successfully")
    else:
        print("Failed to send command")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python control.py <command>")
        sys.exit(1)

    command = sys.argv[1]

    if command == "start":
        send_command('pos/0')
    elif command.startswith("pos"):
        _, pos = command.split()
        send_command(f'pos/{pos}')
    elif command == "leftBAM":
        send_command('leftBAM')
    elif command == "rightBAM":
        send_command('rightBAM')
    elif command == "winnerL":
        send_command('winnerL')
    elif command == "winnerR":
        send_command('winnerR')
    else:
        print("Unknown command")
