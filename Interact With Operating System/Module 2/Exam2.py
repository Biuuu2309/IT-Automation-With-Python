import os

def new_directory(directory, filename):
  # Before creating a new directory, check to see if it already exists
  if os.path.isdir(directory) == False:
    return

  # Create the new file inside of the new directory
  os.chdir(filename)
  with open (directory, filename) as file:
    pass

  # Return the list of files in the new directory
  return file

print(new_directory("PythonPrograms", "script.py"))