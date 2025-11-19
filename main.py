from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
import time 

steps = ["&step=1&stepname=personalInformation","&step=2&stepname=eeo"]

driver = webdriver.Chrome()
driver.get(f"https://colescareers.com.au/au/en/apply?jobSeqNo=COGRAU172573EXTERNALENAU{steps[0]}") #Website ONLY COLES 
keyboard = Controller()
clickAction = ActionChains(driver)

driverElementsIdAndTexts = {"email": "Example@gmail.com", 
                  "phoneNumber": "0123123123", 
                  "address": "999 Way", 
                  "city": "Claydon", 
                  "postalCode": "3067", 
                  "firstName": "John", 
                  "lastName": "James", 
                  "preferredFirstName": "Lol", 
                  "state": "New South Wales", 
                  "salutation": "Mr.", 
                  "cust_anotherLocation": "Home", 
                  "custAboriginal": "No",
                  "custdisability": "No",
                  "gender": "Man",
                  "cust_workLegally": "Australian Citizen", 
                  "cust_Privacy": "Yes", 
                  "bday": "10081999",                     
                  } #ALL ID ELEMENTS + TEXT 

driverElementsClasses = [".upload-resume-btn.btn.primary-button",".btn.btn-navigate.btn-next"]

for element, text in driverElementsIdAndTexts.items(): 
    inputter = driver.find_element(By.ID, element) 
    

    if element == "bday": 
       clickAction.move_to_element(inputter).click().perform()
       
    inputter.send_keys(text) 

    if element != "bday":
        inputter.submit()
  
for elementClass in driverElementsClasses: # This section is for the RESUME INPUTTER
    time.sleep(2) #I've testing all the Time.sleep and yes you do need them
    inputter = driver.find_element(By.CSS_SELECTOR, elementClass)

    if elementClass == ".upload-resume-btn.btn.primary-button":
        clickAction.move_to_element(inputter).click().perform()
        time.sleep(1)
        keyboard.type("C:\\Users\\e\\e\\e\\Empty Resume.txt") # Resume Path PS: YOU NEED ABSOLUTE PATH
        time.sleep(2)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        time.sleep(4)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    else:
        clickAction.move_to_element(inputter).click().perform()

driverElementsIdAndTexts = {"standard.Cust_StoreMedicalCond": "No",
                            "standard.cust_previousEmp": "No",
                            "standard.cust_CandAvHours": "21-29",
                            "standard.Cust_CurrentStudy": "Not Currently Studying",
                            "standard.Cust_CandLeave.37012": "",
                            "standard.Cust_TypeofEmpNew": "",
                            "standard.Cust_Quals_Lic": "Learners Drivers Permit (L Plates)",
                            "standard.Cust_CandSource": "Google",
                            "standard.Cust_AlterativeStore": "Yes",
                            "standard.Cust_ExpSumary": "",
                            "standard.Cust_BrandPref": "",
                            "standard.Cust_AvailabilityMon": "",
                            "standard.Cust_AvailabilityTues": "",    
                            "standard.Cust_AvailabilityWed": "",     
                            "standard.Cust_AvailabilityThurs": "",
                            "standard.Cust_AvailabilityFri": "",
                            "standard.Cust_AvailabilitySat": "",
                            "standard.Cust_AvailabilitySun": "",                     
                  } #ALL ID ELEMENTS + TEXT for part 2  


driver.get(f"https://colescareers.com.au/au/en/apply?jobSeqNo=COGRAU172573EXTERNALENAU{steps[1]}") # Because its a new websites needs driver to reassign 

def applicationProcedures(timeWorking, type):
    clickAction.move_to_element(inputter).click().perform()

    
    if timeWorking != "":
        keyboard.type(timeWorking)
        time.sleep(0.2)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif type != "":
        keyboard.type(type)
        time.sleep(0.2)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

    

def applicationProceduresTwo(brandPreference, experience):
    inputter.click()
    if brandPreference != "":
        keyboard.type(brandPreference)
        time.sleep(0.5)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        brandPreference = ""
    elif experience != "":
        keyboard.type(experience)
        time.sleep(0.5)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        experience = ""

driverElementsClasses = [".btn.primary-button.btn-submit"]

for element, text in driverElementsIdAndTexts.items():
    inputter = driver.find_element(By.ID, element)  

    if element == "standard.Cust_CandLeave.37012":
        inputter.click()
    
    elif text == "Not Currently Studying":
        clickAction.move_to_element(inputter).click().perform()
        inputter.send_keys(text)
        inputter.submit()
    elif text == "Google":
        clickAction.move_to_element(inputter).click().perform()
        inputter.send_keys(text)
        inputter.submit()
    elif element == "standard.Cust_Quals_Lic":
        inputter.click()

        time.sleep(0.5)
        keyboard.type(text)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif element == "standard.Cust_AlterativeStore":
        clickAction.move_to_element(inputter).click().perform()
        inputter.send_keys(text)
        inputter.submit()
    elif element == "standard.cust_CandAvHours":
        inputter.click()

        time.sleep(0.5)
        keyboard.type(text)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
    elif element == "standard.cust_previousEmp": 
        inputter.click
        inputter.send_keys(text)
        inputter.submit()
    elif element == "standard.Cust_StoreMedicalCond":
        inputter.click
        inputter.send_keys(text)
        inputter.submit()

    while "standard.Cust_Availability" in element:
        applicationProcedures("Stores - Morning (5am - 12pm)", "")
        applicationProcedures("Afternoon (12pm - 6pm)", "")
        applicationProcedures("Stores - Night (6pm - 12am)", "")
        element = ""

    while element == "standard.Cust_BrandPref":
        inputter.click()
        applicationProceduresTwo("Coles Supermarket", "")

        applicationProceduresTwo("Coles group", "")
        applicationProceduresTwo("", "")
        element = ""

    while element == "standard.Cust_ExpSumary":
        applicationProceduresTwo("", "Customer Service")
        applicationProceduresTwo("", "Trolley Collection")

        applicationProceduresTwo("", "")
        element = ""

    while element == "standard.Cust_TypeofEmpNew":
        applicationProcedures("", "Part Time")
        applicationProcedures("", "Full Time")
        applicationProcedures("", "Casual")
        element = ""

for elementClass in driverElementsClasses: 
    inputter = driver.find_element(By.CSS_SELECTOR, elementClass)
    clickAction.move_to_element(inputter).click().perform()

       
print("Do you want to Quit? Yes or No")
answer = input().lower()

if answer == "yes":
    driver.quit()
elif answer == "no":
    time.sleep(360)





