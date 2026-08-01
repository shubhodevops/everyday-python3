
# try:
#     with open("/home/shubho/Documents/python-everyday/module-11/datafile.txt", "x" , encoding="utf-8") as file:
#         file.write("This is new datafile")
#     print("Data File Created Successfully")
# except FileExistsError:
#     print("Data file alredy exist")

# try:
#     with open("/home/shubho/Documents/python-everyday/module-11/datafile.txt", "r",encoding="utf-8") as file:
#         content=file.read()
#     print(content)
# except FileNotFoundError:
#     print("File Not Found")   


# try:
#     with open("/home/shubho/Documents/python-everyday/module-11/datafile.txt","a", encoding="utf-8") as file:
#         file.write("\nanother line for data file")
#     print("New Line appended")
# except FileNotFoundError:
#     print("File not found")                 


