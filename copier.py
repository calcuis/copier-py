import shutil
import os

source_file = 'input.png'
output_directory = 'output'
os.makedirs(output_directory, exist_ok=True)

# Copy the file 100 times with names from '0' to '99' / '100' to '199' => for i in range(100, 200):
for i in range(100):
    output_file = os.path.join(output_directory, f"{i}.png") # '000' to '099' => f"{i:03d}.png"
    shutil.copy(source_file, output_file)

print("Copy process completed.")
