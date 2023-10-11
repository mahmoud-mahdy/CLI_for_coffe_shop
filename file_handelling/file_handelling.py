names = []
dict = {}
num_lines = 0
#reading the file and writing names to list
with open("text.txt", "r") as file:
    for line in file:
        names.append(line.strip())
        
#removing empty items from the list (empty lines)
for item in names:
    if not item:
        names.remove(item)

#counting the repeation for each name
for name in names:
    num_lines += 1
    if name in dict:
        dict[name] += 1
    elif not name in dict:
        dict[name] = 1

#writig the dictionary to the end of the file
with open("text.txt", "r+") as file:
    for _ in range(num_lines):
        file.readline()
    file.write("\n---------------------------------------\n")
    for name, count in dict.items():
        file.write(f"{name}: {count}\n")



#print(names)
#reading
#file = open("text.txt", "r")
#content = file.read()
#print(content)

#overwritting
#file = open("text.txt", "w")
#file.write("text has been written to the file")