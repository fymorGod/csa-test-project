import time
import pandas as pd

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import * 
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Auto_process:

    def iniciar(self):

        self.raspar_posts_do_site()
        self.gerar_scv_dos_posts()
        self.busca_de_tags()

    def raspar_posts_do_site(self):

        try:
            self.driver = webdriver.Chrome('D:/anaconda/chromedriver.exe')
            self.driver.get("http://www.csa-ma.com.br/")

            #click button BLOG
            self.element = self.driver.find_element_by_link_text("BLOG")
            self.element.click()

            #click button 'Main noticias'
            WebDriverWait(self.driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="main"]/div[2]/div[1]/div/div[1]/div[1]/div[4]/div/a')))
            self.button_link = self.driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div/div[1]/div[1]/div[4]/div/a')
            self.gerar_scv_dos_posts()
        except Exception:
            print('Log: error process raspar_posts_do_site')

    def gerar_scv_dos_posts(self):

        try:
            self.busca_de_tags()
            time.sleep(4)
            colunas = ['Titulo', 'Conteudo', 'Data-Postagens','Links']    
            time.sleep(4)
            news = pd.DataFrame(self.lista_dados_post, columns=colunas)
            news.to_excel('teste001.xlsx', index=False)
            time.sleep(4)
            self.driver.quit()
        except:
            pass
    
    def busca_de_tags(self):

        lista_urls_img = []    
        self.lista_dados_post = []
        try:
            for i in range(19):
                self.button_link.click()
                time.sleep(3)
                #get all elements
                post_content = self.driver.find_elements_by_class_name('post-excerpt')
                post_title = self.driver.find_elements_by_class_name('post-title')
                post_date = self.driver.find_elements_by_class_name('post-date')
                url_image = self.driver.find_elements_by_class_name('attachment-post-thumbnail')
                time.sleep(2)

                self.lista_dados_post.append([post_title[i].text, post_content[i].text, post_date[i].text, url_image[i].get_attribute('src')])   
        except:
            pass
            