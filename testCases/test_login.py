from selenium import webdriver
import pytest
from pageObjects.LoginPage import LoginPage
from Utilities.readProperties import ReadConfig
from Utilities.customLogger import LogGen

class Test_001_Login:

    baseurl=ReadConfig.getAppURL()
    username=ReadConfig.getusername()
    password=ReadConfig.getpassword()

    logger=LogGen.loggen()



    @pytest.mark.regression
    def test_homepageTitle(self,setup):
        self.logger.info("**Test_001_Login**")
        self.logger.info("**Verify Home Page Title**")

        self.driver=setup
        self.driver.get(self.baseurl)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            self.driver.close()
            assert True
            self.logger.info("** Home Page Title Verificaion Passed**")
        else:
            self.driver.save_screenshot(".\\screenShots\\"+"test_homepageTitle.png")
            self.logger.error("** Home Page Title Verificaion Failed**")
            self.driver.close()
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("**Verify The Login function**")
        self.driver = setup
        self.driver.get(self.baseurl)
        self.lp=LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title=self.driver.title

        if act_title=="Dashboard / nopCommerce administration":
            assert True
            self.driver.close()
            self.logger.info("**Login is successfule and Title Verified**")
        else:
            self.driver.save_screenshot(".\\screenShots\\" + "test_login.png")
            self.driver.close()
            assert False
            self.logger.error("**Login is Failed**")