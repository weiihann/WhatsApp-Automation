"""
File containing class WhatsAppAutomation

Author: Ng Wei Han
"""

from selenium import webdriver

class WhatsAppAutomation:
    def __init__(self):
        """
        Initialize web driver
        """
        self.driver = webdriver.Chrome()

    def navigate(self):
        """
        Navigate to whatsapp website
        """
        self.driver.get("https://web.whatsapp.com/")
        input("Please scan QR code. Press any key to continue.")

    def find_user(self,name):
        """
        Find user based on the chat list
        :param name: Exact user name
        """
        self.user = self.driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
        self.user.click()
        print("Found user")

    def find_msg_box(self):
        """
        Finding the message box
        """
        inp_xpath = '//div[@class="_1awRl copyable-text selectable-text"][@contenteditable="true"][@data-tab="6"]'
        self.msg_box = self.driver.find_element_by_xpath(inp_xpath)

    def send_message(self,message):
        """
        Inputting message in the message box and pressing the enter button
        """
        self.msg_box.send_keys(message)
        self.driver.find_element_by_class_name("_2Ujuu").click() # Press send button
        print("Message sent correctly")

contacts = ["Wan fang", "Jia Hui", "Ann Drea", "WhatsApp Bot"]

test = WhatsAppAutomation() 
test.navigate()
for name in contacts:
    try:
        test.find_user(name)
    except:
        print("User not found")
        continue

    test.find_msg_box()
    test.send_message("Hi friend please ignore this i'm testing a project")