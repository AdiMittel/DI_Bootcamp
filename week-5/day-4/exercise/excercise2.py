import json
sampleJson ={ 
   "company":{ 
      "employee":{ 
         "name":"emma",
         "payable":{ 
            "salary":7000,
            "bonus":800
         }
      }
   }
}
with open('main.json','w') as f:
    json.dump(sampleJson,f,indent=2)
    f.close()
with open ('main.json','r') as file:    
    salary = json.load(file)
    file.close()
print(salary['company']['employee']['payable']['salary'])
salary['company']['employee']['birthdate'] = '11.11.1900'
with open('main.json','w') as f:
    json.dump(salary,f,indent=2)
    f.close()

