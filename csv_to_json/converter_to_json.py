import csv 
import json 

from manual import ManualCsvConverter
def read_built_in(file): 
    jsonArray = []
    with open(file, encoding='utf-8') as f: 
            content = csv.DictReader(f) 
            for row in content: 
                jsonArray.append(row)
    return jsonArray

def write_built_in(file,data):
    with open(file, 'w', encoding='utf-8') as f: 
        f.write(json.dumps(data, indent=4)) 
        
def read_data_to_list(file_name):
    file = open(file_name)
    content = file.readlines()
    file.close()
    return content



def write_data(file_name, data):
    file = open(file_name, 'w')
    file.write(data)
    file.close()
        
        
def main():
    data = read_data_to_list("input.csv")
    converter = ManualCsvConverter(data)
    result = converter.to_json()
    write_data("output.json", result)
    
#     data=read_built_in("input.csv")
#     write_built_in("output.json",data)
    
if __name__ == "__main__":
    main()