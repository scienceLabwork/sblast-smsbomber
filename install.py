import pip
import time

def mainMessage():
    print('''
             _     _           _   
         ___| |__ | | __ _ ___| |_ 
        / __| '_ \| |/ _` / __| __|
        \__ \ |_) | | (_| \__ \ |_  
        |___/_.__/|_|\__,_|___/\__|.........
                                    
    ''')
    print('Installing.... all required dependencies and libraries...Wait for a while \n>>>')
    time.sleep(3)
    print('>>>Requires 3-4 modules..')
    print("installing all modules under USERS PERMISSION! ")
    time.sleep(2)
    print('>>>Getting modules\n')

mainMessage()

pip.main(['install','selenium'])
print('\nselenium installed successfully\n')
time.sleep(3)
pip.main(['install','webdriver_manager'])
print('\nwebdriver_manager for all webBrowsers installed successfully\n')
time.sleep(2)
print('successfully installed all the modules....\n')
print('Now type Python3 smsBombing.py and sms bomber will start')

