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
        time.sleep(2)
        keyboard.type("C:\\E\\E\\E\\E\\Resume.docx") # Resume Path PS: YOU NEED ABSOLUTE PATH
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
                            "standard.Cust_TypeofEmpNew": "Part Time",
                            "standard.Cust_TypeofEmpNew": "Casual",
                            "standard.Cust_TypeofEmpNew": "Full Time",
                            "standard.Cust_Quals_Lic": "EXAMPLE EXMAPLE",
                            "standard.Cust_CandSource": "Google",
                            "standard.Cust_AlterativeStore": "Yes",
                            "standard.Cust_ExpSumary": "Customer Service",
                            "standard.Cust_ExpSumary": "Trolley Collection",
                            "standard.Cust_BrandPref": "Coles Supermarket",
                            "standard.Cust_BrandPref": "Coles group",
                            "standard.Cust_AvailabilityMon": "",
                            "standard.Cust_AvailabilityMon": "",  
                            "standard.Cust_AvailabilityTues": "",
                            "standard.Cust_AvailabilityWed": "",     
                            "standard.Cust_AvailabilityThurs": "",
                            "standard.Cust_AvailabilityFri": "",
                            "standard.Cust_AvailabilitySat": "",

                            "standard.Cust_AvailabilitySun": "",                     
                  } #ALL ID ELEMENTS + TEXT for part 2  


driver.get(f"https://colescareers.com.au/au/en/apply?jobSeqNo=COGRAU172573EXTERNALENAU{steps[1]}") # Because its a new websites needs driver to reassign 

for element, text in driverElementsIdAndTexts.items():
    inputter = driver.find_element(By.ID, element)  


    while "standard.Cust_Availability" in element:
        morning = "Stores - Morning (5am - 12pm)"
        afternoon = "Afternoon (12pm - 6pm)"
        night = "Stores - Night (6pm - 12am)"

        clickAction.move_to_element(inputter).click().perform()
        
        keyboard.type(morning)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        clickAction.move_to_element(inputter).click().perform()

        keyboard.type(afternoon)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        clickAction.move_to_element(inputter).click().perform()

        keyboard.type(night)
        keyboard.press(Key.down)
        keyboard.release(Key.down)
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)

        element = ""

   
    
    if element == "standard.Cust_CandLeave.37012":
        inputter.click()
    
    if text == "Not Currently Studying":
        clickAction.move_to_element(inputter).click().perform()
        inputter.send_keys(text)
        inputter.submit()

    if text == "Google":
        clickAction.move_to_element(inputter).click().perform()
        inputter.send_keys(text)
        inputter.submit()

    # if text == "Customer Service": #NEEDS MORE FIXING FUCKING SHITBOX CODE I'VE SPENT HOURS ON THIS CRAP FOR IT TO FUCK ME IN THE WORSE WAY IMAGINABLE
    #     clickAction.move_to_element(inputter).click().perform()
        
    #     keyboard.type("Customer Service")
    #     time.sleep(1)
    #     keyboard.press(Key.down)
    #     keyboard.release(Key.down)
    #     keyboard.press(Key.enter)
    #     keyboard.release(Key.enter)

    #     keyboard.type("Trolley Collection")
    #     time.sleep(1)
    #     keyboard.press(Key.down)
    #     keyboard.release(Key.down)
    #     keyboard.press(Key.enter)
    #     keyboard.release(Key.enter)


        





#basic but can be improved or will be improved 
print("Do you want to Quit? Yes or No")
answer = input().lower()

if answer == "yes":
    driver.quit()
elif answer == "no":
    time.sleep(360)





