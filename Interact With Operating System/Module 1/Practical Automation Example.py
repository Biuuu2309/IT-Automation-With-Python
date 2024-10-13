import shutil
du = shutil.disk_usage("/")
print(du)
print(du.free/du.total*100)
import psutil
print(psutil.cpu_percent(0.1))

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 75

if not check_cpu_usage() or not check_disk_usage("/"):
    print("Error")
else:
    print("Ok")