#importting required modules
import requests


def getdata(input_data):
    #get call
    response = requests.get("http://localhost:5000/crudapi",json=input_data)
    
    return response.json()  # return response from server

#input data with database and collection    
input_data = {  "database":"ABC_company",
                "collection":"Employee"
            }

result = getdata(input_data)
print(result)

#sample output - [{'cpu': 4, 'gpu': 4, 'processor': 'i5', 'user_id': 'siva'}]
