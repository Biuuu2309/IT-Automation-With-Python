import os
import datetime

print(os.path.getsize("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/ProgrammingLanguage.txt"))
print(os.path.getmtime("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/ProgrammingLanguage.txt"))
timestamp = os.path.getmtime("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/ProgrammingLanguage.txt")
print(datetime.datetime.fromtimestamp(timestamp))
print(os.path.abspath("Python Project/IT-Automation-With-Python/Interact With Operating System/Module 2/ProgrammingLanguage.txt"))