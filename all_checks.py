import os
import sys
import shutil

def check_reboot():
    """returns True, if a computer has a pending reboot"""
    return os.path.exists("run/reboot-required")

def check_disk_full(disk,min_gb, min_percent):
    """Returns True if there isn't enough disk space, False otherwise."""
    du=shutil.disk_usage(disk)
    #Calculate the percentage of free space
    percent_free = 100*du.free / du.total
    # Calculate how many free gigabytes
    gigabytes_free = du.free / 2**30
    if percent_free < min_percent or gigabytes_free < min_gb:
        return True
    return False

def check_root_full():
    """returns True if the root partition is full, False otherwise"""
    return check_disk_full(disk="/",min_gb=2, min_percent=10)

def main():
    checks=[
        (check_reboot,"Pending Reboot"),
        (check_root_full,"Root partition full"),

    ]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)

    print("Everything ok.")
    sys.exit(0)

main()
