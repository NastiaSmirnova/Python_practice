import csv 
import json 


def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()
    
def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content  
 
def prepare_data(data):
    title = data.pop(0).strip().split(',')
    return title, data


def convert_row_to_pretty_json(keys, row):
    values = row.strip().split(',')
    d=dict(zip(keys, values))
    
    template ="""{{
"id": {},
"name": {},
"birth": {},
"salary": {},
"department": {}
    }}"""
    return template.format(*values)

def convert_csv_to_json(data):
    title, data = prepare_data(data)
    result = [convert_row_to_pretty_json(title, row) for row in data]  
    return str(result)

# вариант считывания и записи при помощи модуля csv и json
def read_csv(file): 
    jsonArray = []
    with open(file, encoding='utf-8') as f: 
            content = csv.DictReader(f) 
            for row in content: 
                jsonArray.append(row)
    return jsonArray

def write_json(file,data):
    with open(file, 'w', encoding='utf-8') as f: 
        f.write(json.dumps(data, indent=4))     
    
def main(param):
    if param==False:
        data=read_csv("input.csv")
        write_json("output.json",data)
    else:
        data = read_data_to_list("input.csv")
        result = convert_csv_to_json(data)
        write_data("output.json", result)


if __name__ == "__main__":
    main(False) #True - вариант с использованием функций из модуля csv и json, False - самописный вариант