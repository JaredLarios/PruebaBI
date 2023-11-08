import os
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

import time

script_dir = os.path.dirname(os.path.abspath(__file__))

class SeleniumTest(unittest.TestCase):
    @classmethod
    def setUp(self):
        service  = Service(executable_path=r"E:\Web\driver\geckodriver-v0.33.0-win64\geckodriver.exe" )
        options = webdriver.FirefoxOptions()
        self.driver = webdriver.Firefox(service=service, options=options)


    #@unittest.skip("demonstrating skipping")
    def test_1_elemets(self):
        #1.	Ingresar al módulo “Elements”
        #   a.	Ingresar al apartado de “Check Box”
        #   b.	Presionar el botón “+” ubicado en la parte superior derecha.
        #   c.	Presionar el checkbox de ExcelFile y WordFile, que se encuentra dentro de Documents 
        #       -> Downloads -> ExcelFile/WordFile.
        try:
            driver = self.driver 
            driver.get("https://demoqa.com/")
            self.assertIn("DEMOQA", driver.title)
            
            elements = driver.find_element(By.XPATH ,'//H5[text()="Elements"]')
            elements.click()

            checkbox = driver.find_element(By.XPATH ,'//SPAN[@class="text"][text()="Check Box"]')
            checkbox.click()
            home = driver.find_element(By.XPATH ,'//BUTTON[@aria-label="Toggle"]')
            home.click()
            downloads = driver.find_element(By.XPATH, '(//BUTTON[@aria-label="Toggle"])[4]')
            downloads.click()
            word = driver.find_element(By.XPATH ,'//SPAN[@class="rct-title"][text()="Word File.doc"]')
            word.click()
            excel = driver.find_element(By.XPATH, '//SPAN[@class="rct-title"][text()="Excel File.doc"]')
            excel.click()

            time.sleep(3)

            ## verificacion de reultado 
            # time.sleep(15)
            self.assertTrue(excel.is_enabled())
            self.assertTrue(word.is_enabled())

        finally:
            driver.quit()


    #@unittest.skip('demonstrating skipping')
    def test_2_dynamic_properties(self):
        #2.	Ingresar al apartado de “Dynamic Properties”
        #   a.	Espera a que pasen 5 segundos en lo que se activa el botón
        #   b.	Luego da Click en el mismo
        try:
            driver = self.driver 
            driver.get('https://demoqa.com/checkbox')
            self.assertIn('DEMOQA', driver.title)

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

            dynamic_properties = driver.find_element(By.ID ,'item-8')
            dynamic_properties.click()

            element = driver.find_element(By.ID, 'enableAfter')
            button = driver.find_element(By.ID, 'colorChange')
            button = WebDriverWait(driver, 10).until(
                                                EC.presence_of_element_located(
                                                    (By.CLASS_NAME, 'text-danger')))
            element.send_keys(Keys.RETURN)

            ## verficacion de resultado
            # time.sleep(15)
            color = 'text-danger' in button.get_attribute('class')
            time.sleep(3)
            self.assertTrue(color)

        finally:
            driver.quit()


    
    #@unittest.skip('demonstrating skipping')
    def test_3_web_tables(self):
        #3.	Luego Buscar el apartado de “Web Tables”
        #   a.	Elimina el primer elemento de la tabla
        #   b.	Presiona el botón Add y crear un nuevo registro
        #   c.	Llenar el formulario con los siguientes datos:
        #       Nombre: Juan 
        #       Apellido: Perez
        #       Email: test@test.bi.com.gt
        #		Age: (Tu edad)
        #		Salario: 8000
        #       Departamento: Guatemala

        # possible dict 
        data = {
            'firstName': 'Juan',
            'lastName': 'Perez',
            'userEmail': 'test@test.bi.com.gt',
            'age': '25',
            'salary': '8000',
            'department': 'Guatemala'
        }
        try:
            driver = self.driver 
            driver.get('https://demoqa.com/checkbox')
            self.assertIn("DEMOQA", driver.title)

            web_tables = driver.find_element(By.ID, 'item-3')
            web_tables.click()

            first_delete = driver.find_element(By.ID, 'delete-record-1')
            first_delete.click()

            add_button = driver.find_element(By.ID, 'addNewRecordButton')
            add_button.send_keys(Keys.RETURN)

            for tag, value in data.items():
                input_field = driver.find_element(By.ID, tag)
                input_field.send_keys(value)

            submit = driver.find_element(By.XPATH, '//BUTTON[@id="submit"]')
            submit.send_keys(Keys.RETURN)

            time.sleep(5)
            ## verificacion de reultado 
            # time.sleep(15)
            for value in data.values():
                input_field = driver.find_element(By.XPATH, f'//DIV[@class="rt-td"][text()="{value}"]' )
                self.assertTrue(input_field)
            
            

        finally:
            driver.quit()


    #@unittest.skip('demonstrating skipping')
    def test_4_forms(self):
        #4.	Ingresar al módulo “Forms”
        #   a.	Llenar el formulario con la siguiente información:
        #       i.	Nombre: Tu nombre 
        #       ii.	Apellido: Tu Apellido
        #       iii.	Email: test@test.bi.com.gt
        #       iv.	Mobile: 1234567890
        #       v.	Fecha de nacimiento: Tu fecha de nacimiento
        #       vi.	Subjects: Maths 
        #       vii.	Hobbies: Los que se acoplen más a ti. (Mínimo 1)
        #       viii.	Archivo: Subir un archivo de prueba .txt
        #       ix.	Dirección: Banco Industrial Zona 4. 7ª. Avenida 5-10, Zona 4 Centro Financiero Torre I
        #       x.	Estado: Seleccionar NRC
        #       xi.	Ciudad: Seleccionar Delhi
        #   b.	Enviar el formulario
        #   c.	Cerrar el resumen de formulario éxitoso.
        path = os.path.join(script_dir, "test.txt")
        data = {
            'firstName': 'Jared',
            'lastName': 'Larios',
            'userEmail': 'test@test.bi.com.gt',
            'gender': 'Male', 
            'userNumber': '1234567890',
            'subjectsInput': "Maths",
            'dateOfBirthInput': '09 Oct 1998',
            'hobbies': 'Sports', 
            'uploadPicture': f'{path}',
            'currentAddress': 'Banco Industrial Zona 4. 7ª. Avenida 5-10, Zona 4 Centro Financiero Torre I',
            '3': 'NCR',
            '4': 'Delhi'
        }
        try:
            driver = self.driver
            driver.get('https://demoqa.com/checkbox')
            self.assertIn("DEMOQA", driver.title)

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

            forms = driver.find_element(By.XPATH, '(//DIV[@class="header-text"])[2]')
            forms.click()

            form_practice = driver.find_element(By.XPATH, '//SPAN[@class="text"][text()="Practice Form"]')
            form_practice.click()

            select_buttons = ['gender', 'hobbies']
            select_location = ['3', '4']

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            
            for tag, value in data.items():
                # si son botones de seleccion hace click
                if tag in select_buttons:
                    input_field = WebDriverWait(driver, 10).until(
                                        EC.element_to_be_clickable((By.XPATH, f'//LABEL[text()="{value}"]')))
                    input_field.click()

                # si es el ojeto o motivo lo escribe 
                elif tag == "subjectImput":
                    input_field = driver.find_element(By.ID, tag)
                    input_field.send_keys(value)
                    input_field.send_keys(Keys.RETURN)
                    input_field.send_keys(Keys.RETURN)
                    

                # si es un droptdown menu selecciona la opcion
                elif tag in select_location:
                    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
                    input_field = driver.find_element(
                        By.XPATH, f'(//INPUT[@id="react-select-{tag}-input"])')
                    input_field.send_keys(value)
                    input_field.send_keys(Keys.RETURN)

                # si son campos de text los rellena
                else:
                    input_field = driver.find_element(By.ID, tag)
                    if tag == "dateOfBirthInput": 
                        input_field.send_keys(Keys.CONTROL + 'a')
                        input_field.send_keys(Keys.RETURN)
                    input_field.send_keys(value)

            submit = driver.find_element(By.XPATH, '//BUTTON[@id="submit"]')
            submit.send_keys(Keys.RETURN)

            time.sleep(3)

            close_button = driver.find_element(By.XPATH, '//BUTTON[@id="closeLargeModal"]')
            self.assertTrue(close_button)
            close_button.send_keys(Keys.RETURN)

        finally:
            driver.quit()


    #@unittest.skip('demonstrating skipping')
    def test_5_books(self):
        #5.	Ingresar al módulo “Book Store Aplication”
        #   a.	Ingresar al apartado de “Book Store”
        #   b.	Busca el libro “Understanding ECMAScript 6”
        #   c.	Selecciona el titulo (Esto te moverá a la información del libro)
        #   d.	 Luego selecciona el link en el apartado del website.
        #   e.	Cierra la página del link
        #   f.	Por último regresa con el botón “Back to Store”.
        try:
            driver = self.driver
            driver.get('https://demoqa.com/checkbox')
            self.assertIn("DEMOQA", driver.title)

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

            books = driver.find_element(
                        By.XPATH, '(//DIV[@class="header-text"])[6]')
            books.click()

            book_store = driver.find_element(
                        By.XPATH, '//SPAN[@class="text"][text()="Book Store"]')
            book_store.click()
            
            search = driver.find_element(By.XPATH, '//INPUT[@id="searchBox"]')
            search.send_keys('Understanding ECMAScript 6')

            found_book = driver.find_element(By.XPATH, '//A[text()="Understanding ECMAScript 6"]')
            found_book.click()

            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

            book_link = driver.find_element(
                    By.XPATH, f'//LABEL[@class="form-label"][text()="https://leanpub.com/understandinges6/read"]')

            book_link.click()

            web_title = 'Read Understanding ECMAScript 6 | Leanpub'

            current_window = driver.window_handles[0]
            new_window = driver.window_handles[1]

            time.sleep(5)
            driver.switch_to.window(new_window)

            self.assertEqual(web_title,driver.title)

            time.sleep(3)
            driver.close()

            driver.switch_to.window(current_window)

            back_to_sotre = driver.find_element(By.XPATH, '//BUTTON[@id="addNewRecordButton"]')
            back_to_sotre.send_keys(Keys.RETURN)

            time.sleep(3)


        finally:
            driver.quit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
