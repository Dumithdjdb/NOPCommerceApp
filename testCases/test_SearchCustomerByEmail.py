import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.SearchCustomer import SearchCustomer

class Test_SearchCustomerByEmail_004:
    baseurl = ReadConfig.getAppURL()
    username = ReadConfig.getusername()
    password = ReadConfig.getpassword()
    logger = LogGen.loggen()

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("**Searcg Customer by email**")
        self.driver=setup
        self.driver.get(self.baseurl)
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("**Login Successful**")

        self.logger.info("**Starting Search Customer by Email ***")

        self.addcust=AddCustomer(self.driver)
        self.addcust.clickonCustomerMenu()
        time.sleep(1)
        self.addcust.clickonCustomerMenuItem()

        self.logger.info("**Searching Customer by email ID")
        searchcust=SearchCustomer(self.driver)
        searchcust.setEmail("victoria_victoria@nopCommerce.com")
        searchcust.clickSearch()
        time.sleep(3)
        status=searchcust.searchCustomerByEmail("victoria_victoria@nopCommerce.com")
        time.sleep(2)
        assert True==status
        self.logger.info("**TC_Search Customer by email Finished**")

        self.driver.close()