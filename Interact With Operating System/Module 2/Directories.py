import os
print(os.getcwd())
os.mkdir("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/new_dir")
os.chdir("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/new_dir")

print(os.getcwd())

# os.mkdir("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/new_dir2")
# os.rmdir("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/new_dir2")

dir = "Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/new_dir"

for name in os.listdir(dir):
    fullname = os.path.join(dir, name)
    if os.path.isdir(fullname):
        print(f'{fullname} is directory')
    else:
        print(f'{fullname} is file')
