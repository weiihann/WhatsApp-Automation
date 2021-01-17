"""
File containing class UserInterface

Author: Ng Wei Han
"""
from typing import List

class UserInterface:

    def __init__(self):
        pass

    def num_input(self,message,lower_bound=None,upper_bound=None):

        user_input = 0

        while True:
            try:
                user_input = int(input(message))
                if lower_bound is not None:
                    if user_input < lower_bound:
                        raise ValueError("Number input cannot be less than lower bound")

                if upper_bound is not None:
                    if user_input > upper_bound:
                        raise ValueError("Number input cannot be more than upper bound ")
            except:
                print("Please reenter option again")
                continue

            break

        return user_input

    def print_divider(self):
        print("--------------------")

    def print_options(self,lst:List):
        for i in range(len(lst)):
            print(str(i+1) + ". {}".format(lst[i]))
        print()

    def print_message(self,message):
        print(message)
