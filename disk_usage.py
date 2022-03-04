''' Importing all the necessary modules for the program '''
import shutil
import sys
import os


def check_disk_usage(disk,min_gb,min_percent):
    ''' Check for the disk free usage and percentage of disk free.
    Converting the values to GB for the min_gb checks '''
    du = shutil.disk_usage(disk)
    percent_free = du.free / du.total * 100
    free_gb = du.free / 2 ** 30
    if percent_free < min_percent or free_gb < min_gb:
        return True
    return False


def check_root_full():
    return check_disk_usage('/', min_gb=2, min_percent=20)


def check_reboot():
    ''' Returns True if the computer has a pending Reboot. '''
    return os.path.exists('/run/reboot-required')


def main():
    checks=[
        (check_reboot, 'Pending Reboot'),
        (check_root_full, 'Disk Full'),
    ]
    for check, msg in checks:
        if check():
            print(msg)
            sys.exit(1)

    print('Everything ok!')
    sys.exit(0)


main()
