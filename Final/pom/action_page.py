from selenium.webdriver.common.by import By
from pom.base_page import BasePage
import time

class DemoPage(BasePage):
    URL = "https://tdd-detroid.onrender.com/"
    
    STUDENT_NAME_INPUT = (By.ID, "student-nome")
    STUDENT_BTN = (By.ID, "student-btn")
    COURSE_NAME_INPUT = (By.ID, "course-nome")
    COURSE_BTN = (By.ID, "course-btn")
    STUDENT_ID_SUBSCRIBE_COURSE_INPUT     = (By.ID, "student-id")
    COURSE_ID_SUBSCRIBE_ALUNO_INPUT    = (By.ID, "course-id")
    STUDENT_SUBSCRIBE_COURSE_BTN = (By.XPATH, "/html/body/div[1]/div[1]/div[4]/button")
    DISCIPLINE_NAME_INPUT = (By.ID, "discipline-nome")
    COURSE_DISCIPLINE_ID_INPUT = (By.ID, "course-discipline-id")
    ADD_DISCIPLINE_BTN = (By.XPATH, "/html/body/div[1]/div[1]/div[5]/button")

    STUDANT_ID_SUBSCRIBE_DISCIPLINE_INPUT = (By.ID, "subscribe-student-id")  
    SUBSCRIBE_DISCIPLINE_ID_INPUT = (By.ID, "subscribe-discipline-id")
    MESSAGE_OUTPUT = (By.CSS_SELECTOR, ".py-p")
    SUBSCRIBE_STUDENT_DISCIPLINE_BTN = (By.XPATH, "/html/body/div[1]/div[1]/div[6]/button")


    def open(self):        
        self.driver.get(self.URL)
        time.sleep(5)

    def add_student(self, name):
        self.enter_text(self.STUDENT_NAME_INPUT, name)
        self.click(self.STUDENT_BTN)

    def add_course(self, name):
        self.enter_text(self.COURSE_NAME_INPUT, name)
        self.click(self.COURSE_BTN)

    def add_discipline(self, name, course_id):
        self.enter_text(self.DISCIPLINE_NAME_INPUT, name)
        self.enter_text(self.COURSE_DISCIPLINE_ID_INPUT, course_id)
        self.click(self.ADD_DISCIPLINE_BTN)

    def subscribe_student(self, student_id, discipline_id):
        self.enter_text(self.STUDANT_ID_SUBSCRIBE_DISCIPLINE_INPUT, student_id)
        self.enter_text(self.SUBSCRIBE_DISCIPLINE_ID_INPUT, discipline_id)
        self.click(self.SUBSCRIBE_STUDENT_DISCIPLINE_BTN)

    def subscribe_student_to_course(self, student_id, discipline_id):
        self.enter_text(self.STUDENT_ID_SUBSCRIBE_COURSE_INPUT, student_id)
        self.enter_text(self.COURSE_ID_SUBSCRIBE_ALUNO_INPUT, discipline_id)
        self.click(self.STUDENT_SUBSCRIBE_COURSE_BTN)

    def get_message(self):
        time.sleep(1)
        return self.get_text(self.MESSAGE_OUTPUT)
