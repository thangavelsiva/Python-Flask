#importting required modules
import requests


def postdata(input_data):
    #post call
    response = requests.post("http://localhost:5000/crudapi",json=input_data)
    
    return response.json()  # return response from server

#input data with database and collection and document to be created or inserted    
input_data = {
        
    "database":"ABC_company",
    "collection":"Employee",
    "document":
    {   "user_id":"siva",
        "processor":"i5",
        "cpu":8,
        "gpu":4
    }
}

result = postdata(input_data)
print(result)

#sample output - {'Document_ID': 'siva', 'Status': 'Successfully Inserted'}