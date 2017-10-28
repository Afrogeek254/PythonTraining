# -*- coding: utf-8 -*-
import unittest

from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import Select

from model.Clases import Contact


def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False


class Add_Contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver(capabilities={"marionette": False})
        self.wd.implicitly_wait(60)
    
    def test_Add_Contact(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/Addressbook/")
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd)
        self.create_contact(wd, Contact(firstname="Test", middlename="Testovich", lastname="Testov", nickname="Testik",
                            title="For python training", company="Big", address="Moscow",
                            home="USSR", mobile="89123456789", work="84951234567", email="test@test.com",
                            email2="test@test.com", email3="Test@test.com", homepage="localhost/Addressbook", bday="5",
                            bmonth="5", byear="1975", aday="5", amonth="5", ayear="2015", address2="Moscow",
                            home2="h.5 f. 35", notes="Test"))
        self.return_homepage(wd)
        self.logout(wd)
        self.assertTrue(success)

    def test_Add_Contact_epty(self):
        success = True
        wd = self.wd
        wd.get("http://localhost/Addressbook/")
        self.login(wd, username="admin", password="secret")
        self.add_new_contact(wd)
        self.create_contact(wd, Contact(firstname="", middlename="", lastname="", nickname="",
                            title="", company="", address="",
                            home="", mobile="", work="", email="",
                            email2="", email3="", homepage="", bday="0",
                            bmonth="0", byear="", aday="0", amonth="0", ayear="", address2="",
                            home2="", notes=""))
        self.return_homepage(wd)
        self.logout(wd)
        self.assertTrue(success)

    def logout(self, wd):
        # Log out
        wd.find_element_by_link_text("Logout").click()

    def return_homepage(self, wd):
        # return to home page
        wd.find_element_by_id("content").click()

    def create_contact(self, wd, contact):
        # fill contact form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("home").click()
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home)
        wd.find_element_by_name("mobile").click()
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").click()
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work)
        wd.find_element_by_name("email").click()
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").click()
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").click()
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").click()
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # Select Birthday date
        Select(wd.find_element_by_name("bday")).select_by_index(contact.bday)
        Select(wd.find_element_by_name("bmonth")).select_by_index(contact.bmonth)
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.byear)
        # Select Anniversary date
        Select(wd.find_element_by_name("aday")).select_by_index(contact.aday)
        Select(wd.find_element_by_name("amonth")).select_by_index(contact.amonth)
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.ayear)
        # Fill Secondary form
        wd.find_element_by_name("address2").click()
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        wd.find_element_by_name("phone2").click()
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.home2)
        wd.find_element_by_name("notes").click()
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # submit contact creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def add_new_contact(self, wd):
        # add new contact
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, username, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def tearDown(self):
        self.wd.quit()


if __name__ == '__main__':
    unittest.main()
