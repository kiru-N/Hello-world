import shutil
import sys


def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    du_free = du.free / du.total * 100
    return round(du_free)
    
def main():
    if check_disk_usage("/") < 20 :
        print('Not enough space')
        sys.exit(1)
    else:
        print('Everything ok!')
        sys.exit(0)
main()
