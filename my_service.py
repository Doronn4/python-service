import win32serviceutil
import win32service
import servicemanager
import sys

# Import your main script
import main

class MyService(win32serviceutil.ServiceFramework):
    _svc_name_ = 'MyPythonService'
    _svc_display_name_ = 'My Python Service'

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.is_running = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        self.is_running = False

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.is_running = True

        main.main(self)

if __name__ == '__main__':
    if len(sys.argv) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(MyService)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        if sys.argv[1].lower() == 'install':
            try:
                win32serviceutil.InstallService(
                    win32serviceutil.GetServiceClassString(MyService),
                    MyService._svc_name_,
                    MyService._svc_display_name_,
                    startType=win32service.SERVICE_AUTO_START,
                    delayedstart=False
                )
                print(f"Service '{MyService._svc_name_}' installed successfully.")
            except Exception as e:
                print(f"Failed to install service: {str(e)}")
        else:
            # Handle other command-line arguments
            win32serviceutil.HandleCommandLine(MyService)

