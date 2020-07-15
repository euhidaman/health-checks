import shutil
import sys


def check_disk_usage(disk,min_absolute,min_percent):
    du=shutil.disk_usage(disk)
    #calculate percentage of free space
    percent_free=100*du.free/du.total
    #calculate how many free gigabytes
    gigabytes_free= du.free/2**30
    if percent_free<min_percent or gigabytes_free<min_absolute:
        return False
    return True

#check for atleast 2gb and 10% free
if not check_disk_usage("/",2,10):
    printf("ERROR : Not enough disk space.")
    sys.exit(1)

print("Everything OK.")
sys.exit(0)
