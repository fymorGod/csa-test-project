from process import Auto_process
from selenium import webdriver

import time
class Send_form:

    def enviar_formulario(self):

        try:
            self.driver = webdriver.Chrome('D:/anaconda/chromedriver.exe')
            self.driver.get("http://www.csa-ma.com.br/")
            
            self.element = self.driver.find_element_by_xpath('//*[@id="nav-item-1584"]/a/div[2]')
            self.element.click()
            #get to inputs in website
            input_button_name = self.driver.find_element_by_xpath('//*[@id="wpcf7-f1776-o1"]/form/div[2]/div[1]/span[1]/input')
            input_button_name.send_keys("Luiz Fylip")
            time.sleep(3)

            input_button_company = self.driver.find_element_by_xpath('//*[@id="wpcf7-f1776-o1"]/form/div[2]/div[1]/span[2]/input')
            input_button_company.send_keys("Fymorstudios")
            time.sleep(3)

            input_button_fone_number = self.driver.find_element_by_xpath('//*[@id="wpcf7-f1776-o1"]/form/div[2]/div[1]/span[3]/input')
            input_button_fone_number.send_keys('98983124406')
            time.sleep(3)

            input_button_email = self.driver.find_element_by_xpath('//*[@id="wpcf7-f1776-o1"]/form/div[2]/div[1]/span[4]/input')
            input_button_email.send_keys('fymor7@gmail.com')
            time.sleep(3)

            input_button_wbsite = self.driver.find_element_by_xpath('//*[@id="wpcf7-f1776-o1"]/form/div[2]/div[1]/span[5]/input')
            input_button_wbsite.send_keys('Não tenho website')
            time.sleep(3)

            input_text_area_message = self.driver.find_element_by_xpath('//*[@id="txt-contact-page"]')
            input_text_area_message.send_keys('Desejo entrar para equipe e poder ajudar em todo o desenvolvimento e aprender muito com todos.')
            time.sleep(3)

            button_submit_form = self.driver.find_element_by_xpath('//*[@id="contact-page-button-blue"]')
            button_submit_form.click()

            time.sleep(3)
            self.driver.quit()
        except Exception:
            print('LogError: error in process send form')