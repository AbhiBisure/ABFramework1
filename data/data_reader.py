import json

class DataReader:

    @staticmethod
    def get_data(file_name):
       with open (f'data/{file_name}')as f:
           return json.load(f)
