from flask import Flask, request, json, Response #import flask modules required for creating endpoint
from Modules import crud_api  #importing our custom module for CRUD operations

# initialized the Flask APP
app = Flask(__name__)




@app.route('/crudapi', methods=['GET'])   # Read/get  data from database through get method
def read_data():
    data = request.json
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    read_obj = crud_api.CrudAPI(data)
    response = read_obj.read()
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')


@app.route('/crudapi', methods=['POST'])    # create/insert data  into database through post method
def create():
    data = request.json
    if data is None or data == {} or 'document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    create_obj = crud_api.CrudAPI(data)
    response = create_obj.insert_data(data)
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')

@app.route('/crudapi', methods=['PUT'])     # update existing data  in database through put method
def update():
    data = request.json
    if data is None or data == {} or 'filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    update_obj = crud_api.CrudAPI(data)
    response = update_obj.update_data()
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')


@app.route('/crudapi', methods=['DELETE'])    # delete existing data  in database through delete method
def delete():
    data = request.json
    if data is None or data == {} or 'filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400, mimetype='application/json')
    delete_obj = crud_api.CrudAPI(data)
    response = delete_obj.delete_data(data)
    return Response(response=json.dumps(response), status=200,
                    mimetype='application/json')
    
    
@app.route('/backup',methods=['GET'])     # backup mongodb data into json file
def backup():
    try:
            
        result ={}
        data = { "database":"ABC_company", "collection":"Employee" }
        
        read_obj = crud_api.CrudAPI(data)
        mongo_data = read_obj.read()
        backup_file_path ='./backup_mongodb/backup_mongodb.json'
        with open(backup_file_path,'w') as f:
            for details in mongo_data:
     
                result.update({details['user_id']: { key:value for key,value in details.items() if key !='user_id' } })  # formating the mongodb data
            json.dump(result,f)
        return Response(response=json.dumps({"status":"successfully backed up into file","filepath":backup_file_path}), status=200,
                        mimetype='application/json')
    except:
        return Response(response=json.dumps({"status":"Error in file backup. Please check database connection"}), status=400,
                        mimetype='application/json')
        


if __name__ == '__main__':
    app.run(debug=True, port=5000,host = "0.0.0.0")  #application runs in debug mode