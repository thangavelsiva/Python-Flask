#importing required modules
import requests


def deletedata(input_data):
    #delete call
    response = requests.delete("http://localhost:5000/crudapi",json=input_data)
    
    return response.json()  # return response from server

#input data with database and collection and document to be deleted    
input_data = {
        
    "database":"ABC_company",
    "collection":"Employee",
    "filter":
    {  
     "user_id":"siva"
     }
    }


result = deletedata(input_data)
print(result)

#sample output - {'Status': 'Successfully Deleted'} or {'Status': 'Document not found.'}