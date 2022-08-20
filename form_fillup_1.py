from selenium import webdriver
#import time

web = webdriver.Firefox(executable_path = r'E:\42\geckodriver-v0.31.0-win64\geckodriver.exe')
for a in range(25):
    
    web.get('') # webform hyperlink
    #time.sleep(2)

    ###male
    gender = web.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    gender.click()

    Industry = "Business"
    industry = web.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    industry.send_keys(Industry)

    ###service profit
    service = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    service.click()
    
    ##tenure
    Radio3 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[4]/div/div/div[2]/div[1]/div[3]/label/div/div[1]/div[2]')
    Radio3.click()
    #conflict = often
    Radio4 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[5]/div/div/div[2]/div[1]/div[2]/label/div/div[1]/div[2]')
    Radio4.click()
    Hour = "3"
    hour = web.find_element("xpath",'/html/body/div[1]/div[2]/form/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div/div[1]/input')
    hour.send_keys(Hour)
    #negetive= personal insult
    Radio5 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[7]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]'   )
    Radio5.click()
    #feeling=demotivated
    Radio6 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[8]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    Radio6.click()
    #level = entry
    Radio7 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[9]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    Radio7.click()
    #conflict reason = personality
    Radio8 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[10]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    Radio8.click()
    # manage = everyone
    Radio9 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[11]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    Radio9.click()
    #aware = yes
    Radio10 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[12]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    Radio10.click()
    #provide = yes
    Radio11 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[13]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    Radio11.click()
    #positive = better understanding
    Radio12 = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[2]/div[14]/div/div/div[2]/div[1]/div[1]/label/div/div[1]/div[2]')
    Radio12.click()

    submit = web.find_element("xpath",'/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.click()


web.close()






























