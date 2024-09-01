import argparse
import subprocess
import os
import re

def acquire_data(device, output):
    command = [
        'dd', f'if={device}', f'of={output}', 'bs=4M', 'status=progress'
    ]
    subprocess.run(command)

def create_image(device, output):
    command = [
        'dd', f'if={device}', f'of={output}', 'bs=4M', 'status=progress'
    ]
    subprocess.run(command)

def parse_arguments():
    parser = argparse.ArgumentParser(description="Data Acquisition and Imaging Tool")
    parser.add_argument('--acquire', action='store_true', help="Acquire data from device")
    parser.add_argument('--imaging', action='store_true', help="Create a disk image of device")
    parser.add_argument('device', type=str, help="Device path (e.g., /dev/sda)")
    parser.add_argument('output', type=str, help="Output file (e.g., image.dd)")

    return parser.parse_args()

def show_progress(device):
    size_cmd = ['blockdev', '--getsize64', device]
    total_size = int(subprocess.check_output(size_cmd).strip())
    dd_cmd = ['dd', f'if={device}', 'of=/dev/null', 'bs=4M']
    dd_proc = subprocess.Popen(dd_cmd, stderr=subprocess.PIPE)
    
    for line in dd_proc.stderr:
        match = re.search(r'(\d+) bytes', line.decode())
        if match:
            bytes_copied = int(match.group(1))
            progress = (bytes_copied / total_size) * 100
            print(f'Progress: {progress:.2f}%')

def main():
    args = parse_arguments()

    if args.acquire:
        acquire_data(args.device, args.output)
    elif args.imaging:
        create_image(args.device, args.output)
    else:
        print("Please specify either --acquire or --imaging.")

if __name__ == '__main__':
    main()
