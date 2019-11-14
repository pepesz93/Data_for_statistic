#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
#driver = webdriver.PhantomJS()
driver = webdriver.Chrome()
def main():
    try:
        driver.get("http://swaid.stat.gov.pl/_layouts/15/ReportServer/RSViewerPage.aspx?rv:RelativeReportUrl=/PrzedsiebiorstwaNiefinansowe/Raporty/RAP_F01_205_3_t.rdl&rp:Jezyk=pl-PL&rp:styl=5&rv:HeaderArea=None&rv:AsyncRender=false&rv:ToolBarItemsDisplayMode=207")
     
        elem = driver.find_element_by_id("m_sqlRsWebPart_ctl00_ctl19_ctl06_ctl05_ddDropDownButton")
        elem.click()        

        elem = driver.find_element_by_id("m_sqlRsWebPart_ctl00_ctl19_ctl06_ctl05_divDropDown_ctl00")
        elem.click()

        elem = driver.find_element_by_name("m_sqlRsWebPart$ctl00$ctl19$ApplyParameters")
        elem.click()
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.NAME, "m_sqlRsWebPart$ctl00$ctl19$ApplyParameters")))
                
        elem = driver.find_element_by_id("m_sqlRsWebPart_RSWebPartToolbar_ctl00_RptControls_RSActionMenu_ctl01_t")
        elem.click()

        time.sleep(5)
        elemHover = driver.find_element_by_id("mp1_0_0_Anchor")

        action= ActionChains(driver)
        action.move_to_element(elemHover).perform()
 
        elem = driver.find_element_by_id("mp1_1_1_Anchor")
        elem.click()
        time.sleep(50)
        driver.quit()
        
    except Exception ,e:
        driver.quit()
        with open("Error log.txt", "w") as f:
            f.write(e[0])
            f.close()


if __name__ == "__main__":
    main()

