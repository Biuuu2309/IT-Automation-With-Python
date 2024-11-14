import os
import datetime

def file_date(filename):
    # Create the file in the current directory
    with open(filename, 'w') as file:
        pass

    # Get the timestamp of when the file was last modified
    timestamp = os.path.getmtime(filename)

    # Convert the timestamp into a readable format, then into a string
    date = datetime.datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d')

    # Return just the date portion
    return date

print(file_date("newfile.txt"))
# Should be today's date in the format of yyyy-mm-dd
