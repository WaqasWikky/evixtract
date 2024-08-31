import subprocess

def acquire_data(device, output):
    try:
        subprocess.run(['dd', f'if={device}', f'of={output}', 'bs=4M'], check=True)
        print(f"Data acquisition successful: {output}")
    except subprocess.CalledProcessError as e:
        print(f"Error during acquisition: {e}")

def create_image(device, output):
    try:
        subprocess.run(['dd', f'if={device}', f'of={output}', 'bs=4M'], check=True)
        print(f"Imaging successful: {output}")
    except subprocess.CalledProcessError as e:
        print(f"Error during imaging: {e}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Data Acquisition and Imaging Tool")
    parser.add_argument("--acquire", help="Acquire data from device", action="store_true")
    parser.add_argument("--imaging", help="Create a disk image of device", action="store_true")
    parser.add_argument("device", help="Device path (e.g., /dev/sda)")
    parser.add_argument("output", help="Output file (e.g., image.dd)")

    args = parser.parse_args()

    if args.acquire:
        acquire_data(args.device, args.output)
    elif args.imaging:
        create_image(args.device, args.output)
    else:
        print("Please specify either --acquire or --imaging.")
