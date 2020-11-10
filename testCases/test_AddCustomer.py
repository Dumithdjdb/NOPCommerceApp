import string

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
import random



class Test_003_Add_Customer:
    baseurl = ReadConfig.getAppURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    def test_addCustomer(self,setup):
        self.logger.info('***Test003_Add_Customer***')
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info('***Login Syccessful***')

        self.logger.info("***Starting Add Customer Test***")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickonCustomerMenu()
        self.addcust.clickonCustomerMenuItem()
        self.addcust.clickonAddNew()

        self.logger.info("***Providing Customer Info***")
        self.email= random_generator() + "@gmail.com"
        self.addcust.setEmail(self.email)
        self.addcust.setPassword("test123")
        self.addcust.setFirstName("John")
        self.addcust.setLastName("Smith")
        self.addcust.setGender("Male")
        self.addcust.setDOB("07/05/1981")
        self.addcust.setCompanyName("ABC")
        #self.addcust.setNewsLetter("Test store 2")
        #self.addcust.setCustomerRoles("Guests")
        self.addcust.setManagerofVendor("Vendor 2")
        self.addcust.setAdminContent("This is for testing")
        self.addcust.clickOnSave()

        self.logger.info("****Saving Customer Info***")

        self.logger.info("***Add Customer validation Started***")

        self.msg=self.driver.find_element_by_tag_name("body").text

        if 'customer has been added successfully.' in self.msg:
            assert True
            self.logger.info("*** Add Customer Test Passed")
        else:
            self.driver.save_screenshot(".\\screenshots\\" + "test_addCustomer_scr.png")
            self.logger.error("***Add Customer Test Failed")
            assert False

        self.driver.close()
        self.logger.info("**Ending the add customer test")



    def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))