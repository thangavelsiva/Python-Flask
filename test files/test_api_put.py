#importting required modules
import requests


def updatedata(input_data):
    #update call
    response = requests.put("http://localhost:5000/crudapi",json=input_data)
    
    return response.json()  # return response from server

#input data with database and collection and document to be updated    
input_data = {
        
    "database":"ABC_company",
    "collection":"Employee",
    "filter":
    {  
     "user_id":"siva"
     },
    "data_to_be_updated" :
        {
            
        "processor":"i7",
        "cpu":8,
        "gpu":4
    }
}

result = updatedata(input_data)
print(result)

#sample output - {'Status': 'Successfully Updated'}