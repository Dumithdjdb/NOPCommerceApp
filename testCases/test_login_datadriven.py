from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen
from Utilities import XLUtils
import time

class Test_002_DDT_Login:

    baseurl=ReadConfig.getAppURL()
    path=".//testData/LoginData.xlsx"
    logger=LogGen.loggen()


    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**Test_002_DDT_Login**")
        self.logger.info("**Verify The Login DDT function**")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)

        self.rows=XLUtils.getRowCount(self.path,'Sheet1')

        # List variable to capture to results of the test

        lst_status=[] # Empty list variable


        for r in range(2,self.rows+1):
            self.username=XLUtils.readData(self.path,'Sheet1',r,1)
            self.password=XLUtils.readData(self.path,'Sheet1',r,2)
            self.expected=XLUtils.readData(self.path,'Sheet1',r,3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(2)

            act_title = self.driver.title
            exp_tile="Dashboard / nopCommerce administration"


            if act_title==exp_tile:
                if self.expected=="Pass":
                    self.logger.info("***Test Passed***" +self.username)
                    self.lp.clickLogout()
                    lst_status.append("Pass")
                elif self.expected=="Fail":
                    self.logger.error("***Test Failed***" +self.username)
                    self.lp.clickLogout()
                    lst_status.append("Fail")
            elif act_title!=exp_tile:
                if self.expected=="Pass":
                    self.logger.error("***Test Failed***" +self.username)
                    lst_status.append("Fail")
                elif self.expected=="Fail":
                    self.logger.info("***Test Passed***" +self.username)
                    lst_status.append("Pass")

        if "Fail" not in lst_status:
            self.logger.info("***Login DDT Test Passed***")
            self.driver.close()
            assert True
        else:
            self.logger.error("***Login DDT Test Failed***")
            self.driver.close()
            assert False

        self.logger.info("***End of DDT Test**")
        self.logger.info("***Completed the Test ***")
