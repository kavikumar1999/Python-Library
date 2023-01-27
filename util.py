from sysutil.Stream import StreamDataAnalyser

def CPU_usage():
    cpu=StreamDataAnalyser()
    cpu.get_CPU_util_info()

def Memory_usage():
    memory=StreamDataAnalyser()
    memory.get_Memory_info()

def Disk_usage():
    disk=StreamDataAnalyser()
    disk.get_Disk_info()

def Battery_usage():
    battery=StreamDataAnalyser()
    battery.get_battery_info()

  






        