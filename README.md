# evixtract

**evixtract** is a command-line tool designed for data acquisition and imaging of storage devices. It ensures the secure collection and preservation of digital evidence.

## Features
- Securely acquire data from storage devices.
- Create bit-by-bit disk images for forensic analysis.
- Optional hashing (MD5, SHA1, SHA256) for integrity verification.
- Progress display during operations.

## Installation

You can clone this repository and use the tool directly:

```bash
git clone https://github.com/yourusername/evixtract.git
cd evixtract
python setup.py install

Usage
Data Acquisition
bash
Copy code
evixtract.py --acquire /dev/sda --output image.dd --hash sha256 --progress
This command will acquire data from /dev/sda and save it as image.dd. It will also calculate a SHA256 hash of the output file and show the progress.

Disk Imaging
bash
Copy code
evixtract.py --imaging /dev/sdb --output image.dd --hash md5 --progress
This command will create a disk image of /dev/sdb, save it as image.dd, and calculate an MD5 hash for verification.
