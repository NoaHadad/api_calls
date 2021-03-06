import requests
import json

address='http://35.184.29.91/api/'
dict={'update':(address+'quote-update'),'create':(address+'quote-create'),'list':(address+'quote-list'),'detail':(address+'quote-detail/'),'delete':(address+'quote-delete/')}

a=json.load(open('/home/noa/myproject/myproject/example/a.json'))
b=json.load(open('/home/noa/myproject/myproject/example/b.json'))
c=json.load(open('/home/noa/myproject/myproject/example/c.json'))
d=json.load(open('/home/noa/myproject/myproject/example/d.json'))
e=json.load(open('/home/noa/myproject/myproject/example/e.json'))
f=json.load(open('/home/noa/myproject/myproject/example/f.json'))
h=json.load(open('/home/noa/myproject/myproject/example/h.json'))
a_update=json.load(open('/home/noa/myproject/myproject/example/a_update.json'))
c_update=json.load(open('/home/noa/myproject/myproject/example/c_update.json'))
c_create=json.load(open('/home/noa/myproject/myproject/example/c_create.json'))
empty_string_update=json.load(open('/home/noa/myproject/myproject/example/empty_name_update.json'))

#getting access token
credentials = {'username':'noa','password':'1234'}
access=requests.post('http://35.184.29.91/api-token-auth/',data = credentials).json()
print()
print('Access token: '+access['token'])
print()
headers={'Authorization':('Token '+access['token'])} #,'content-Type': 'application/json'}

print("1) creatig a ",a)
print(requests.post(dict['create'],headers=headers,json=a).json())
print()

print("2) creatig b ",b)   
print(requests.post(dict['create'],headers=headers,json=b).json())
print()

print("3) creatig a again ")
print(requests.post(dict['create'],headers=headers,json=a).json())
print()

print("quotes: ")
print(requests.get(dict['list'],headers = headers).json())
print()

print("4) updating c (which doesn't exist) ",c_update)
print(requests.post(dict['update'],headers=headers,json=c_update).json())
print()

print("5) deleting b (soft deletion) ")
print(requests.delete(dict['delete']+'b',headers=headers).json())
print()

print("6) trying to get b ")
print(requests.get(dict['detail']+'b',headers = headers).json())
print()

print("7) deleting b again (flag 'deleted' is on) ")
print(requests.delete(dict['delete']+'b',headers=headers).json())
print()

print("8) updating b (flag 'deleted' is on)")
print(requests.post(dict['update'],headers=headers,json=b).json())
print()

print("9) creating b ", b)  
print(requests.post(dict['create'],headers=headers,json=b).json())
print()

print("10) creating c ", c)
print(requests.post(dict['create'],headers=headers,json=c).json())
print()

print("11) updating c (price changed to 88) ",c_update)        
print(requests.post(dict['update'],headers=headers,json=c_update).json())    
print(requests.get(dict['detail']+'c',headers = headers).json())
print()

print("12) creating d (price is negative) ",d)
print(requests.post(dict['create'],headers=headers,json=d).json())  
print()

print("13) creating e (str is empty) ",e) 
print(requests.post(dict['create'],headers=headers,json=e).json())  
print()

print("14) updating a with negative price ",a_update)
print(requests.post(dict['update'],headers=headers,json=a_update).json())
print()

print("15) updating name with empty string ",empty_string_update)
print(requests.post(dict['update'],headers=headers,json=empty_string_update).json())
print()

print("16) deleting a")
print(requests.delete(dict['delete']+'a',headers=headers).json())
print()

print("17) creating f (field price is missing) ",f)       
print(requests.post(dict['create'],headers=headers,json=f).json())
print()

print("18) creating c (field price is negative and c already exists) ",c_create)
print(requests.post(dict['create'],headers=headers,json=c_create).json())
print()

print("19) updating h (field price is negative and quote with this name doesn't exists) ",h)
print(requests.post(dict['update'],headers=headers,json=h).json())
print()

print("quotes: ")
print(requests.get(dict['list'],headers = headers).json())
print("quote 'a' is in the DB with flag 'deleted' sets to 1" )
