from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time 

steps = ["&step=1&stepname=personalInformation","&step=2&stepname=eeo"] #applications steps: after careful cosnideration this may be redundant but idk

driver = webdriver.Chrome()
driver.get(f"https://colescareers.com.au/au/en/apply?jobSeqNo=COGRAU172573EXTERNALENAU{steps[0]}") #Website ONLY COLES 

driverElementsIdAndTexts = {"email": "example@gmail.com", 
                  "phoneNumber": "0123123123", 
                  "address": "999 Way", 
                  "city": "Petersburg", 
                  "postalCode": "8888", 
                  "firstName": "Example", 
                  "lastName": "Example", 
                  "preferredFirstName": "Example", 
                  "state": "New South Wales", 
                  "salutation": "Miss.", 
                  "cust_anotherLocation": "Home", 
                  "custAboriginal": "No",
                  "custdisability": "No",
                  "gender": "Man",
                  "cust_workLegally": "Australian Citizen", 
                  "cust_Privacy": "Yes", 
                  "bday": "10101997"      
                  } #ALL ID ELEMENTS + TEXT 

driverElementsClasses = [".upload-resume-btn.btn.primary-button"]

for element, text in driverElementsIdAndTexts.items(): 

    inputter = driver.find_element(By.ID, element) 
    

    if element == "bday": 
       inputter.click()
       
    inputter.send_keys(text) 

    if element != "bday":
        inputter.submit()
  
for elementClass in driverElementsClasses: # This section is for the RESUME INPUTTER
    time.sleep(2) #I've testing all the Time.sleep and yes you do need them
    inputter = driver.find_element(By.CSS_SELECTOR, elementClass)

    inputter.click()

    keyboard = Controller()
    time.sleep(2)
    keyboard.type("C:\\Users\\Example\\Example\\Example\\Resume.docx") # Resume Path PS: YOU NEED ABSOLUTE PATH
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    time.sleep(2)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)

while True: #basic but can be improved or will be improved 
    print("Do you want to Quit? Yes or No")
    answer = input().lower()

    if answer == "yes":
        driver.quit()
    elif answer == "no":
        time.sleep(360)





