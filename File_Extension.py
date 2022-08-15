import os
file = input("Enter the file name: ")
file_extn = os.path.splitext(file)
file_name = file_extn[0]
file_extension = file_extn[1]
print("File Name is: ",file_name)
print("File Extension is: ",file_extension)
