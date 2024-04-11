file_path = "C:\\Users\\PC\\Documents\\python-lessons\\File Handling\\sample_data.txt"

# don't forget to add double backslashes - cuz python treats backslashes as a escape character
reader = open(file_path, "r")
# print(reader)
# print(reader.read())

# readline() reads the first line of the text data
# numbers can be passed as parameters to define the # of chars we want to print
# print(reader.readline())
# print(reader.readline(3))

my_file = open("File Handling\\script.py", "w")
my_file.write('print("Im a newly created py script")')
