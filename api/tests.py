import unittest
import requests
import json

class ApiTestCase(unittest.TestCase):

  def test_createQuote_name(self):

    file=open("/home/noa/myproject/myproject/api/test_name.json")
    data=json.load(file)
    file.close()

    expected={"errorCode": 2,"description": "input is not valid", "level": "error"}  
    result = requests.post('http://35.184.29.91/api/quote-create',headers = {'Authorization':'Token 7250270b0d6d401c05d1375c43845729f17af91f'},json=data).json()

    print("test empty name") 
    print("quote   : ",data)
    print("expected: ",expected)
    print("result  : ",result)

    self.assertEqual(expected,result)

  def test_createQuote_price(self):

    file=open("/home/noa/myproject/myproject/api/test_price.json")
    data=json.load(file)
    file.close()

    expected={"errorCode": 2,"description": "input is not valid", "level": "error"}
    result = requests.post('http://35.184.29.91/api/quote-create',headers = {'Authorization':'Token 7250270b0d6d401c05d1375c43845729f17af91f'},json=data).json()

    print()
    print("test negative price")
    print("quote   : ",data)
    print("expected: ",expected)
    print("result  : ",result)

    self.assertEqual(expected,result)


if __name__=='__main__':
    unittest.main()
