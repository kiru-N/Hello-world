''' Importing all the necessary modules for the program '''
import shutil
import sys


def check_disk_usage(disk,min_gb,min_percent):
    ''' Check for the disk free usage and percentage of disk free.
    Converting the values to GB for the min_gb checks '''
    du = shutil.disk_usage(disk)
    percent_free = du.free / du.total * 100
    free_gb = du.free / 2 ** 30
    if percent_free < min_percent or free_gb < min_gb:
        return False
    return True


def main():
    if check_disk_usage('/', min_gb=2, min_percent=10):
        print('Not enough space')
        sys.exit(1)
    print('Everything ok!')
    sys.exit(0)


main()
