import unittest
from salary_service import  Salary_per_hour_service

class Salary_service_Tests(unittest.TestCase):


    def test_convert_month_to_str(self):
        data = { "year": 2010, "month": "JANUARY", "salary": 40000}
        year, month, salary = data.get('year'), data.get('month'), data.get("salary")
        service= Salary_per_hour_service(year, month, salary)
        
        exp='01'
        self.assertEqual(service.convert_month_to_str(month), exp)

    def test_find_work_days(self):
        data = { "year": 2015, "month": "JULY", "salary": 65000}
        year, month, salary = data.get('year'), data.get('month'), data.get("salary")
        service= Salary_per_hour_service(year, month, salary)
        exp= 23
        self.assertEqual(service.find_work_days(), exp)   

    def test_find_salary(self):
        data = { "year": 2021, "month": "February", "salary": 95500}
        year, month, salary = data.get('year'), data.get('month'), data.get("salary")
        service= Salary_per_hour_service(year, month, salary)

        exp= 628.29
        self.assertEqual(service.find_salary(), exp)  
if __name__ == "__main__":
    unittest.main()