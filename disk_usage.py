''' Importing all the necessary modules for the program '''
import shutil
import sys


def check_disk_usage(disk):
    ''' Check for the disk free usage and percentage of disk free.
    Converting the values to GB for the min_gb checks '''
    du = shutil.disk_usage(disk)
    percent_free = du.free / du.total * 100

    if percent_free < 20:
        return False
    return True


def main():
    if check_disk_usage("/") < 20:
        print('Not enough space')
        sys.exit(1)
    else:
        print('Everything ok!')
        sys.exit(0)


main()
