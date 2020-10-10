from fastapi import FastAPI
from src.bean.registration import SignUp
from src.client.mongo_db_client import MongoDBClient

MDClient = MongoDBClient()

app = FastAPI()


@app.get('/')
def index():
    return {'key': 'value'}


@app.get('/login/{userid}')
def login_credentials(userid: int, password: str):
    result = MDClient.Collection.find({'UserId': userid, 'password': password},
                                      {'_id': 0, 'id': 1, 'name': 1,
                                       'email': 1, 'phone_number': 1,
                                       'Reference_ID': 1})
    user_details = [i for i in result]
    return user_details


@app.post('/signup')
def signup_credentials(signup: SignUp):
    result = MDClient.Collection.find()
    res = [i for i in result]
    Dict = signup.dict()
    if len(res) == 0:
        Dict['UserId'] = 0
    else:
        Dict['UserId'] = res[-1]['UserId'] + 1
    if signup.password == signup.confirm_password:
        MDClient.Collection.insert_one(Dict)
        return "registration successful and your UserId is: " + str(Dict['UserId'])
    else:
        return "password mismatch"


@app.put("/{userid}")
def update_password(userid: int, new_password: str):
    filter = {'UserId': userid}
    newvalues = {"$set": {'password': new_password, 'confirm_password': new_password}}
    MDClient.Collection.update_one(filter, newvalues)
    return "your password successfully updated"

@app.delete("/{userid}")
def remove_data(userid: int, password: str):
    MDClient.Collection.delete_one({'UserId': userid, 'password': password})
    return "You are no longer in our database"