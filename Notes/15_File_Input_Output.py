<<<<<<< HEAD
"""
# FIle Input/Output means reading a file and writing into file.

# File handling in Databricks:
 %fs = Big data (fs stands for file system or big data file system)
 %sql = SQL
 %scala = Scala
 %r = R
 %sh = Shell script

# fs related commands in big data
 ls - listing files or directories
 mkdir - creating new directories
 put - creating new file
 cp - copying file
 mv - moving file
 rm - removing file
 head - reading file

# to copy file in DBFS (Distributed files system)
 %fs cp "from file" "to file"

# To copy file in Normal file system we need to use file: otherwise it will use dbfc as default file system
 %fs ls file:

# FILE HANDLING
 Primary requirement of file handling of file handling is creating file, reading file
 and writing into existing file. means:
 open a file, Read and write (perform operations) and close the file.

 # Key function for working with files in python is the Open() function.
 # Open() function takes two parameters: filename and mode.

 There are four different methods (modes) for opening a file:
  "r" - Read - Default value. Opens a file for reading, error if the file does not exist
  "a" - Append - Opens a file for appending, creates the file of it does not exists
  "w" - Write - Opens a file for writing, creates the fie if it does not exists.
  "x" - Create - Create the specified file, returns an error if the file exists.
"""

# To check you current directory in python
import os

# Get the current working directory
current_directory = os.getcwd()

print("Current Directory:", current_directory)


=======
"""
# FIle Input/Output means reading a file and writing into file.

# File handling in Databricks:
 %fs = Big data (fs stands for file system or big data file system)
 %sql = SQL
 %scala = Scala
 %r = R
 %sh = Shell script

# fs related commands in big data
 ls - listing files or directories
 mkdir - creating new directories
 put - creating new file
 cp - copying file
 mv - moving file
 rm - removing file
 head - reading file

# to copy file in DBFS (Distributed files system)
 %fs cp "from file" "to file"

# To copy file in Normal file system we need to use file: otherwise it will use dbfc as default file system
 %fs ls file:

# FILE HANDLING
 Primary requirement of file handling of file handling is creating file, reading file
 and writing into existing file. means:
 open a file, Read and write (perform operations) and close the file.

 # Key function for working with files in python is the Open() function.
 # Open() function takes two parameters: filename and mode.

 There are four different methods (modes) for opening a file:
  "r" - Read - Default value. Opens a file for reading, error if the file does not exist
  "a" - Append - Opens a file for appending, creates the file of it does not exists
  "w" - Write - Opens a file for writing, creates the fie if it does not exists.
  "x" - Create - Create the specified file, returns an error if the file exists.
"""

# To check you current directory in python
import os

# Get the current working directory
current_directory = os.getcwd()

print("Current Directory:", current_directory)


>>>>>>> 77a7026290cffc14ad5280317110e1c4e2e6e29e
