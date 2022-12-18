import json
from datetime import datetime
import requests

def read(file):
    with open(file, 'r') as f:
        data = json.load(f)
    return data


def write(file,data,salary_per_hour):
    data["hour_income"] = salary_per_hour
    with open(file, 'w') as f:
        f.write(json.dumps(data, indent=4))


class Salary_per_hour_service:
    def __init__(self, year, month, salary):
        self.year = year
        self.month = self.convert_month_to_str(month)
        self.salary = salary
        self.work_days = self.find_work_days()

    def convert_month_to_str(self,m):
        return '0'+str(datetime.strptime(m.upper(),'%B').month)

    def find_work_days(self):
        url = 'https://isdayoff.ru/api/getdata'
        params = {'year': self.year, 'month': self.month}
        work_days = requests.get(url, params=params).text.count('0')
        return work_days

    def find_salary(self):
        return round(self.salary/(self.work_days*8),2)


def main():
    data = read('input.json')
    year, month, salary = data.get('year'), data.get('month'), data.get("salary")
    salary_per_hour = Salary_per_hour_service(year, month, salary).find_salary()
    write('output.json',data,salary_per_hour)


if __name__ == "__main__":
    main()