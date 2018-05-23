import time
def login(driver):
    driver.wait_activity(".activity.LoginActivity",10)
    EditText = driver.find_elements_by_class_name("android.widget.EditText")
    EditText[0].send_keys("13410066133")
    EditText[1].send_keys("1234567a")
    driver.find_element_by_id("com.happy.food:id/login").click()
    time.sleep(4)
    try:
        driver.find_element_by_xpath("//android.widget.Button[contains(@text,'允许')]").click()
    except:
        pass