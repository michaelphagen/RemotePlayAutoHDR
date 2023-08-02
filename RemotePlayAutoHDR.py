# This script will watch the steam streaming_log file to determine when user is using remote play, and will turn off HDR
# when remote play is active.  This is because HDR is not supported by steam remote play.

import os
import time
from infi.systray import SysTrayIcon


# Set the path to the streaming_log file
path = "C:\Program Files (x86)\Steam\logs\streaming_log.txt"
global streaming
streaming = False
global Run
Run = True

def toggleHDR(set):
    if set=="on":
        # call .\HDRSwitch.exe --hdr_on -a
        os.system(".\HDRSwitch.exe --hdr_on -a")
    elif set=="off":
        # call .\HDRSwitch.exe --hdr_on -a
        os.system(".\HDRSwitch.exe --hdr_off -a")

def printLog(string):
    print(string)
    with open("RemotePlayAutoHDR.log", "a") as f:
        # write the datetime and string to the log file
        f.write(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + " " + string + "\n")

def watch(): 
    printLog("Starting watch")
    # Open the file
    global Run
    while Run:
        with open(path, 'r') as f:
            # Read the last line
            lines = f.readlines()
            last_line = lines[-1]
            global streaming
            # Check if the last line contains the string "Streaming session started"
            if "Streaming initialized" in last_line and streaming == False:
                printLog("Remote play started")
                streaming = True
                # Run the HDR off script
                toggleHDR("off")
                # Wait 10 seconds
                time.sleep(10)
            elif "Stopped desktop stream" in last_line and streaming == True:
                printLog("Remote play stopped")
                streaming = False
                # Run the HDR on script
                toggleHDR("on")
                # Wait 10 seconds
                time.sleep(1)
            else:
                #print(last_line)
                time.sleep(1)

def openLog(systray):
    # opens RPM.log file in pwd
    os.system("start RemotePlayAutoHDR.log")

def menuBar():
    menu_options = (("Open Log", None, openLog),)
    systray = SysTrayIcon("icon.ico", "RemotePlayAutoHDR", menu_options, on_quit=on_quit_callback)
    systray.start()
    watch()

def on_quit_callback(systray):
    printLog("Exiting")
    global Run
    Run = False

# Auto run the script
if __name__ == '__main__':
    # Start by toggling HDR on
    toggleHDR("on")
    # Start the watch function
    menuBar()