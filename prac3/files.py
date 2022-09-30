
name = input("what is your name?")

file_edit = open(f"{name}.txt", 'w')
print(f"{name}", file=file_edit)
file_edit.close()

file_read = open(f"{name}.txt", 'r')
answer = file_read.readline()
print("Yor name is", answer)
file_read.close()

