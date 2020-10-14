import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer

class Test_SearchCustomerByName_004:
    baseurl = ReadConfig.getAppURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_searchCustomerByName(self,setup):
        self.logger.info("**Search Customer by Name**")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**Login Successful**")

        self.logger.info("**Starting Search Customer by NAME ***")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickonCustomerMenu()
        time.sleep(1)
        self.addcust.clickonCustomerMenuItem()

        self.logger.info("**Searching Customer by Name")
        searchcust=SearchCustomer(self.driver)
        searchcust.setFirstName("Victoria")
        searchcust.setLastName("Terces")
        searchcust.clickSearch()
        time.sleep(3)
        status=searchcust.searchCustomerByName("Victoria Terces ")
        time.sleep(2)
        assert True==status
        self.logger.info("**TC_Search Customer by Name Finished**")

        self.driver.close()