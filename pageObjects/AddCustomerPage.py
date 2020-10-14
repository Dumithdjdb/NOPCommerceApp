import time
from selenium.webdriver.support.ui import Select
from selenium import webdriver

class AddCustomer:
    lnkCustomers_menu_xpath="//a[@href='#']//span[contains(text(),'Customers')]"
    lnkCustomers_menuitem_xpath="//span[@class='menu-item-title'][contains(text(),'Customers')]"
    btnAddNew_xpath="//a[@class='btn bg-blue']"

    txtEmail_xpath="//input[@id='Email']"
    txtPassword_xpath="//input[@id='Password']"
    txtFirstName_xpath="//input[@id='FirstName']"
    txtLastName_xpath="//input[@id='LastName']"
    rdMaleGender_id='Gender_Male'
    rdFemaleGender_ID='Gender_Female'
    txtdob_xpath="//input[@id='DateOfBirth']"
    txt_companyname_xpath="//input[@id='Company']"
    txt_newsletter_xpath="//ul[@id='SelectedNewsletterSubscriptionStoreIds_taglist']"
    listitemNewsLetter_xpath="//li[contains(text()),'Test store 2']"
    chk_isTaxExempt_xpath="//input[@id='IsTaxExempt']"
    txtCustomerRoles_xpath="//div[@class='k-multiselect-wrap k-floatwrap']//ul[@id='SelectedCustomerRoleIds_taglist']"
    listitemAdministrator_xpath="//li[contains(text()),'Administrators']"
    listitemFormmoderators_xpath="//li[contains(text(),'Forum Moderators')]"
    listitemRegistered_xpath="//li[contains(text(),'Registered')]"
    listitemGuests_xpath="//li[contains(text(),'Guests')]"
    listitemVendors_xpath="//li[contains(text(),'Vendors')]"
    drpmanagerofvendors_xpath="//*[@id='VendorId']"
    chkActive_xpath="//input[@id='Active']"
    txtAdminComment_xpath="//textarea[@id='AdminComment']"
    btnSave_xpath="//button[@name='save']"


    def __init__(self,driver):
        self.driver=driver

    def clickonCustomerMenu(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menu_xpath).click()

    def clickonCustomerMenuItem(self):
        self.driver.find_element_by_xpath(self.lnkCustomers_menuitem_xpath).click()

    def clickonAddNew(self):
        self.driver.find_element_by_xpath(self.btnAddNew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element_by_xpath(self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element_by_xpath(self.txtPassword_xpath).send_keys(password)

    def setFirstName(self,firstname):
        self.driver.find_element_by_xpath(self.txtFirstName_xpath).send_keys(firstname)

    def setLastName(self,lastname):
        self.driver.find_element_by_xpath(self.txtLastName_xpath).send_keys(lastname)

    def setDOB(self,DOB):
        self.driver.find_element_by_xpath(self.txtdob_xpath).send_keys(DOB)

    def setNewsLetter(self,newsletter):
        self.driver.find_element_by_xpath(self.txt_newsletter_xpath).click()
        time.sleep(2)
        self.listitemNL=self.driver.find_element_by_xpath(self.listitemNewsLetter_xpath)
        self.driver.execute_script("arguments[0].click();", self.listitemNL)

    def setCompanyName(self,compname):
        self.driver.find_element_by_xpath(self.txt_companyname_xpath).send_keys(compname)
        time.sleep(2)

    def setCustomerRoles(self,role):
        self.driver.find_element_by_xpath(self.txtCustomerRoles_xpath).click()
        time.sleep(3)

        if role=='Registered':
            time.sleep(3)
            self.listitem=self.driver.find_element_by_xpath(self.listitemRegistered_xpath)
        elif role=='Administrators':
            time.sleep(3)
            self.listitem=self.driver.find_element_by_xpath(self.listitemAdministrator_xpath)
        elif role=='Guests':
            time.sleep(3)
            self.driver.find_element_by_xpath("//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.listitem=self.driver.find_element_by_xpath(self.listitemGuests_xpath)
        elif role=='Vendors':
            self.listitem=self.driver.find_element_by_xpath(self.listitemVendors_xpath)
        else:
            self.listitem = self.driver.find_element_by_xpath(self.listitemGuests_xpath)
        time.sleep(3)
        self.driver.execute_script("arguments[0].click();",self.listitem)

    def setManagerofVendor(self,value):
        drp=Select(self.driver.find_element_by_xpath(self.drpmanagerofvendors_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender=='Male':
            self.driver.find_element_by_id(self.rdMaleGender_id).click()
        elif gender=='Female':
            self.driver.find_element_by_id(self.rdFemaleGender_ID).click()
        else:
            self.driver.find_element_by_id(self.rdMaleGender_id).click()

    def setAdminContent(self,content):
        self.driver.find_element_by_xpath(self.txtAdminComment_xpath).send_keys(content)

    def clickOnSave(self):
        time.sleep(2)
        self.driver.find_element_by_xpath(self.btnSave_xpath).click()





