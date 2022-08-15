fileName = input("Enter the filename: ")
file_extension = fileName.split(".")
print("The extension of file is "+ repr(file_extension[-1]))