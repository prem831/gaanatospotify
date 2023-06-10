import os

# get current directory to comeback again
cwd = os.getcwd()
print(cwd)
#kjd1111111111
chrome_app_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application"
os.chdir(chrome_app_path)

try:
    os.system('cmd /k "chrome.exe --remote-debugging-port=8989 --user-data-dir=\"E:\\chromedriver\\chromeprofile\""')
except:
    print("cannot execute")
finally:
    print("check what happened")
# getting  back to our directory
os.chdir(cwd)

exit()
