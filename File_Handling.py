f=open("demofile.txt")
print(f.read())   # read whole file
print(f.read(5)) # read 5 characters
print(f.readline()) # read a line
#open from a directory
f = open("C:\welcome.txt", "r")
print(f.read())
# Using loop for reading file
f = open("demofile.txt", "r")
for x in f:
  print(x)
f.close()

#File write and read
f1 = open("demofile.txt", "r")  # Open the source file in read mode
f = open("demofile2.txt", "w")  # Open the destination file in write mode

f.write(f1.read())  # Write the content of f1 to f
f1.close()  # Close the source file

f.close()  # Close the destination file after writing

# Reopen the destination file in read mode to print its contents
f = open("demofile2.txt", "r")
print(f.read())  # Read and print the contents of the file
f.close()  # Close the destination file

