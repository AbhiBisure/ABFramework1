from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    NAME=(By.XPATH,"//input[@name='name']")
    EMAIL=(By.XPATH,"//input[@name='email']")
    PASSWORD= (By.CSS_SELECTOR,"input[placeholder='Password']")
    ICECREAMS=(By.ID,"exampleCheck1")
    STUDENT=(By.XPATH,"//label[text()='Student']")
    EMPLOYED = (By.XPATH, "//label[text()='Employed']")
    GENDER= (By.ID,"exampleFormControlSelect1")
    SUBMIT=(By.XPATH,"//input[@type='submit']")
    SUCCESSFULL_SUBMITED_MESSAGE= (By.CLASS_NAME,"alert")
    DATE=(By.XPATH,"//label[text()='Date of Birth']/../input[@class ='form-control']")

    def enter_name(self,name):
        self.logger.info(f"Entering name: {name}")
        self.send_keys(self.NAME,name)

    def enter_email(self, email):
        self.send_keys(self.EMAIL, email)

    def enter_password(self, password):
        self.send_keys(self.PASSWORD, password)

    def love_icecream(self, yes_or_no):
        if yes_or_no == True:
            self.click(self.ICECREAMS)

    def select_employee_status(self,status):
        if status == "Student":
            self.click(self.STUDENT)
        elif status == "Employed":
            self.click(self.EMPLOYED)

    def select_gender(self,gender):
        if gender == "Male":
            self.select_dropdown_value(self.GENDER,"Male")

        elif gender == "Female":
            self.select_dropdown_value(self.GENDER,"Female")

    def submit(self):
        self.click(self.SUBMIT)

    def success_text(self):
        return self.get_text(self.SUCCESSFULL_SUBMITED_MESSAGE)

    def fill_full_form(self,data):
        self.logger.info(f"Registering user: {data['name']}")
        self.enter_name(data["name"])
        self.enter_email(data["email"])
        self.enter_password(data["password"])
        self.love_icecream(data["love_ice_creams"])
        self.select_employee_status(data["employment_status"])
        self.select_gender(data["gender"])
        self.submit()


