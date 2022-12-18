import unittest
from manual import ManualCsvConverter



class ManualCsvConverter_Tests(unittest.TestCase):


    def test_prepare_title(self):
        data1 = ManualCsvConverter(['id,name,birth,salary,department\n','2,Nikita,1980,2000,6'])
        data2 = ManualCsvConverter(['id,name,birth,salary\n'])

        self.assertEqual(data1.prepare_title(), ['id','name','birth','salary','department'])
        self.assertEqual(data2.prepare_title(), ['id','name','birth','salary'])
    
    def test_to_json(self):
        data1 = ManualCsvConverter(['id,name\n','2,Nikita'])
        data2 = ManualCsvConverter(['id,name\n']) 
        data3 = ManualCsvConverter(['id,name,birth\n','1,Nikita,','2,,1980',',Vlad,1960'])
        data4 = ManualCsvConverter(['id,name,birth\n','1,Nikita,1978','2,Egor,1980','3,Vlad,1960'])

        self.assertEqual(data1.to_json(), '[{ "id": "2" ,"name": "Nikita"  }]')   
        self.assertEqual(data2.to_json(), '[]')  
        self.assertEqual(data3.to_json(), '[{ "id": "1" ,"name": "Nikita" ,"birth": ""  },{ "id": "2" ,"name": "" ,"birth": "1980"  },{ "id": "" ,"name": "Vlad" ,"birth": "1960"  }]') 
        self.assertEqual(data4.to_json(), '[{ "id": "1" ,"name": "Nikita" ,"birth": "1978"  },{ "id": "2" ,"name": "Egor" ,"birth": "1980"  },{ "id": "3" ,"name": "Vlad" ,"birth": "1960"  }]') 

if __name__== "__main__":
    unittest.main()