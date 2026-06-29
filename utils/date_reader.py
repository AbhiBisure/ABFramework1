import json

class DataReader:

    @staticmethod
    def get_data(file_name):
       with open (f'data/{file_name}',"r")as f:
           return json.load(f)


    #def get_data(file_name):
    #    path = Path(__file__).parent.parent / "data" / file_name
    #    with open(path, "r") as f:
    #        return json.load(f)
    #
    # DataReader.get_data("home_page_data.json")