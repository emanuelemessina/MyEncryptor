import os
import win32service  
import win32serviceutil  
import win32event 

class EncryptorService(win32serviceutil.ServiceFramework):  
    
    _svc_name_ = "MyEncryptor" # NET service name      
    _svc_display_name_ = "MyEncryptor" # SCM name  
    _svc_description_ = "A friendly discouragement service" # SCM desc
      
    def __init__(self, args):  
        win32serviceutil.ServiceFramework.__init__(self,args)        
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)  # Create stop request event listener
      
    # Core    
    def SvcDoRun(self):
        
        encrypt_path = "D:\Documents\Documents"

        file = open(os.path.join(encrypt_path, "service.txt"), "r+")
        file.write("ciao")  
 
        file.close() 

        #os.system('"' + sys.executable + '" ' + os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])), 'WinService.py') + ' remove')
        
    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)  

if __name__ == '__main__':  
    win32serviceutil.HandleCommandLine(EncryptorService) 