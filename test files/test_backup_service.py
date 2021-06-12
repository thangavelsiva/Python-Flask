#importting required modules
import requests


def backupdata():
    #get call to backup data into file
    response = requests.get("http://localhost:5000/backup")
    
    return response.json()  # return response from server


result = backupdata()
print(result)

#sample output -  {'filepath': './backup_mongodb/backup_mongodb.json', 'status': 'successfully backed up into file'}
