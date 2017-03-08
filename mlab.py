import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds123410.mlab.com:23410/a7-flask-db

host = "ds123410.mlab.com"
port = 23410
db_name = "a7-flask-db"
username = "a7"
password = "a7"

def connect():
    mongoengine.connect(db_name, host=host, port=port, username=username, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]

def item2json(item):
    import json
    return json.loads(item.to_json())