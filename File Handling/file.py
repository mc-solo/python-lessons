file_path = "C:\\Users\\PC\\Documents\\python-lessons\\File Handling\\sample_data.txt"


# don't forget to add double backslashes - cuz python treats backslashes as a escape character
reader = open(file_path, "r")
print(reader.read())
