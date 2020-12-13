"""
File containing class

Author: Ng Wei Han
"""
import pandas as pd
from typing import List

class FileOperation:
    def __init__(self,file_name):
        if ".csv" in file_name:
            self.df = pd.read_csv(file_name)
        elif ".xlsx" in file_name:
            self.df = pd.read_csv(file_name)
        else:
            raise ValueError("Only .csv and .xlsx file formats are accepted.")

    def get_column(self,num) -> List:
        try:
            result = self.df.iloc[:,num]
        except:
            print("Invalid column number")
        else:
            return list(result)

