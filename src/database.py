import json
import uuid
from mysql.connector import connect, Error
from typing import Optional
from datetime import datetime

url = 1
def getNoteins(
    id: int,
    url: str,                  
    title: str,                 
    description: Optional[str],  
    tags: dict[str,str],           
    createdDate: datetime,       
    updateDate: datetime   ):
    try:
        with connect(
            host="localhost",
            user="root",
            password="11111",
            database="noteins",
        ) as conn:
            with conn.cursor() as cursor:
                new_note = (url, title, description, json.dumps(tags), createdDate, updateDate,id)
                request_to_insert_data = "INSERT INTO Notein(url, title, description, tags, createdDate, updateDate,id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                cursor.execute(request_to_insert_data, new_note)
                conn.commit()
    except Error as e:
        print(e)

dt = datetime.now()
getNoteins(int(uuid.uuid4()),'url', 'title', 'description', {'tag1': 'value1', 'tag2': 'value2'}, dt , dt,)
