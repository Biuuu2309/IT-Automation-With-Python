file = open("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/ProgrammingLanguage.txt")
print(file.readline())
print(file.readline())
print(file.read())
file.close()
with open("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/ProgrammingLanguage.txt") as file:
    print(file.readline())