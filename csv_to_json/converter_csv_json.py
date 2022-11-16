import csv 
import json 
class converter_csv_json:
    def __init__(self):
        pass
    
    def read_data(self,file_name):
        file = open(file_name)
        content = file.read()
        file.close()
        return content

    def write_data(self,file_name, data):
        file = open(file_name, 'w')
        file.write(data)
        file.close()

    def read_data_to_list(self,file_name):
        file = open(file_name)
        content = file.readlines()
        file.close()
        return content  

    def prepare_data(self,data):
        title = data.pop(0).strip().split(',')
        return title, data


    def convert_row_to_pretty_json(self,keys, row):
        values = row.strip().split(',')
        d=dict(zip(keys, values))

        template ="""{{
    "id": {},
    "name": {},
    "birth": {},
    "salary": {},
    "department": {}
        }}"""
        print(template.format(*d.values()))
        return template.format(*d.values())

    def convert_csv_to_json(self,data):
        title, data = self.prepare_data(data)
        result = [self.convert_row_to_pretty_json(title, row) for row in data]  
        return str(result)

    # вариант считывания и записи при помощи модуля csv и json
    def read_csv(self,file): 
        jsonArray = []
        with open(file, encoding='utf-8') as f: 
                content = csv.DictReader(f) 
                for row in content: 
                    jsonArray.append(row)
        return jsonArray

    def write_json(self,file,data):
        with open(file, 'w', encoding='utf-8') as f: 
            f.write(json.dumps(data, indent=4))     
    def main(self,param):
        if param==False:
            data=self.read_csv("input.csv")
            self.write_json("output.json",data)
        else:
            data = self.read_data_to_list("input.csv")
            result = self.convert_csv_to_json(data)
            self.write_data("output.json", result)
