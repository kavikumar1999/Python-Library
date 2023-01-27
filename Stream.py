import os.path
import psutil
import json
from datetime import datetime as dt


class StreamDataAnalyser:
    def __init__(self):
        self.Current_CPU_utilization=[]
        self.Current_per_CPU_utilization=[]
        self.current_date_time=[]
        self.current_battery_percent=[]
        self.battery_plugged_status=[]
        self.Total_Memory=[]
        self.Available_Memory=[]
        self.Used_Memory=[]
        self.Memory_usage=[]
        self.Total_Disk=[]
        self.Available_Disk=[]
        self.used_Disk=[]
        self.Disk_usage=[]

    def get_path(temp,path,list):
            list.append(temp)
            with open(path,"w") as file:
                file.writelines(json.dumps(list))


    def get_CPU_util_info(self):
            try:
                folderName=input("Enter a file path to save CPU util info:")
                fileName='CPU_info.json'
                path=os.path.join(folderName,fileName)
                list=[]
                while True:
                    datetime = dt.now()
                    self.current_date_time.append(datetime.strftime("%Y-%m-%d,%H:%M:%S"))
                    self.Current_CPU_utilization.append(f'{psutil.cpu_percent(interval=1)}%')
                    self.Current_per_CPU_utilization.append(f'{psutil.cpu_percent(interval=1, percpu=True)}%')
                    '''while appending , the pairs appending to the single key .by accessing [-1] index
                    we can access the single pair and next pair appending in the next execution key.
                    '''
                    temp={
                        'executed_time':self.current_date_time[-1],
                        'current_cpu_utilization': self.Current_CPU_utilization[-1],
                        'current_per_cpu_utilzation': self.Current_per_CPU_utilization[-1]
                        }
                    StreamDataAnalyser.get_path(temp,path,list) 
                    print(temp)
            except Exception as ex:
                print(ex)    

    def get_Memory_info(self):
            try:
                folderName=input("Enter a file path to save Memory info:")
                fileName='Memory_info.json'
                path=os.path.join(folderName,fileName)
                list=[]
                while True:
                    
                    datetime = dt.now()
                    self.current_date_time.append(datetime.strftime("%Y-%m-%d,%H:%M:%S"))
                    #Rounding the whole number as a GB from Bytes
                    self.Total_Memory.append(f'{round(psutil.virtual_memory().total/1000000000, 2)}GB')
                    self.Available_Memory.append(f'{round(psutil.virtual_memory().available/1000000000, 2)}GB')
                    self.Used_Memory.append(f'{round(psutil.virtual_memory().used/1000000000, 2)}GB')
                    self.Memory_usage.append(f'{psutil.virtual_memory().percent}%')
                    temp={
                        'executed_time':self.current_date_time[-1],
                        'total_memory': self.Total_Memory[-1],
                        'used_memory': self.Used_Memory[-1],
                        'availabe_memory':self.Available_Memory[-1],
                        'memory_usage':self.Memory_usage[-1]
                        }
                    StreamDataAnalyser.get_path(temp,path,list)
                    print(temp)
            except Exception as ex:
                print(ex)  

    def get_Disk_info(self):
            try:
                folderName=input("Enter a file path to save Disk info:")
                fileName='Disk_info.json'
                path=os.path.join(folderName,fileName)
                list=[]
                while True:
                    datetime = dt.now()
                    self.current_date_time.append(datetime.strftime("%Y-%m-%d,%H:%M:%S"))
                    Path_for_psutil='/'
                    self.Total_Disk.append(f'{round(psutil.disk_usage(Path_for_psutil).total/1000000000,2)}GB')
                    self.used_Disk.append(f'{round(psutil.disk_usage(Path_for_psutil).used/1000000000,2)}GB')
                    self.Available_Disk.append(f'{round(psutil.disk_usage(Path_for_psutil).free/1000000000,2)}GB')
                    self.Disk_usage.append(f'{psutil.disk_usage(Path_for_psutil).percent}%')
                    temp={
                        'executed_time':self.current_date_time[-1],
                        'total_disk': self.Total_Disk[-1],
                        'used_disk': self.used_Disk[-1],
                        'availabe_disk':self.Available_Disk[-1],
                        'disk_usage':self.Disk_usage[-1]
                        }
                    StreamDataAnalyser.get_path(temp,path,list)  
                    print(temp)
            except Exception as ex:
                print(ex)  

    def get_battery_info(self):
            try:
                folderName=input("Enter a file path to save Battery info:")
                fileName='Battery_info.json'
                path=os.path.join(folderName,fileName)
                list = []
                while True:
                    datetime = dt.now()
                    self.current_date_time.append(datetime.strftime("%Y-%m-%d,%H:%M:%S"))
                    battery = psutil.sensors_battery()
                    plugged = battery.power_plugged
                    self.current_battery_percent.append(f'{battery.percent}%')
                    self.battery_plugged_status.append("Plugged In" if plugged else "Not Plugged In")
                    temp={
                        'executed_time':self.current_date_time[-1],
                        'current_battery(%)': self.current_battery_percent[-1],
                        'battery_plugged_status': self.battery_plugged_status[-1]
                        }   
                    StreamDataAnalyser.get_path(temp,path,list)
                    print(temp)
            except Exception as ex:
                print(ex)                                       
              

    
      


        