from fastapi import FastAPI,APIRouter
from app.database.schema import client, Message, db
from bson.objectid import ObjectId
some_router = APIRouter() 

def get_message():
    """
    Args : None 
    
    The Function is used to fetch all the data in the DB 
    
    Return Type : List 
    
    """
    cynergy = []
    print (db.message.find())
    for i in db.message.find():
      print(i)
      cynergy.append(Message(**i))
    return {'message is ': cynergy}


def create_message(name:str,message:str):
    """
    Args: 
    \n Name -> str
    \n Message -> str
    
    The Function is used to create only one message and insert the data into DB 
    
    Return Type : List 
    
    """
    ret = db.message.insert_one({"Name":name,"Message":message})
    return {"Name":name,"Message":message}

def remove_message(_id):
    """
    Args: 
    \n _id -> String 
    
    The Function is used to delete one data from DB
    
    Return Type : String
    
    """
    oid = ObjectId(_id)
    try:
        db.message.delete_one({"_id":oid})
        return "Sucessfull"
    except Exception as err:
        print(err)
        
    