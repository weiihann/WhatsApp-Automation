"""
File containing Application class

Author: Ng Wei Han
"""

from whatsapp_automation import WhatsAppAutomation
from user_interface import UserInterface
from file_operation import FileOperation
import time
import sys

class Application:
    OPTIONS = ["Manually input customer names", "Read from .csv or .xlsx file"]

    def __init__(self):
        self.ui = UserInterface()
        self.name_staff = "I am a worker"

    def manual_input(self):
        while True:
            user_input = input("Please enter person name. (Press Ctrl + C to quit)\n")
            if user_input == "q":
                sys.exit(0)
            try:
                self.searching(user_input)
            except:
                continue

            self.ui.print_divider()

    def read_from_file(self, file_name):
        file_reader = FileOperation(file_name)
        contacts = file_reader.get_column(0)
        for name in contacts:
            try:
                self.searching(name)
            except ValueError:
                print("Empty name cannot be processed.")

    def searching(self, name_cus):
        if name_cus == "":
            raise ValueError("Cannot be empty")

        try:
            self.bot.search_user(name_cus)
        except:
            print("{} not found".format(name_cus))
            while True:
                try:
                    self.bot.search_again()
                except:
                    time.sleep(1)
                    continue
                else:
                    break
        else:
            self.bot.find_msg_box()
            self.bot.send_message("Hi {}!\n".format(name_cus) +
                                  "{} here from PichaEats.\n".format(self.name_staff) +
                                  "How was the food yesterday? :)")

    def run(self):
        self.ui.print_message("Welcome to WhatsApp Automation program!")
        self.ui.print_message("Please read the read_me file before proceeding to using this program.")
        self.ui.print_divider()

        # Enter staff name
        self.name_staff = input("Enter your name: ")
        self.ui.print_divider()

        self.ui.print_options(self.OPTIONS)

        # Allow user to choose option
        selected = self.ui.num_input("Please select an option: ", 1, len(self.OPTIONS))
        self.ui.print_divider()

        self.bot = WhatsAppAutomation()
        # Run operation based on option
        self.bot.navigate()
        self.bot.search_user_box()
        time.sleep(3)

        if selected == 1:
            self.manual_input()
        elif selected == 2:
            while True:
                file_name = input("Please enter file name (eg. customer_list.csv | Press Ctrl + C to quit): ")
                try:
                    self.read_from_file(file_name)
                except:
                    print("File not found. Please enter again.")
                    continue
                break
            print("Press Ctrl + C to quit.")

application = Application()
application.run()
sys.exit(0)
