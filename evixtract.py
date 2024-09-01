import argparse
import subprocess

def acquire_data(device, output):
    command = ['dd', f'if={device}', f'of={output}', 'bs=4M']
    subprocess.run(command)

def create_image(device, output):
    command = ['dd', f'if={device}', f'of={output}', 'bs=4M']
    subprocess.run(command)

def main():
    parser = argparse.ArgumentParser(description="Data Acquisition and Imaging Tool")
    parser.add_argument('--acquire', action='store_true', help="Acquire data from device")
    parser.add_argument('--imaging', action='store_true', help="Create a disk image of device")
    parser.add_argument('device', type=str, help="Device path (e.g., /dev/sda)")
    parser.add_argument('output', type=str, help="Output file (e.g., image.dd)")

    args = parser.parse_args()

    if args.acquire:
        acquire_data(args.device, args.output)
    elif args.imaging:
        create_image(args.device, args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
