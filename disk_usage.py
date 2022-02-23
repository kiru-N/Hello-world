import shutil

def check_disk_usage(disk):
    du = shutil.disk_usage(disk)
    du_free = du.free / du.total * 100
    print(round(du_free))
    
check_disk_usage("/")
