import sys
import subprocess

# Get the file paths from command line arguments
original_path = sys.argv[1]
encoded_path = sys.argv[2]

# Run scripts
subprocess.call(["python3", "psnr.py", original_path, encoded_path ])
subprocess.call(["python3", "ssim.py", original_path, encoded_path ])
subprocess.call(["python3", "pvd.py", original_path, encoded_path ])
