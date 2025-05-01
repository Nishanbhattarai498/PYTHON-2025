# copyfile()=copies content of the file 
# Copy the contents of the file named src to a file named dst.
# The destination file will be created if it does not exist, and it will be truncated if it does.
#copy( ):copy file()+permission mode + destination can be a directory or file
#copy2(): copy()+ copies metadata of the file


import shutil
import os
shutil.copyfile('test.txt','copy.txt')     
