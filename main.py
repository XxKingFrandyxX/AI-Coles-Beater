from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pynput.keyboard import Key, Controller
import time 

steps = ["&step=1&stepname=personalInformation","&step=2&stepname=eeo"] #applications steps: after careful cosnideration this may be redundant but idk

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
        time.sleep(2)
        keyboard.type("C:\\Users\\Example\\Example\\Example\\Resume.docx") # Resume Path PS: YOU NEED ABSOLUTE PATH
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
                            "standard.Cust_AvailabilityMon": "5am - 12.00pm",
                            "standard.Cust_AvailabilityMon": "12.00pm - 6.00pm",
                            "standard.Cust_AvailabilityMon": "6.00pm - 12.00am",  
                            "standard.Cust_AvailabilityTues": "5am - 12.00pm",
                            "standard.Cust_AvailabilityTues": "12.00pm - 6.00pm",
                            "standard.Cust_AvailabilityTues": "6.00pm - 12.00am",
                            "standard.Cust_AvailabilityWed": "5am - 12.00pm",
                            "standard.Cust_AvailabilityWed": "12.00pm - 6.00pm",
                            "standard.Cust_AvailabilityWed": "6.00pm - 12.00am",     
                            "standard.Cust_AvailabilityThurs": "5am - 12.00pm",
                            "standard.Cust_AvailabilityThurs": "12.00pm - 6.00pm",
                            "standard.Cust_AvailabilityThurs": "6.00pm - 12.00am",
                            "standard.Cust_AvailabilityFri": "5am - 12.00pm",
                            "standard.Cust_AvailabilityFri": "12.00pm - 6.00pm",
                            "standard.Cust_AvailabilityFri": "6.00pm - 12.00am",
                            "standard.Cust_AvailabilitySat": "5am - 12.00pm",
                            "standard.Cust_AvailabilitySat": "12.00pm - 6.00pm",
                            "standard.Cust_AvailabilitySat": "6.00pm - 12.00am",
                            "standard.Cust_AvailabilitySun": "5am - 12.00pm",
                            "standard.Cust_AvailabilitySun": "12.00pm - 6.00pm",
                            "standard.Cust_AvailabilitySun": "6.00pm - 12.00am",
                            "standard.Cust_CurrentStudy": "Not Currently Studying",
                            "standard.Cust_CandLeave.37012": "",
                            "standard.Cust_TypeofEmpNew": "Part Time",
                            "standard.Cust_TypeofEmpNew": "Casual",
                            "standard.Cust_TypeofEmpNew": "Full Time",
                            "standard.Cust_Quals_Lic": "EXAMPLE EXMAPLE",
                            "standard.Cust_CandSource": "Google"
                  } #ALL ID ELEMENTS + TEXT for part 2  

for element, text in driverElementsIdAndTexts.items():
    inputter = driver.find_element(By.ID, element)  

    if element == "standard.Cust_CandLeave.37012":
        clickAction.move_to_element(inputter).click().perform()
    else:
        inputter.send_keys(text)
        inputter.submit()




#basic but can be improved or will be improved 
print("Do you want to Quit? Yes or No")
answer = input().lower()

if answer == "yes":
    driver.quit()
elif answer == "no":
    time.sleep(360)





