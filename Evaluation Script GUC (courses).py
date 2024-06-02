import os
from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


PATH1 = r"C:\Users\mozam\Documents\Coding projects\Scripting\msedgedriver.exe";
os.environ['PATH']+= r"C:\Users\mozam\Documents\Coding projects\Scripting\msedgedriver.exe";
driver = webdriver.ChromiumEdge()
url="https://"+"hamza.elshammaa"+":"+"**PASSWORD HERE**"+"@"+"apps.guc.edu.eg/student_ext/Evaluation/EvaluateCourse.aspx";
x=0
i=0  
while (x<20):
    driver.get(url)
    driver.implicitly_wait(10)
    transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_crsIdLst")
    transcriptBTN.click()
    for i in range(x):
        transcriptBTN.send_keys(Keys.DOWN)
        i+=1
    transcriptBTN.send_keys(Keys.ENTER)
    i =0
    driver.implicitly_wait(10)

            

    try:
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_0_1_0").click()   
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_1_1_1").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_2_1_2").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_3_1_3").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_4_1_4").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_5_1_5").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_6_1_6").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_7_1_7").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_8_1_8").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_9_1_9").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_10_1_10").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_11_1_11").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_12_1_12").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_13_1_13").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_14_1_14").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_15_1_15").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_16_1_16").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_17_1_17").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_objRptr_grade_18_1_18").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_RadioButtonList1_2").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_RadioButtonList2_2").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_RadioButtonList3_2").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_pstEvalBtn").click()
        transcriptBTN=driver.find_element(by=By.ID,value="ContentPlaceHolderright_ContentPlaceHoldercontent_crsIdLst")
        x+=1
    except NoSuchElementException:
        x+=1
