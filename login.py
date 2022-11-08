import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

class RegisterNewUser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = './chromedriver.exe')
        driver = self.driver
        driver.implicitly_wait(15)
        driver.maximize_window()
        driver.get("https://accounts.google.com/AccountChooser/identifier?continue=https%3A%2F%2Faccounts.google.com%2Fo%2Fsaml2%2Fidp%3Ffrom_login%3D1%26zt%3DChRWcHNNSjZBWTlQbC12Q1BOY25LaxIfazF4SHRzS1hqS1Fmd0ktM2lWMU9TaWVuUzZ6MlJCZw%25E2%2588%2599AD98QVYAAAAAY2md_OZCfAdKhehJMzT2MZYZJgobysQz%26as%3Dk99kBdPbAuWTj2ZLXAStjAQ0KmGtf9MEEM3sRYby6dw&ltmpl=popup&btmpl=authsub&scc=1&oauth=1&flowName=GlifWebSignIn&flowEntry=AccountChooser")
        
    def test_login(self):
        driver = self.driver
        email = driver.find_element('id', 'identifierId')
        next_button = driver.find_element('xpath', '//*[@id="identifierNext"]/div/button/span')
        email.send_keys('user') #sacado de 10-minute mail
        next_button.click()
        password = driver.find_element('name', 'password')
        password.send_keys('****') #sacado de 10-minute mail
        next_button2 = driver.find_element('xpath', '//*[@id="passwordNext"]/div/button/span')
        next_button2.click()
        
        #sleep(5)
        courses=driver.find_element('xpath','//*[@id="global_nav_courses_link"]/div[1]')
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#global_nav_courses_link > div.menu-item-icon-container')))
        courses.click()
        
        six=driver.find_element('xpath','//*[@id="nav-tray-portal"]/span/span/div/div/div/div/div/ul[1]/li[6]/a')
        six.click()
        #sleep(2)
        grades_six=driver.find_element('xpath','//*[@id="section-tabs"]/li[5]/a')
        grades_six.click()
        #sleep(5)
        table_data=[[] for i in range(15)]
        

        for i in range(14):
            names=driver.find_element('xpath',f'//*[@id="gradebook_grid"]/div[2]/div[4]/div/div[{i+1}]/div/div[1]/a')
                                               #'//*[@id="gradebook_grid"]/div[2]/div[4]/div/div[2]/div/div[1]/a'
            table_data[i].append(names.text)
            for j in range(3):
                guias=driver.find_element('xpath',f'//*[@id="gradebook_grid"]/div[3]/div[4]/div/div[{i+1}]/div[{j+1}]/div/div[2]/span')
                                                    #//*[@id="gradebook_grid"]/div[3]/div[4]/div/div[1]/div[1]/div/div[2]/span
                                                    #//*[@id="gradebook_grid"]/div[3]/div[4]/div/div[1]/div[2]/div/div[2]/span
                                                    #//*[@id="gradebook_grid"]/div[3]/div[4]/div/div[5]/div[1]/div/div[2]/span  cambio de guias
                                                    #//*[@id="gradebook_grid"]/div[3]/div[4]/div/div[2]/div[2]/div/div[2]/span   otra estudiante
                table_data[i].append(guias.text)
                
            
        print(table_data)

    def tearDown(self):
        self.driver.implicitly_wait(3)
        self.driver.close()

if __name__ == "__main__":
	unittest.main(verbosity = 2)