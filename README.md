### file copier

The provided Python code utilizes the `shutil` and `os` modules to create copies of a specified source file (i.e., input.png) and save them into a designated output directory (output). The script ensures the existence of the output directory by creating it if it does not already exist.

The primary functionality of the code is to iterate through a range of numbers from 0 to 99 (inclusive) and create individual copies of the source file, naming them with a numerical index (e.g., "0.png", "1.png", ..., "99.png"). Each copy is saved in the specified output directory.

Upon completion of the copying process, a message is printed to the console, indicating that the copy process has been successfully completed.

In summary, the code automates the generation of multiple copies of a given source file with sequentially numbered filenames and organizes them in a specified output directory. This could be useful, for example, in scenarios where batch processing or duplication of files is required.

#### possible modification(s):
##### copy the file 100 times with names from '000' to '099' (original)
```
for i in range(100):
```
##### copy the file 100 times with names from '100' to '199'
```
for i in range(100, 200):
```
##### copy the file 100 times with names from '200' to '299'
```
for i in range(200, 300):
```
etc.
